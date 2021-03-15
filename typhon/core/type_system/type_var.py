# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:34:58 2021

@author: eliphat
"""
from .type_repr import BottomType

class TypeVar:
    def __init__(self, name, init_type=None):
        self.name = name  # name for debugging and error reporting
        self.T = init_type or BottomType()
        self.func_srcs = set()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
