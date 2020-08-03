# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:52:31 2020

@author: eliphat
"""
from collections import namedtuple


Interface = namedtuple(
    "Interface",
    ["name", "types"]
)

Implementation = namedtuple(
    "Implementation",
    ["name", "types", "result_type", "varnames", "code", "include", "inline"]
)


def name_of(imp):
    return imp.name + "_" + str(abs(hash(imp)))


def find_implementation(collection, interface):
    for imp in collection:
        if imp.name == interface.name and imp.types == interface.types:
            return imp
    return None
