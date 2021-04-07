# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:59:17 2021

@author: eliphat
"""
from . import add_intrinsic
from .special_method_proxy import SpecialMethodProxy
from ..intrinsic_function import WrapperIntrinsic, IntrinsicFunction
from ..py_list import PyList
from ..py_bool import py_bool


add_intrinsic("list", WrapperIntrinsic(lambda: PyList()))


class BoolIntrinsic(IntrinsicFunction):
    def __call__(self, out_type_var, arg_type_vars):
        if len(arg_type_vars) >= 2:
            raise TypeError("bool expected at most 1 argument")
        out_type_var.T = py_bool


class IterIntrinsic(SpecialMethodProxy):
    def __init__(self):
        super().__init__("iter(obj)", "__iter__")

    def __call__(self, out_type_var, arg_type_vars):
        if len(arg_type_vars) == 2:
            raise NotImplementedError(
                "iter(callable, sentinel) overload is not supported yet."
            )
        if len(arg_type_vars) > 2:
            raise TypeError("iter expected at most 2 arguments")
        return super().__call__(out_type_var, arg_type_vars)


add_intrinsic("bool", BoolIntrinsic())
add_intrinsic("iter", IterIntrinsic())
