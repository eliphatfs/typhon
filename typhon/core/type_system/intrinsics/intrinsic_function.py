# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:04:38 2021

@author: eliphat
"""
from ..type_repr import TyphonType, BottomType


class IntrinsicFunction(TyphonType):
    def __init__(self):
        self.name = "<intrinsic @%d>" % id(self)

    def __call__(self, out_type_var, *arg_type_vars):
        pass


class ArrowTypeCollectionIntrinsicFunction(list, IntrinsicFunction):
    def __call__(self, out_type_var, *arg_type_vars):
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
            raise TypeError("Intrinsic type error.")
            # TODO: meaningful error message

    def __or__(self, o):
        if isinstance(o, ArrowTypeCollectionIntrinsicFunction):
            return ArrowTypeCollectionIntrinsicFunction(
                [a for a in self if a in o]
            )
        return NotImplemented
