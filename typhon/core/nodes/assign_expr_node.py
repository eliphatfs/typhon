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
    def __init__(self, env, expr: ExprNode, target: ExprNode):
        super().__init__(env, expr)
        self.target = target

    def children(self):
        return [self.expr, self.target]

    def typing(self, ts):
        ts.add_constraint(SubtypeConstraint(
            self.target.value_type_var(),
            self.expr.value_type_var()
        ))
