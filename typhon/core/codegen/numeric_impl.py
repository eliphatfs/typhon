# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:23:46 2020

@author: eliphat
"""
from . import impl
from ..type_system.base_types import PyInt, PyFloat, PyNone, PyStr


def merge_numeric(t1, t2):
    assert {PyInt, PyFloat}.issuperset({t1, t2}), "Non-numeric types"
    if PyFloat in (t1, t2):
        return PyFloat
    return PyInt


bin_ops = {
    "__add__": "+",
    "__sub__": "-",
    "__mul__": "*",

    "__lt__": "<",
    "__le__": "<=",
    "__eq__": "==",
    "__gt__": ">",
    "__ge__": ">=",
}

for name, op in bin_ops.items():
    for fir in (PyInt, PyFloat):
        for sec in (PyInt, PyFloat):
            impl(name, (fir, sec), merge_numeric(fir, sec),
                 ("x", "y"), "return x {op} y;".format(op=op))

int_bin_ops = {
    "__floordiv__": "/",
    "__mod__": "%",
    "__lshift__": "<<",
    "__rshift__": ">>",
    "__and__": "&",
    "__xor__": "^",
    "__or__": "|"
}
for name, op in int_bin_ops.items():
    impl(name, (PyInt, PyInt), PyInt,
         ("x", "y"), "return x {op} y;".format(op=op))

for name, op in bin_ops.items():
    for fir in (PyInt, PyFloat):
        for sec in (PyInt, PyFloat):
            impl("__truediv__", (fir, sec), PyFloat,
                 ("x", "y"), "return (double)x / (double)y;")


for fir in (PyInt, PyFloat):
    for sec in (PyInt, PyFloat):
        if fir == PyInt and sec == PyInt:
            continue
        impl("__mod__", (fir, sec), PyFloat,
             ("x", "y"), "return fmod(x, y);", "math.h")
        impl("__floordiv__", (fir, sec), PyFloat,
             ("x", "y"), "return (x - fmod(x, y)) / y;", "math.h")
        impl("pow", (fir, sec), PyFloat,
             ("x", "y"), "return pow(x, y);", "math.h")
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
impl("pow", (PyInt, PyInt), PyInt, ("base", "exp"), """
    int result = 1;
    while (exp) {
        if (exp % 2) result *= base;
        exp /= 2;
        base *= base;
    }
    return result;
""", inl=False)
impl("pow", (PyInt, PyInt, PyInt), PyInt, ("base", "exp", "modulo"), """
    int result = 1;
    while (exp) {
        if (exp % 2) { result *= base; result %= modulo; }
        exp /= 2;
        base *= base; base %= modulo;
    }
    return result % modulo;
""", inl=False)
