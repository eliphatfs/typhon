# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:59:56 2020

@author: eliphat
"""
from ..type_system.concepts import Implementation, name_of
base_impls = []


def impl(name, types, result_type, varnames, code, inc=None, inl=True):
    if inc is None:
        inc = tuple()
    if isinstance(inc, str):
        inc = (inc,)
    base_impls.append(Implementation(
        name, types, result_type, varnames, code, inc, inl
    ))


from . import numeric_impl, string_impl, range_impl


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
