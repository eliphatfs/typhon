# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:14:02 2021

@author: eliphat
"""
from typing import List
from .base_node import ExprNode
from ..type_system import TypeVar, TypeSystem, FuncCallConstraint

class FuncCallNode(ExprNode):
    def __init__(self, env, func_node: ExprNode, args_nodes: List[ExprNode]):
        super().__init__(env)
        self.func_node = func_node
        self.args_nodes = args_nodes
        self.ret_var = None

    def typing(self, ts: TypeSystem):
        vc = ts.add_var(TypeVar("%s:Ret" % self.func_node))
        ts.add_constraint(FuncCallConstraint(
            self.func_node.value_type_var(),
            vc,
            [arg.value_type_var() for arg in self.args_nodes]
        ))
        self.ret_var = vc

    def children(self):
        return [self.func_node] + self.args_nodes

    def value_type_var(self):
        return self.ret_var
