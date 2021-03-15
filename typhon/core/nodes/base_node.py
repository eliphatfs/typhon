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

    def pprint(self, depth=0):
        children = self.children()
        me = "  " * depth + type(self).__name__
        if type(self).__str__ is not object.__str__:
            me += "[" + str(self) + ']'
        lines = [me]
        for child in children:
            lines.append(child.pprint(depth + 1))
        return '\n'.join(lines)

    def __repr__(self):
        return self.pprint()


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
