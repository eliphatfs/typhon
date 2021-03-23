# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:03:44 2021

@author: eliphat
"""
from .base_node import StmtNode, RootNodeMixin


class FuncDefNode(StmtNode, RootNodeMixin):
    def __init__(self, env, body):
        super().__init__(env)
        self.body = body

    def children(self):
        return self.body
