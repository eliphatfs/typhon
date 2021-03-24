# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:27:23 2021

@author: eliphat
"""
from .base_node import StmtNode


class TestedConditionStmtNode(StmtNode):
    def __init__(self, env, test, body, orelse):
        super().__init__(env)
        self.test = test
        self.body = body
        self.orelse = orelse

    def children(self):
        return self.body + self.orelse + [self.test]


class IfNode(TestedConditionStmtNode):
    pass


class WhileNode(TestedConditionStmtNode):
    pass
