# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:03:36 2021

@author: eliphat
"""
from .base_node import ExprNode, DeterminedValue
from ..type_system import TypeVar, TypeSystem, FixedConstraint

class ConstantNode(ExprNode):
    def __init__(self, env, constant_value):
        super().__init__(env)
        self.c = constant_value
        self.typed_c = None

    def typing(self, ts: TypeSystem):
        vc = ts.add_var(TypeVar("Constant %s" % self.c))
        ts.add_constraint(FixedConstraint(vc, ts.query_val_type(self.c)))
        self.typed_c = DeterminedValue(vc, self.c)

    def value_type_var(self):
        return self.typed_c.TV
