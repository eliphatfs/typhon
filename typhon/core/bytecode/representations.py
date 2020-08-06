# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:12:53 2020

@author: eliphat
"""
from .. import concepts
from ..type_system import base_types
from .. import codegen


class Reduction:

    def reduce(self, impls):
        raise NotImplementedError


class FuncApply(Reduction):

    def __init__(self, name, args=None):
        self.name = name
        self.args = args
        self.impl = None

    def reduce(self, impls):
        if self.args is None:
            raise ValueError("No arguments to reduce.")
        red = []
        for arg in self.args:
            if isinstance(arg, Reduction):
                red.append(arg.reduce(impls))
            else:
                raise TypeError("Non-reducible argument.")
        interface = concepts.Interface(self.name, tuple(a[0] for a in red))
        self.impl = concepts.find_implementation(codegen.base_impls, interface)
        if self.impl is None:
            raise TypeError("Interface %s is not implemented."
                            % repr(interface))
        impls.add(self.impl)
        return (
            self.impl.result_type,
            (concepts.name_of(self.impl)
             + "(" + ', '.join(a[1] for a in red) + ")")
        )


class Constant(Reduction):

    def __init__(self, val):
        self.val = val

    def reduce(self, impls):
        t = base_types.from_const(self.val)
        if self.val is None:
            return t, "_typhon_create_none()"
        if type(self.val) is str:
            return t, '"' + self.val + '"'
        else:
            return t, str(self.val)


class Variable(Reduction):

    def __init__(self, name):
        self.py_type = None
        self.name = name

    def reduce(self, impls):
        return self.py_type, self.name

    def union(self, type_assigned):
        if self.py_type is None:
            self.py_type = type_assigned
        typeset = set((self.py_type, type_assigned))
        if typeset == {base_types.PyInt, base_types.PyFloat}:
            self.py_type = base_types.PyFloat
        if self.py_type == type_assigned:
            return
        raise ValueError("Multiple types for variable %s." % self.name +
                         " This is not yet implemented.")


class TempVar(Reduction):

    def __init__(self, py_type, name, replica):
        self.py_type = py_type
        self.name = name
        self.replica = replica

    def reduce(self, impls):
        return self.py_type, self.name
