# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:34:08 2021

@author: eliphat
"""
from ..type_var import TypeVar
from .base_constraint import BaseConstraint


class EqualityConstraint(BaseConstraint):
    def __init__(self, v_dst: TypeVar, v_src: TypeVar):
        self.dst = v_dst
        self.src = v_src

    def cause_vars(self):
        return [self.src]

    def effect_vars(self):
        return [self.dst]

    def fix(self, ts):
        self.dst.T = self.src.T
        self.dst.func_srcs = set(self.src.func_srcs)

    def is_resolved(self):
        return True
