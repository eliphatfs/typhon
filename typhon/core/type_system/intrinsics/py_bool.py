# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:11:47 2021

@author: eliphat
"""
from ..type_repr import RecordType, FunctionType


py_bool = RecordType("builtins.bool", {})
py_bool.add_function_member("__bool__", FunctionType([], py_bool))
