# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:46:02 2021

@author: eliphat
"""
from .type_system.intrinsics import builtin_functions


class NodeEnv:
    def __init__(self, qualname: str, parent):
        self.qualname = qualname
        self.bindings = dict()  # Python names
        self.symbols = dict()  # Let-bound symbol
        self.children = list()
        if parent is not None:
            parent.children.append(self)
        self.parent = parent

    def query_name(self, name):
        if name in self.bindings:
            return self.bindings[name]
        elif self.parent is not None:
            return self.parent.query_name(name)
        else:
            intrinsic = builtin_functions.registry.get(name, NotImplemented)
            if intrinsic is not NotImplemented:
                return intrinsic
        raise NameError("Attempting to load unbound name %s" % name)

    def query_symbol(self, sym):
        return self.symbols[sym]
