# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:51:36 2021

@author: eliphat
"""
import ast
from typing import Optional

from ..nodes import BaseNode, NodeEnv, AbstractVariable
from ..nodes import ExprStmtNode, PlaceholderStmtNode, AssignStmtNode
from ..nodes import FuncCallNode, AttributeNode, ConstantNode, LoadNode


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
    if isinstance(ast_node, ast.Assign):
        if len(ast_node.targets) > 1:
            raise NotImplementedError("Multiple-target assignment is not yet supported.")
        target = ast_node.targets[0]
        assert isinstance(target, ast.Name)
        if target.id not in env.bindings:
            env.bindings[target.id] = AbstractVariable(None, target.id)
            # Type Var creation is deferred to before typing nodes and after parsing
        sexpr = typhon_expr(env, ast_node.value)
        return AssignStmtNode(env, sexpr, target.id)
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


def typhon_tree(env: NodeEnv, ast_node: ast.AST) -> Optional[BaseNode]:
    if isinstance(ast_node, ast.Module):
        return [typhon_stmt(env, s) for s in ast_node.body]
    raise TypeError("AST root should be Module.")
