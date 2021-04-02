from ...core import nodes
from . import klass, instructions, hir_container


class TreeToHIR:
    def __init__(self):
        self.hir = hir_container.HIR()
        self.mapper = {
            nodes.AssignStmtNode: self.assign_stmt,
            nodes.ExprStmtNode: self.expr_stmt,
            nodes.ConstantNode: self.constant_exp,
            nodes.FuncCallNode: self.func_call_exp,
            nodes.IfNode: self.if_stmt,
            nodes.PlaceholderStmtNode: lambda _: [],
            nodes.ReturnStmtNode: self.return_stmt,
            nodes.LoadNode: self.load_exp
        }
        self.global_env_klass = klass.HIRClass("__global__")
        dcb = instructions.HIRDummyCodeBlock()
        bint = klass.HIRClass("builtins.int")
        bint.funcs.append(klass.HIRFunction("__le__", bint, [bint], [], dcb))
        bint.funcs.append(klass.HIRFunction("__add__", bint, [bint], [], dcb))
        bint.funcs.append(klass.HIRFunction("__sub__", bint, [bint], [], dcb))
        bint.funcs.append(klass.HIRFunction("__init__", bint, [bint], [], dcb))
        self.hir.objects.append(bint)
        self.hir.objects.append(self.global_env_klass)
        for f in bint.funcs:
            self.hir.objects.append(f)
        self.klasses = {
            "builtins.int": bint,
            "builtins.bool": bint
        }

    def root_transpile(self, root: nodes.FuncDefNode):
        to_handle = []
        for name, bound in root.env.bindings.items():
            if bound.func_binding is not None:
                if len(bound.func_binding.instances) > 1:
                    raise NotImplementedError("Polymorphism is not supported yet.")
                inst, arg_types = bound.func_binding.instances[0]
                ienv = inst.env
                local_list = [
                    self.klasses[v.TV.T.name] for k, v in ienv.bindings.items()
                    if k not in map(lambda x: x.arg, ienv.generator.args.args)
                ]
                self.global_env_klass.funcs.append(klass.HIRFunction(
                    name,
                    self.klasses[ienv.bindings["@RET"].TV.T.name],
                    [self.klasses[arg_t.name] for arg_t in arg_types],
                    local_list, None
                ))
                to_handle.append((self.global_env_klass.funcs[-1], inst))
        self.global_env_klass.funcs.append(
            klass.HIRFunction(
                "__main__",
                None,
                [],
                [],
                self.block_transpile(root.body)
            )
        )
        for func, inst in to_handle:
            func.body_block = self.block_transpile(inst.body)
        for f in self.global_env_klass.funcs:
            self.hir.objects.append(f)

    def block_transpile(self, stmts) -> instructions.HIRCodeBlock:
        block = instructions.HIRCodeBlock()
        for stmt in stmts:
            block.extend(self.transpile(stmt))
        self.hir.objects.append(block)
        return block

    def transpile(self, node) -> list:
        return self.mapper[type(node)](node)

    def find_var(self, env, name):
        arg_list = []
        if env.generator is not None:
            arg_list.extend(map(lambda x: x.arg, env.generator.args.args))
            if name in arg_list:
                return "A", arg_list.index(name)
        local_list = [x for x in env.bindings.keys() if x not in arg_list]
        if name in local_list:
            return "L", local_list.index(name)
        return "G", name

    def store_var_instruction(self, env, name):
        position, indexer = self.find_var(env, name)
        if position == "A":
            return instructions.HIRIStoreArgument(indexer + 1)
        elif position == "L":
            return instructions.HIRIStoreLocal(indexer)
        elif position == "G":
            raise NotImplementedError("Global variables are not implemented yet.")

    def load_var_instruction(self, env, name):
        position, indexer = self.find_var(env, name)
        if position == "A":
            return instructions.HIRILoadArgument(indexer + 1)
        elif position == "L":
            return instructions.HIRILoadLocal(indexer)
        elif position == "G":
            raise NotImplementedError("Global variables are not implemented yet.")

    def assign_stmt(self, node: nodes.AssignStmtNode):
        expr_ir = self.transpile(node.expr)
        if isinstance(node.target, nodes.LoadNode):
            expr_ir.append(self.store_var_instruction(node.env, node.target.local_name))
            return expr_ir
        else:
            raise NotImplementedError(
                "Only variable-target assignment is supported now."
            )

    def expr_stmt(self, node: nodes.ExprStmtNode):
        expr_ir = self.transpile(node.expr)
        expr_ir.append(instructions.HIRIPop())
        return expr_ir

    def constant_exp(self, node: nodes.ConstantNode):
        klass = self.klasses[node.value_type_var().T.name]
        return [
            instructions.HIRINewObject(klass),
            instructions.HIRIPushInt32(int(node.c)),
            instructions.HIRICallMember(klass.find_sub("__init__"))
        ]

    def load_exp(self, node: nodes.LoadNode):
        return [self.load_var_instruction(node.env, node.local_name)]

    def func_call_exp(self, node: nodes.FuncCallNode):
        if isinstance(node.func_node, nodes.AttributeNode):
            base_ir = self.transpile(node.func_node.base_node)
            base_klass = self.klasses[node.func_node.base_node.value_type_var().T.name]
            for arg in node.args_nodes:
                base_ir.extend(self.transpile(arg))
            base_ir.append(instructions.HIRICallMember(
                base_klass.find_sub(node.func_node.label)
            ))
            return base_ir
        if isinstance(node.func_node, nodes.LoadNode):
            if node.func_node.local_name == "bool":
                return []
            base_ir = [instructions.HIRILoadArgument(0)]
            for arg in node.args_nodes:
                base_ir.extend(self.transpile(arg))
            base_ir.append(instructions.HIRICallMember(
                self.global_env_klass.find_sub(node.func_node.local_name)
            ))
            return base_ir
        raise NotImplementedError("Non-member function calls are not implemented yet.")

    def if_stmt(self, node: nodes.IfNode):
        test = self.transpile(node.test)
        test.append(instructions.HIRIIf(
            self.block_transpile(node.body),
            self.block_transpile(node.orelse)
        ))
        return test

    def return_stmt(self, node: nodes.ReturnStmtNode):
        base = self.transpile(node.expr)
        base.append(instructions.HIRIReturn())
        return base
