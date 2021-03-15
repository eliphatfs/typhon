# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:23:00 2021

@author: eliphat
"""
from .base_node import ExprNode
from ..type_system import TypeVar, TypeSystem, MemberConstraint


class AttributeNode(ExprNode):
    def __init__(self, env, base_node: ExprNode, label: str):
        super().__init__(env)
        self.base_node = base_node
        self.label = label
        self.ret_var = None

    def typing(self, ts: TypeSystem):
        vc = ts.add_var(TypeVar("%s.%s" % (self.base_node, self.label)))
        ts.add_constraint(MemberConstraint(
            vc,
            self.base_node.value_type_var(),
            self.label
        ))
        self.ret_var = vc

    def children(self):
        return [self.base_node]

    def value_type_var(self):
        return self.ret_var
