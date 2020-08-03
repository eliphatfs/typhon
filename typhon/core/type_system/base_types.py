# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:49:30 2020

@author: eliphat
"""
from collections import namedtuple


BaseType = namedtuple(
    "BaseType",
    ["c_name", "definition"]
)
PyInt = BaseType("long long", "")
PyFloat = BaseType("double", "")
PyStr = BaseType("char *", "")
PyNone = BaseType("PyNone", """
typedef struct PyNone {
    char placeholder;
} PyNone;
static PyNone _typhon_create_none () { PyNone n; return n; }
""")


def from_const(val):
    if val is None:
        return PyNone
    if type(val) == int:
        return PyInt
    if type(val) == float:
        return PyFloat
    if type(val) == str:
        return PyStr
    raise TypeError("Unsupported Type", type(val))
