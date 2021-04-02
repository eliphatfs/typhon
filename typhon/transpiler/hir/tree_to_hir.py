from ...core import nodes
from . import klass, instructions


class TreeToHIR:
    def __init__(self):
        self.objects = []
        self.mapper = {
            nodes.AssignStmtNode: self.assign_stmt,
            nodes.ExprStmtNode: self.expr_stmt,
            nodes.ConstantNode: self.constant_exp,
            nodes.FuncCallNode: self.func_call_exp,
            nodes.IfNode: self.if_stmt,
            nodes.PlaceholderStmtNode: lambda: []
        }
        self.global_env_klass = klass.HIRClass("__global__")
        bint = klass.HIRClass("builtins.int")
        bint.funcs.append(klass.HIRFunction("__le__", bint, bint, [bint], ))
        bint.funcs.append(klass.HIRFunction("__add__"))
        bint.funcs.append(klass.HIRFunction("__sub__"))
        bint.funcs.append(klass.HIRFunction("__init__"))
        self.klasses = {
            "builtins.int": bint,
            "builtins.bool": bint
        }

    def block_transpile(self, stmts) -> instructions.HIRCodeBlock:
        block = instructions.HIRCodeBlock();
        for stmt in stmts:
            block.extend(self.transpile(stmt))
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
            return instructions.HIRIStoreArgument(indexer)
        elif position == "L":
            return instructions.HIRIStoreLocal(indexer)
        elif position == "G":
            raise NotImplementedError("Global variables are not implemented yet.")

    def load_var_instruction(self, env, name):
        position, indexer = self.find_var(env, name)
        if position == "A":
            return instructions.HIRILoadArgument(indexer)
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
        raise NotImplementedError("Non-member function calls are not implemented yet.")

    def if_stmt(self, node: nodes.IfNode):
        test = self.transpile(node.test)
        test.append(instructions.HIRIIf(
            self.block_transpile(node.body),
            self.block_transpile(node.orelse)
        ))
        return test
