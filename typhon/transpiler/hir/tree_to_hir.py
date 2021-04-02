from ...core import nodes
from . import klass, instructions


class TreeToHIR:
    def __init__(self):
        self.objects = []
        self.mapper = {
            nodes.AssignStmtNode: self.assign_stmt
        }
        self.global_env_klass = klass.HIRClass("Typhon.Global")

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
