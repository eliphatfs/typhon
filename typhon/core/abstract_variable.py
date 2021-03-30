# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:44:25 2021

@author: eliphat
"""


class AbstractVariable:
    def __init__(self, type_var, name, func_binding=None):
        self.name = name  # local name
        self.TV = type_var
        self.func_binding = func_binding
