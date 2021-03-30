# -*- coding: utf-8 -*-
"""
Ad-hoc transpilation of function body.
Created on Sun Mar 28 10:04:04 2021

@author: eliphat
"""
import json
from ..core import nodes
from . import sanitize, CommonTranspiler


class FunctionBodyTranspiler(CommonTranspiler):
    def __init__(self, env, indent=0, indent_str="    "):
        super().__init__(indent, indent_str)
        self.statement_delimit = ";"
        self.mapper = {
            nodes.AssignStmtNode: self.statement(self.assign_stmt),
            nodes.AttributeNode: self.expr(self.attribute_exp),
            nodes.BreakStmtNode: self.statement(self.break_stmt),
            nodes.ConstantNode: self.expr(self.constant_exp),
            nodes.ContinueStmtNode: self.statement(self.cont_stmt),
            nodes.ExprStmtNode: self.statement(self.expr_stmt),
            nodes.FuncCallNode: self.expr(self.func_call_exp),
            nodes.IfElseExprNode: self.expr(self.if_else_exp),
            nodes.IfNode: self.statement(self.if_stmt),
            nodes.LetBindingExprNode: self.expr(self.let_binding),
            nodes.LoadNode: self.expr(self.load_name),
            nodes.PlaceholderStmtNode: self.placeholder_stmt,
            nodes.ReturnStmtNode: self.statement(self.return_stmt),
            nodes.SymbolNode: self.expr(self.symbol),
            nodes.WhileNode: self.statement(self.while_stmt),
        }
        self.symbol_use = {k: i for i, k in enumerate(env.symbols.keys())}

    def transpile(self, node):
        return self.mapper[type(node)](node)

    def statement(self, visitor):

        def _statement(node):
            visitor(node)
            self.write(self.statement_delimit)
            self.newline()

        return _statement

    def expr(self, visitor):

        def _expr(node):
            self.write("(")
            visitor(node)
            self.write(")")

        return _expr

    def assign_stmt(self, node):
        self.transpile(node.target)
        self.write(" = ")
        self.transpile(node.expr)

    def expr_stmt(self, node):
        self.transpile(node.expr)

    def attribute_exp(self, node):
        self.transpile(node.base_node)
        self.write("->")
        self.write(node.label)

    def constant_exp(self, node):
        if node.c is None:
            self.write("nullptr")
        else:
            self.write("new ")
            self.write(sanitize(node.value_type_var().T.name))
            self.write("(")
            self.write(json.dumps(node.c))
            self.write(")")

    def func_call_exp(self, node):
        self.transpile(node.func_node)
        self.write("->__call__(")
        for i, arg in enumerate(node.args_nodes):
            if i > 0:
                self.write(", ")
            self.transpile(arg)
        self.write(")")

    def if_else_exp(self, node):
        self.write("*")
        self.transpile(node.test)
        self.write(" ? ")
        self.transpile(node.yes)
        self.write(" : ")
        self.transpile(node.no)

    def block(self, body):
        self.write(" {")
        self.indent += 1
        self.newline()
        for stmt in body:
            self.transpile(stmt)
        self.indent -= 1
        self.write("}")

    def if_stmt(self, node):
        self.write("if (*")
        self.transpile(node.test)
        self.write(")")
        self.block(node.body)
        if node.orelse:
            self.newline()
            self.write("else")
            self.block(node.orelse)

    def while_stmt(self, node):
        self.write("while (*")
        self.transpile(node.test)
        self.write(")")
        self.block(node.body)

    def let_binding(self, node):
        self.indent += 1
        self.statement_delimit = ','
        self.newline()
        self.transpile(node.symbol_node)
        self.write(" = ")
        self.transpile(node.bound_expr)
        self.write(",")
        self.newline()
        for stmt in node.ex_stmts:
            self.transpile(stmt)
        self.transpile(node.inner)
        self.indent -= 1
        self.statement_delimit = ';'
        self.newline()

    def load_name(self, node):
        level = node.env.query_name_level(node.local_name)
        prepend = ""
        if level > 0:
            prepend = level * "__parent_env__->"
        elif level < 0:
            prepend = "::"
        self.write(prepend)
        self.write(node.local_name)

    def break_stmt(self, node):
        self.write("break")

    def cont_stmt(self, node):
        self.write("continue")

    def placeholder_stmt(self, node):
        return

    def return_stmt(self, node):
        self.write("return ")
        self.transpile(node.expr)

    def symbol(self, node):
        if node.symbol not in self.symbol_use:
            self.symbol_use[node.symbol] = len(self.symbol_use)
        self.write("_sym_%d" % self.symbol_use[node.symbol])
