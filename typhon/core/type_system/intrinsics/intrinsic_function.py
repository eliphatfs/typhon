# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:04:38 2021

@author: eliphat
"""
from ..type_repr import TyphonType, BottomType


class IntrinsicFunction(TyphonType):
    def __init__(self):
        self.name = "<intrinsic @%d>" % id(self)

    def __call__(self, out_type_var, arg_type_vars):
        pass


class WrapperIntrinsic(IntrinsicFunction):
    def __init__(self, type_callable):
        super().__init__()
        self.type_callable = type_callable

    def __call__(self, out_type_var, arg_type_vars):
        out_type_var.T = self.type_callable(*(tv.T for tv in arg_type_vars))


class ArrowCollectionIntrinsic(list, IntrinsicFunction):
    def __init__(self, name, items):
        self.name = name
        list.__init__(self, items)

    def __call__(self, out_type_var, arg_type_vars):
        for arrow in self:
            if len(arrow.args) != len(arg_type_vars):
                continue
            for arg_gt, arg_var in zip(arrow.args, arg_type_vars):
                if arg_gt != arg_var.T:
                    break
            else:
                out_type_var.T = arrow.r
                return
        if not any(isinstance(argv.T, BottomType) for argv in arg_type_vars):
            raise TypeError("Intrinsic type error.", self.name, [v.T.name for v in arg_type_vars])

    def __or__(self, o):
        if isinstance(o, ArrowCollectionIntrinsic):
            return ArrowCollectionIntrinsic(
                [a for a in self if a in o]
            )
        return NotImplemented
