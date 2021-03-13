# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:50:46 2021

@author: eliphat
"""
from ..type_var import TypeVar
from ..type_repr import TyphonType
from .base_constraint import BaseConstraint

class FixedConstraint(BaseConstraint):
    def __init__(self, v: TypeVar, T: TyphonType):
        self.v = v
        self.T = T

    def cause_vars(self):
        return []

    def effect_vars(self):
        return [self.v]

    def fix(self):
        self.v.T = self.T

    def is_resolved(self):
        return self.v.T == self.T
