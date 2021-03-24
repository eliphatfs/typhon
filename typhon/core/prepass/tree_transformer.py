# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:51:36 2021

@author: eliphat
"""
import ast

from ..type_system.type_var import TypeVar
from ..nodes import NodeEnv, AbstractVariable
from ..nodes import PlaceholderStmtNode, AssignStmtNode, ExprStmtNode
from ..nodes import FuncCallNode, AttributeNode, ConstantNode, LoadNode
from ..nodes import ReturnStmtNode, FuncDefNode


class PolymorphicFunction:
    def __init__(self, root_ast_node):
        self.root = root_ast_node
        self.instances = []

    def expand_on_args(self, env, ts, args_types):
        for inst, args in self.instances:
            if args == args_types:
                return inst
        nenv = NodeEnv(env.qualname + self.root.name + " > ", env)
        for arg, T in zip(self.root.args.args, args_types):
            nenv.bindings[arg.arg] = AbstractVariable(TypeVar(
                nenv.qualname + arg.arg, T),
            arg.arg)
        ninst = typhon_tree(nenv, self.root)
        ninst.typing_all_subs(ts)
        self.instances.append((ninst, args_types))
        return ninst


def typhon_stmt(env: NodeEnv, ast_node: ast.stmt):
    if not isinstance(ast_node, ast.stmt):
        raise TypeError("Malformed AST: got %s for stmt." % ast.dump(ast_node))
    # Section - trivial
    if isinstance(ast_node, ast.Pass):
        return PlaceholderStmtNode(env)
    # Section - stmt
    if isinstance(ast_node, ast.Expr):
        sexpr = typhon_expr(env, ast_node.value)
        return ExprStmtNode(env, sexpr)
    if isinstance(ast_node, ast.Return):
        sexpr = typhon_expr(env, ast_node.value)
        # TODO: support empty return statements
        return ReturnStmtNode(env, sexpr)
    if isinstance(ast_node, ast.FunctionDef):
        name = ast_node.name
        if name not in env.bindings:
            env.bindings[name] = AbstractVariable(None, name, PolymorphicFunction(ast_node))
        return PlaceholderStmtNode(env)
    if isinstance(ast_node, ast.Assign):
        if len(ast_node.targets) > 1:
            raise NotImplementedError("Multiple-target assignment is not yet supported.")
        target = ast_node.targets[0]
        if isinstance(target, ast.Name) and target.id not in env.bindings:
            env.bindings[target.id] = AbstractVariable(None, target.id)
            # Type Var creation is deferred to before typing nodes and after parsing
        sexpr = typhon_expr(env, ast_node.value)
        texpr = typhon_expr(env, target)
        return AssignStmtNode(env, sexpr, texpr)
    raise NotImplementedError("%s is not supported as a statement yet."
                              % type(ast_node))


bin_op_map = {
    ast.Add: "__add__",
    ast.Sub: "__sub__",
    ast.Mult: "__mul__",
    ast.FloorDiv: "__floordiv__",
    ast.Mod: "__mod__",
    ast.MatMult: "__matmul__",
    ast.LShift: "__lshift__",
    ast.RShift: "__rshift__",
}


def typhon_expr(env: NodeEnv, ast_node: ast.expr):
    if not isinstance(ast_node, ast.expr):
        raise TypeError("Malformed AST: got %s for expr." % ast.dump(ast_node))
    if isinstance(ast_node, ast.Constant):
        return ConstantNode(env, ast_node.value)
    if isinstance(ast_node, ast.Name):
        return LoadNode(env, ast_node.id)
    if isinstance(ast_node, ast.Call):
        return FuncCallNode(env,
            typhon_expr(env, ast_node.func),
            [typhon_expr(env, arg) for arg in ast_node.args]
        )
    if isinstance(ast_node, ast.Attribute):
        return AttributeNode(env, typhon_expr(env, ast_node.value), ast_node.attr)
    if isinstance(ast_node, ast.BinOp):
        left = typhon_expr(env, ast_node.left)
        right = typhon_expr(env, ast_node.right)
        if type(ast_node.op) in bin_op_map:
            f_ov = AttributeNode(env, left, bin_op_map[type(ast_node.op)])
            return FuncCallNode(env, f_ov, [right])
        raise NotImplementedError("Op %s is not yet supported."
                                  % type(ast_node.op))
    raise NotImplementedError("%s is not supported as an expression yet."
                              % type(ast_node))


def typhon_tree(env: NodeEnv, ast_node: ast.AST) -> FuncDefNode:
    if isinstance(ast_node, (ast.Module, ast.FunctionDef)):
        body = [typhon_stmt(env, s) for s in ast_node.body]
        return FuncDefNode(env, body)
    raise TypeError("AST root should be Module or FuncDef.")
