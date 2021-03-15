# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:13:08 2021

@author: eliphat
"""
class BaseNode:
    def __init__(self, env):
        self.env = env

    def children(self):
        return []

    def typing(self, type_system):
        pass


class StmtNode(BaseNode):
    pass


class ExprNode(BaseNode):
    def value_type_var(self):
        raise NotImplementedError()


class DeterminedValue:
    def __init__(self, type_var, val):
        self.v = val
        self.TV = type_var


class AbstractVariable:
    def __init__(self, type_var, name):
        self.name = name  # local name
        self.TV = type_var


class PolymorphicFunction:
    def __init__(self, root_node, qualified_name):
        self.name = qualified_name
        self.root = root_node
        self.instances = []
