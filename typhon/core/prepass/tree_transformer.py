# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:51:36 2021

@author: eliphat
"""
import ast
from typing import Optional

from ..nodes import BaseNode, ExprStmtNode, PlaceholderStmtNode
from ..nodes import FuncCallNode, AttributeNode, ConstantNode


def typhon_stmt(env, ast_node: ast.stmt):
    if not isinstance(ast_node, ast.stmt):
        raise TypeError("Malformed AST: got %s for stmt." % ast.dump(ast_node))
    # Section - trivial
    if isinstance(ast_node, ast.Pass):
        return PlaceholderStmtNode(env)
    # Section - stmt
    if isinstance(ast_node, ast.Expr):
        sexpr = typhon_expr(env, ast_node.value)
        return ExprStmtNode(env, sexpr)
    raise NotImplementedError("%s is not supported as a statement yet."
                              % type(ast_node))


def typhon_expr(env, ast_node: ast.expr):
    if not isinstance(ast_node, ast.expr):
        raise TypeError("Malformed AST: got %s for expr." % ast.dump(ast_node))
    if isinstance(ast_node, ast.Constant):
        return ConstantNode(env, ast_node.value)
    if isinstance(ast_node, ast.BinOp):
        left = typhon_expr(env, ast_node.left)
        right = typhon_expr(env, ast_node.right)
        if isinstance(ast_node.op, ast.Add):
            f_add = AttributeNode(env, left, "__add__")
            return FuncCallNode(env, f_add, [right])
        raise NotImplementedError("Op %s is not yet supported."
                                  % type(ast_node.op))
    raise NotImplementedError("%s is not supported as an expression yet."
                              % type(ast_node))


def typhon_tree(env, ast_node: ast.AST) -> Optional[BaseNode]:
    if isinstance(ast_node, ast.Module):
        return [typhon_stmt(env, s) for s in ast_node.body]
    raise TypeError("AST root should be Module.")
