# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:20:11 2021

@author: eliphat
"""
from .intrinsics.py_numerics import py_int
from . import TypeVar, BaseConstraint


class TypeSystem:
    def __init__(self, program_name: str):
        self.type_vars = []
        self.type_constraints = []
        self.program_name = program_name

    def query_val_type(self, py_val: type):
        if type(py_val) is int:
            return py_int
        raise TypeError("Unrecognized type: %s from value %s" % (type(py_val), py_val))

    def add_var(self, v: TypeVar):
        if isinstance(v, TypeVar):
            self.type_vars.append(v)
        raise TypeError("add_var called with wrong type: " + str(type(v)))

    def add_constraint(self, cn: BaseConstraint):
        if isinstance(cn, BaseConstraint):
            self.type_constraints.append(cn)
        raise TypeError("add_constraint called with wrong type: " + str(type(cn)))
