# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:46:02 2021

@author: eliphat
"""


class NodeEnv:
    def __init__(self, qualname: str, parent):
        self.qualname = qualname
        self.bindings = dict()
        self.children = list()
        if parent is not None:
            parent.children.append(self)
        self.parent = parent

    def query_name(self, name):
        if name in self.bindings:
            return self.bindings[name]
        if self.parent is not None:
            return self.parent.query_name(name)
        else:
            raise NameError("Attempting to load unbound name %s" % name)
