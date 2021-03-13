# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:03:36 2021

@author: eliphat
"""
from .base_node import BaseNode
from ..type_system import TypeVar, TypeSystem, FixedConstraint

class ConstantNode(BaseNode):
    def __init__(self, env, constant_value):
        super().__init__(env)
        self.c = constant_value

    def typing(self, ts: TypeSystem):
        vc = TypeVar("Constant %s" % self.c)
        ts.add_var(vc)
        ts.add_constraint(FixedConstraint(vc, ts.query_val_type(self.c)))
