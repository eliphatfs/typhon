# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:47:28 2020

@author: eliphat
"""
import dis


def some_arguments(a, b):
    return (a + b, a - b)


def complicated_constants():
    a = 1
    b = "12"
    c = ("1", 12)
    d = (1+12j, 1+12j)
    return a, b, c, d


def frozen_sets():
    return frozenset(), frozenset((1, 2))


dis.show_code(some_arguments.__code__)
dis.dis(some_arguments.__code__)

dis.show_code(complicated_constants.__code__)
dis.dis(complicated_constants.__code__)

dis.show_code(frozen_sets.__code__)
dis.dis(frozen_sets.__code__)
