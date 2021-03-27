# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:16:53 2021

@author: eliphat
"""
from .base_node import ExprNode
from ..type_system import EqualityConstraint


class LetBindingExprNode(ExprNode):

    def __init__(self, env, symbol_node, bound_expr, inner, ex_stmts):
        super().__init__(env)
        self.symbol_node = symbol_node
        self.bound_expr = bound_expr
        self.ex_stmts = ex_stmts
        self.inner = inner

    def children(self):
        return [self.symbol_node, self.bound_expr, self.inner] + self.ex_stmts

    def typing(self, ts):
        ts.add_constraint(EqualityConstraint(
            self.symbol_node.value_type_var(),
            self.bound_expr.value_type_var()
        ))

    def value_type_var(self):
        return self.inner.value_type_var()
