# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:46:02 2021

@author: eliphat
"""


class NodeEnv:
    def __init__(self):
        self.bindings = dict()

    def query_name(self, name):
        if name in self.bindings:
            return self.bindings[name]
        raise NameError("Attempting to load unbound name %s" % name)
