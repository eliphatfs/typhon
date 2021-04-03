using System;
using System.Text.Json;
using System.Reflection.Emit;

namespace TyphonHIRBackend
{
    public class InstructionCompiler
    {
        HIRCompiler ctx;
        ILGenerator generator;
        JsonElement ircb;
        public Label blockStart;
        public InstructionCompiler(HIRCompiler context, ILGenerator builder, long codeBlock)
        {
            ctx = context;
            generator = builder;
            blockStart = builder.DefineLabel();
            var cbo = ctx.hirObject.GetProperty(codeBlock.ToString());
            System.Diagnostics.Trace.Assert(cbo.GetProperty("OBJ_KID").GetString() == "cb");
            ircb = cbo.GetProperty("children");
        }

        public void Compile()
        {
            generator.MarkLabel(blockStart);
            foreach (var ins in ircb.EnumerateArray())
                switch (ins[0].GetString())
                {
                    case "LA":
                        generator.Emit(OpCodes.Ldarg_S, ins[1].GetByte());
                        break;
                    case "NO":
                        generator.Emit(OpCodes.Newobj, ctx.typeMap[ins[1].GetInt64()].GetConstructor(new Type[0]));
                        break;
                    case "I4":
                        generator.Emit(OpCodes.Ldc_I4, ins[1].GetInt32());
                        break;
                    case "CM":
                        generator.Emit(OpCodes.Call, ctx.methodMap[ins[1].GetInt64()]);
                        break;
                    case "IF":
                        var tCompiler = new InstructionCompiler(ctx, generator, ins[1].GetInt64());
                        var fCompiler = new InstructionCompiler(ctx, generator, ins[2].GetInt64());
                        generator.Emit(OpCodes.Brfalse, fCompiler.blockStart);
                        var eoif = generator.DefineLabel();
                        tCompiler.Compile();
                        generator.Emit(OpCodes.Br, eoif);
                        fCompiler.Compile();
                        generator.MarkLabel(eoif);
                        break;
                    case "SP":
                        generator.Emit(OpCodes.Pop);
                        break;
                    case "FR":
                        generator.Emit(OpCodes.Ret);
                        break;
                }
        }
    }
}
