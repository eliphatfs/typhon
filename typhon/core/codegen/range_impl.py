# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:53:55 2020

@author: eliphat
"""
from . import impl
from ..type_system.base_types import PyInt, BaseType


PyRange = BaseType("PyRange *", """
typedef struct PyRange {
    int start, stop, step;
} PyRange;
""")
PyRangeIter = BaseType("PyRangeIter *", """
struct PyRange;
typedef struct PyRangeIter {
    struct PyRange * seq;
    int current_idx;
} PyRangeIter;
""")
impl("iter", (PyRange,), PyRangeIter, ("x",), """
    PyRangeIter * iter_obj = malloc(sizeof(PyRangeIter));
    iter_obj->seq = x;
    iter_obj->current_idx = 0;
    return iter_obj;
""", "stdlib.h")
impl("iter", (PyRangeIter,), PyRangeIter, ("x",), """
    return x;
""")
impl("_typhon_iter_is_over", (PyRangeIter,), PyInt, ("x",), """
    long long cur = x->seq->start + x->current_idx * x->seq->step;
    if ((x->seq)->step > 0)
        return cur >= x->seq->stop;
    else
        return cur <= x->seq->stop;
""")
impl("_typhon_iter_step", (PyRangeIter,), PyInt, ("x",), """
    return x->seq->start + (x->current_idx++) * x->seq->step;
""")
impl("range", (PyInt,), PyRange, ("x",), """
    PyRange * result = malloc(sizeof(PyRange));
    result->start = 0; result->stop = x; result->step = 1;
    return result;
""")
impl("range", (PyInt, PyInt), PyRange, ("x", "y"), """
    PyRange * result = malloc(sizeof(PyRange));
    result->start = x; result->stop = y; result->step = 1;
    return result;
""")
impl("range", (PyInt, PyInt, PyInt), PyRange, ("x", "y", "z"), """
    PyRange * result = malloc(sizeof(PyRange));
    result->start = x; result->stop = y; result->step = z;
    return result;
""")
