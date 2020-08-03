# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:23:46 2020

@author: eliphat
"""
from . import impl
from ..type_system.base_types import PyInt, PyFloat, PyNone, PyStr


impl("__add__", (PyInt, PyInt), PyInt, ("x", "y"), "return x + y;")
impl("__add__", (PyInt, PyFloat), PyFloat, ("x", "y"), "return x + y;")
impl("__add__", (PyFloat, PyInt), PyFloat, ("x", "y"), "return x + y;")
impl("__add__", (PyFloat, PyFloat), PyFloat, ("x", "y"), "return x + y;")


impl("print", (PyInt,), PyNone, ("x",), 'printf("%lld\\n", x);', "stdio.h")
impl("print", (PyFloat,), PyNone, ("x",), 'printf("%lf\\n", x);', "stdio.h")
impl("int", (PyStr,), PyInt, ("x",), """
    long long result;
    sscanf(x, "%lld", &result);
    return result;
""", "stdio.h", inl=False)
impl("float", (PyStr,), PyFloat, ("x",), """
    double result;
    sscanf(x, "%lf", &result);
    return result;
""", "stdio.h", inl=False)
