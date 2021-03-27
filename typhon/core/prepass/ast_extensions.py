# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:47:06 2021

@author: eliphat
"""
import ast


class Symbol(ast.expr):
    pass


class LetBinding(ast.expr):
    _fields = ("symbol", "bound_expr", "inner")
