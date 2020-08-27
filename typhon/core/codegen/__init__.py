# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:59:56 2020

@author: eliphat
"""
import dis
import sys
import string
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
tampered_format = """
{tamper} {name} ({var_list}) {{{code}}}
"""


def generate(imp):
    modifier = "static"
    var_list = ', '.join(t.c_name + ' ' + b
                         for t, b in zip(imp.types, imp.varnames))
    return gen_format.format(
        result_type=imp.result_type.c_name,
        name=name_of(imp.name, imp.types),
        code=imp.code,
        modifier=modifier,
        var_list=var_list
    )


class BootstrappingImplementation(Implementation, AbstractImplementation):

    def implements(self, interface):
        return self.name == interface.name and self.types == interface.types

    def generate(self):
        return generate(self)

    def get_name(self):
        return name_of(self.name, self.types)

    def get_result_type(self):
        return self.result_type

    def get_used_types(self):
        t = set(self.types)
        t.add(self.result_type)
        return t

    def get_dependencies(self):
        return tuple()


class Polymorphic:
    def try_instantiate(self, interface, existence_mem):
        raise NotImplementedError


def identifierize(s):
    return ''.join(map(lambda x: x if x in string.ascii_letters else '_', s))


def name_of(name, types):
    if len(types) == 0:
        return name
    return '_'.join([name] + [identifierize(t.c_name) for t in types])


def impl(name, types, result_type, varnames, code, inc=None, inl=True):
    if inc is None:
        inc = tuple()
    if isinstance(inc, str):
        inc = (inc,)
    base_impls[name].append(BootstrappingImplementation(
        name, types, result_type, varnames, code, inc, inl
    ))


def find_implementation(interface, existence_mem):
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
            poly = python_impl.PythonAbstraction(target)
            imp = poly.try_instantiate(interface, existence_mem)
            if imp is not None:
                base_impls[interface.name].append(imp)
                return imp
    return None


from . import numeric_impl, string_impl, range_impl, python_impl
from . import generator_main
