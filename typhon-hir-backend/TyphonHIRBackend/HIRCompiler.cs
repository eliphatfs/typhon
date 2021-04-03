using System;
using System.Linq;
using System.Collections.Generic;
using System.Text.Json;
using System.Reflection;
using System.Reflection.Emit;

namespace TyphonHIRBackend
{
    public class HIRCompiler
    {
        static Dictionary<string, Type> intrinsicTypes = new Dictionary<string, Type> {
            ["builtins.int"] = typeof(Intrinsics.BuiltinsInt)
        };
        public Dictionary<long, Type> typeMap = new Dictionary<long, Type>();
        public Dictionary<long, MethodInfo> methodMap = new Dictionary<long, MethodInfo>();
        public Dictionary<long, InstructionCompiler> uncompiledBlocks = new Dictionary<long, InstructionCompiler>();
        Queue<Action> lazy = new Queue<Action>();
        public JsonElement hirObject;
        ModuleBuilder compiledModule = AssemblyBuilder.DefineDynamicAssembly(
            new AssemblyName(Guid.NewGuid().ToString()),
            AssemblyBuilderAccess.Run
        ).DefineDynamicModule(
            Guid.NewGuid().ToString()
        );

        public HIRCompiler(JsonElement hir) => hirObject = hir;

        void DeclareIntrinsicFunction(
            long fnid,
            Type fnClass,
            JsonElement fnElement)
        {
            methodMap[fnid] = fnClass.GetMethod(fnElement.GetProperty("name").GetString());
        }

        void DeclareFunction(
            long fnid,
            TypeBuilder fnClass,
            JsonElement fnElement
        ) => lazy.Enqueue(() => {
            var method = fnClass.DefineMethod(
                fnElement.GetProperty("name").GetString(),
                MethodAttributes.Public,
                typeMap[fnElement.GetProperty("return_class").GetInt64()],
                fnElement.GetProperty("arg_classes").EnumerateArray().Select(
                    (x) => typeMap[x.GetInt64()]
                ).ToArray()
            );
            methodMap[fnid] = method;
            var generator = method.GetILGenerator();
            foreach (var locType in fnElement.GetProperty("local_classes").EnumerateArray())
                generator.DeclareLocal(typeMap[locType.GetInt64()]);
            var bodyId = fnElement.GetProperty("body_block").GetInt64();
            uncompiledBlocks[bodyId] = new InstructionCompiler(this, generator, bodyId);
        });
        void DeclareClass(JsonProperty csProperty)
        {
            var oid = long.Parse(csProperty.Name);
            var name = csProperty.Value.GetProperty("name").GetString();
            if (intrinsicTypes.ContainsKey(name)) {
                var t = typeMap[oid] = intrinsicTypes[name];
                foreach (var obj in csProperty.Value.GetProperty("funcs").EnumerateArray())
                    DeclareIntrinsicFunction(
                        obj.GetInt64(), t,
                        hirObject.GetProperty(obj.GetInt64().ToString())
                    );
            }
            else {
                var t = compiledModule.DefineType(name, TypeAttributes.Public);
                typeMap[oid] = t;
                foreach (var obj in csProperty.Value.GetProperty("funcs").EnumerateArray())
                    DeclareFunction(
                        obj.GetInt64(), t,
                        hirObject.GetProperty(obj.GetInt64().ToString())
                    );
            }
        }
        void PassDeclare()
        {
            List<JsonProperty> funcs = new List<JsonProperty>();
            foreach (var prop in hirObject.EnumerateObject())
                if ("cs" == prop.Value.GetProperty("OBJ_KID").GetString())
                    DeclareClass(prop);
            while (lazy.Count > 0)
                lazy.Dequeue()();
        }

        void PassGenerate()
        {
            foreach (var ic in uncompiledBlocks.Values)
                ic.Compile();
        }

        void PassTypeCreate()
        {
            foreach (var t in typeMap.Values)
                if (t is TypeBuilder tb)
                    tb.CreateType();
        }

        public ModuleBuilder Compile()
        {
            PassDeclare();
            PassGenerate();
            PassTypeCreate();
            return compiledModule;
        }
    }
}
