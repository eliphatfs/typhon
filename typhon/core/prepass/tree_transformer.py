# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:51:36 2021

@author: eliphat
"""
import ast

from ..type_system.type_var import TypeVar
from ..environment import NodeEnv
from ..abstract_variable import AbstractVariable
from ..nodes import PlaceholderStmtNode, AssignStmtNode, ExprStmtNode
from ..nodes import FuncCallNode, AttributeNode, ConstantNode, LoadNode
from ..nodes import IfElseExprNode
from ..nodes import ReturnStmtNode, FuncDefNode
from ..nodes import IfNode, WhileNode, RaiseStmtNode
from ..nodes import TryExceptNode, ExceptHandlerNode
from ..nodes import SymbolNode, LetBindingExprNode
from ..nodes import BreakStmtNode, ContinueStmtNode
from . import ast_extensions


class PolymorphicFunction:
    def __init__(self, root_env, root_ast_node):
        self.root_env = root_env
        self.root = root_ast_node
        self.instances = []

    def match_instance(self, args_types):
        for inst, args in self.instances:
            if args == args_types:
                return inst
        return None

    def expand_on_args(self, ts, args_types):
        env = self.root_env
        cinst = self.match_instance(args_types)
        if cinst is not None:
            return cinst
        nenv = NodeEnv(env.qualname + self.root.name + str(args_types) + " > ", env, self.root)
        nenv.bindings["@RET"] = AbstractVariable(None, "@RET")
        for arg, T in zip(self.root.args.args, args_types):
            argTV = ts.add_var(TypeVar(nenv.qualname + arg.arg, T))
            nenv.bindings[arg.arg] = AbstractVariable(argTV, arg.arg)
        ninst = typhon_tree(nenv, self.root)
        ninst.typing_all_subs(ts)
        self.instances.append((ninst, args_types))
        return ninst


def typhon_stmt(env: NodeEnv, ast_node: ast.stmt):
    if not isinstance(ast_node, ast.stmt):
        raise TypeError("Malformed AST: got %s for stmt." % ast.dump(ast_node))
    # Section - stmt
    if isinstance(ast_node, ast.Expr):
        sexpr = typhon_expr(env, ast_node.value)
        return ExprStmtNode(env, sexpr)
    if isinstance(ast_node, ast.Return):
        sexpr = typhon_expr(env, ast_node.value)
        return ReturnStmtNode(env, sexpr)
    if isinstance(ast_node, ast.If):
        return IfNode(env,
                      typhon_expr(env, ast_node.test),
                      typhon_body(env, ast_node.body),
                      typhon_body(env, ast_node.orelse))
    if isinstance(ast_node, ast.While):
        return WhileNode(env,
                         typhon_expr(env, ast_node.test),
                         typhon_body(env, ast_node.body),
                         typhon_body(env, ast_node.orelse))
    if isinstance(ast_node, ast.Raise):
        # TODO: cause and re-raise cases of the raise statement
        return RaiseStmtNode(env, typhon_expr(env, ast_node.exc))
    if isinstance(ast_node, ast.FunctionDef):
        if ast_node.args.vararg is not None:
            raise Exception("Function vararg is not yet supported.")
        name = ast_node.name
        if name not in env.bindings:
            env.bindings[name] = AbstractVariable(None, name, PolymorphicFunction(env, ast_node))
        else:
            raise Exception("Function rewritting is not yet supported.")
        return PlaceholderStmtNode(env)
    if isinstance(ast_node, ast.Assign):
        target = ast_node.targets[0]
        if isinstance(target, ast.Name) and target.id not in env.bindings:
            env.bindings[target.id] = AbstractVariable(None, target.id)
            # Type Var creation is deferred to before typing nodes and after parsing
        sexpr = typhon_expr(env, ast_node.value)
        texpr = typhon_expr(env, target)
        return AssignStmtNode(env, sexpr, texpr)
    if isinstance(ast_node, ast.Break):
        return BreakStmtNode(env)
    if isinstance(ast_node, ast.Continue):
        return ContinueStmtNode(env)
    if isinstance(ast_node, ast.Try):
        if len(ast_node.orelse) > 0:
            raise NotImplementedError("try ... else ... is not supported yet")
        return TryExceptNode(
            env,
            typhon_body(env, ast_node.body),
            typhon_except_handlers(env, ast_node.handlers),
            typhon_body(env, ast_node.finalbody)
        )
    raise NotImplementedError("%s is not supported as a statement yet."
                              % type(ast_node))


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
    if isinstance(ast_node, ast.IfExp):
        return IfElseExprNode(env,
            typhon_expr(env, ast_node.test),
            typhon_expr(env, ast_node.body),
            typhon_expr(env, ast_node.orelse)
        )
    if isinstance(ast_node, ast_extensions.Symbol):
        return SymbolNode(env, ast_node)
    if isinstance(ast_node, ast_extensions.LetBinding):
        env.symbols[ast_node.symbol] = None
        return LetBindingExprNode(
            env,
            typhon_expr(env, ast_node.symbol),
            typhon_expr(env, ast_node.bound_expr),
            typhon_expr(env, ast_node.inner),
            typhon_body(env, ast_node.ex_stmts)
        )
    raise NotImplementedError("%s is not supported as an expression yet."
                              % type(ast_node))


def typhon_body(env: NodeEnv, stmts):
    return [typhon_stmt(env, s) for s in stmts]


def typhon_except_handler(env: NodeEnv, handler):
    if not isinstance(handler, ast.ExceptHandler):
        raise TypeError("`except` clause AST should be of type ExceptHandler")
    if handler.name is not None and handler.name not in env.bindings:
        env.bindings[handler.name] = AbstractVariable(None, handler.name)
    return ExceptHandlerNode(
        env,
        typhon_expr(env, handler.type),
        handler.name and LoadNode(env, handler.name),
        typhon_body(env, handler.body)
    )


def typhon_except_handlers(env: NodeEnv, handlers):
    return [typhon_except_handler(env, handler) for handler in handlers]


def typhon_tree(env: NodeEnv, ast_node: ast.AST) -> FuncDefNode:
    if isinstance(ast_node, (ast.Module, ast.FunctionDef)):
        return FuncDefNode(env, typhon_body(env, ast_node.body))
    raise TypeError("AST root should be Module or FuncDef.")
