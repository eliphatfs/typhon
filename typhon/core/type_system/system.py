# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:20:11 2021

@author: eliphat
"""
from . import TypeVar, BaseConstraint


class TypeSystem:
    def __init__(self, program_name: str):
        self.type_vars = []
        self.type_constraints = []
        self.program_name = program_name

    def query_val_type(self, py_val):
        from .intrinsics.builtin_functions import builtin_types_generated
        if type(py_val) is int:
            return builtin_types_generated.builtins_int
        elif py_val is None:
            return builtin_types_generated.NoneType
        elif type(py_val) is bool:
            return builtin_types_generated.builtins_bool
        elif py_val is ...:
            return builtin_types_generated.ellipsis
        if type(py_val) is float:
            return builtin_types_generated.builtins_float
        if type(py_val) is complex:
            return builtin_types_generated.builtins_complex
        if type(py_val) is str:
            return builtin_types_generated.builtins_str
        if type(py_val) is bytes:
            return builtin_types_generated.builtins_bytes
        raise TypeError("Unrecognized type: %s from value %s" % (type(py_val), py_val))

    def add_var(self, v: TypeVar):
        if isinstance(v, TypeVar):
            v.parent_system = self
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
