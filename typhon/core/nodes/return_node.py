# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:14:37 2021

@author: eliphat
"""
from .base_node import StmtNode
from ..type_system import SubtypeConstraint


class ReturnStmtNode(StmtNode):
    def __init__(self, env, expr):
        super().__init__(env)
        self.expr = expr

    def children(self):
        return [self.expr]

    def typing(self, ts):
        abs_var = self.env.query_name("@RET")
        ts.add_constraint(SubtypeConstraint(
            abs_var.TV,
            self.expr.value_type_var()
        ))
