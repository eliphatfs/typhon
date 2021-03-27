# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:20:11 2021

@author: eliphat
"""
from .intrinsics.py_numerics import py_int
from .intrinsics.py_bool import py_bool
from .intrinsics.py_none import py_none
from . import TypeVar, BaseConstraint


class TypeSystem:
    def __init__(self, program_name: str):
        self.type_vars = []
        self.type_constraints = []
        self.program_name = program_name

    def query_val_type(self, py_val):
        if type(py_val) is int:
            return py_int
        elif py_val is None:
            return py_none
        elif type(py_val) is bool:
            return py_bool
        raise TypeError("Unrecognized type: %s from value %s" % (type(py_val), py_val))

    def add_var(self, v: TypeVar):
        if isinstance(v, TypeVar):
            self.type_vars.append(v)
            return v
        raise TypeError("add_var called with wrong type: " + str(type(v)))

    def add_constraint(self, cn: BaseConstraint):
        if isinstance(cn, BaseConstraint):
            self.type_constraints.append(cn)
            return cn
        raise TypeError("add_constraint called with wrong type: " + str(type(cn)))

    def solve(self):
        L = len(self.type_vars)
        for i in range(L):
            for c in self.type_constraints:
                c.fix(self)
                if L != len(self.type_vars):
                    return self.solve()
        return self
