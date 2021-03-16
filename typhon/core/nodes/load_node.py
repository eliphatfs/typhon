# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:00:54 2021

@author: eliphat
"""
from .base_node import ExprNode


class LoadNode(ExprNode):
    def __init__(self, env, local_name):
        super().__init__(env)
        self.local_name = local_name

    def value_type_var(self):
        return self.env.query_name(self.local_name).TV

    def __str__(self):
        return "Variable %s" % self.local_name
