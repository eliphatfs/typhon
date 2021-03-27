# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:30:17 2021

@author: eliphat
"""
from .base_node import ExprNode


class SymbolNode(ExprNode):
    def __init__(self, env, symbol):
        super().__init__(env)
        self.symbol = symbol

    def value_type_var(self):
        return self.env.query_symbol(self.symbol)
