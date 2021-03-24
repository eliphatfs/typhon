# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:05:21 2021

@author: eliphat
"""
from .py_bool import py_bool
from ..type_repr import RecordType, FunctionType

py_int = RecordType("builtins.int", {})
py_int.add_function_member("__add__", FunctionType([py_int], py_int))
py_int.add_function_member("__sub__", FunctionType([py_int], py_int))
py_int.add_function_member("__mul__", FunctionType([py_int], py_int))
py_int.add_function_member("__floordiv__", FunctionType([py_int], py_int))
py_int.add_function_member("__mod__", FunctionType([py_int], py_int))
py_int.add_function_member("__lshift__", FunctionType([py_int], py_int))
py_int.add_function_member("__rshift__", FunctionType([py_int], py_int))
py_int.add_function_member("__and__", FunctionType([py_int], py_int))
py_int.add_function_member("__xor__", FunctionType([py_int], py_int))
py_int.add_function_member("__or__", FunctionType([py_int], py_int))
py_int.add_function_member("__neg__", FunctionType([], py_int))
py_int.add_function_member("__bool__", FunctionType([], py_bool))
