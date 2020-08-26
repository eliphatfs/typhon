# -*- coding: utf-8 -*-
"""
A very simple IR.
Created on Thu Aug  6 13:12:53 2020

@author: eliphat
"""


class Reduction:
    pass


class Func(Reduction):

    def __init__(self, name):
        self.name = name
        self.args = []
        self.is_value = False

    def curry(self, arg):
        if self.is_value:
            raise TypeError("Value cannot be curried. (%s)" % self.name)
        f = Func(self.name)
        f.args = self.args + [arg]
        return f

    def apply(self, args=None):
        if args is None:
            args = []
        f = Func(self.name)
        f.args = self.args + args
        f.is_value = True
        return f


class Constant(Reduction):

    def __init__(self, val):
        self.val = val


class Variable(Reduction):

    def __init__(self, name):
        self.name = name


class Store(Reduction):

    def __init__(self, v, expr):
        self.v = v
        self.expr = expr


class Return(Reduction):

    def __init__(self, expr):
        self.expr = expr


class ConditionalJump(Reduction):

    def __init__(self, cond, target_block):
        """
        if (cond) goto block
        """
        self.cond = cond
        self.target_block = target_block


class UnconditionalJump(Reduction):

    def __init__(self, target_block):
        self.target_block = target_block


class BasicBlock:

    def __init__(self, name):
        self.name = name
        self.body = []

    def add(self, red):
        self.body.append(red)
        return red

    def __iter__(self):
        return iter(self.body)
