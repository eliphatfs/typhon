# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:59:56 2020

@author: eliphat
"""
import dis
import sys
from collections import namedtuple, defaultdict
from ..concepts import AbstractImplementation


def BaseImplementationIndex():
    return defaultdict(list)


base_impls = BaseImplementationIndex()


Implementation = namedtuple(
    "Implementation",
    ["name", "types", "result_type", "varnames", "code", "include", "inline"]
)


gen_format = """
{modifier} {result_type} {name} ({var_list}) {{{code}}}
"""


def generate(imp):
    modifier = "static"
    var_list = ', '.join(t.c_name + ' ' + b
                         for t, b in zip(imp.types, imp.varnames))
    return gen_format.format(
        result_type=imp.result_type.c_name,
        name=name_of(imp),
        code=imp.code,
        modifier=modifier,
        var_list=var_list
    )


class BootstrappingImplementation(Implementation, AbstractImplementation):

    def implements(self, interface):
        return self.name == interface.name and self.types == interface.types

    def generate(self, types):
        return generate(self)

    def get_name(self):
        return self.name

    def get_result_type(self, types):
        return self.result_type

    def get_depedencies(self, types):
        return tuple()


def name_of(imp):
    return imp.get_name() + "_" + str(abs(hash(imp)))


def impl(name, types, result_type, varnames, code, inc=None, inl=True):
    if inc is None:
        inc = tuple()
    if isinstance(inc, str):
        inc = (inc,)
    base_impls[name].append(BootstrappingImplementation(
        name, types, result_type, varnames, code, inc, inl
    ))


from . import numeric_impl, string_impl, range_impl, python_impl


def find_implementation(interface):
    for imp in base_impls[interface.name]:
        if imp.implements(interface):
            return imp
    scope = sys.modules["__main__"]
    if hasattr(scope, interface.name):
        target = getattr(scope, interface.name)
        if callable(target):
            try:
                dis.Bytecode(target)
            except TypeError:
                return None
            imp = python_impl.PythonImplementation(target)
            if imp.implements(interface):
                return imp
    return None
