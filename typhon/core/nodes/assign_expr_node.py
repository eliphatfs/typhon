# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:14:49 2021

@author: eliphat
"""
from .base_node import StmtNode, ExprNode
from ..type_system import SubtypeConstraint


class ExprStmtNode(StmtNode):
    def __init__(self, env, expr: ExprNode):
        super().__init__(env)
        self.expr = expr

    def children(self):
        return [self.expr]


class AssignStmtNode(ExprStmtNode):
    def __init__(self, env, expr: ExprNode, target_name: str):
        super().__init__(env, expr)
        self.target = target_name

    def typing(self, ts):
        abs_var = self.env.query_name(self.target)
        ts.add_constraint(SubtypeConstraint(
            abs_var.TV,
            self.expr.value_type_var()
        ))
