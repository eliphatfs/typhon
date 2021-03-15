# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:14:49 2021

@author: eliphat
"""
from .base_node import StmtNode, ExprNode


class ExprStmtNode(StmtNode):
    def __init__(self, env, expr: ExprNode):
        super().__init__(env)
        self.expr = expr

    def children(self):
        return [self.expr]
