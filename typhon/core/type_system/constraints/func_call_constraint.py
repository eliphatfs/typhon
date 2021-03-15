# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:04:35 2021

@author: eliphat
"""
import typing
from ..type_var import TypeVar
from ..type_repr import BottomType, FunctionType
from .base_constraint import BaseConstraint


class FuncCallConstraint(BaseConstraint):
    def __init__(self, func_var: TypeVar, ret_var: TypeVar, args: typing.List[TypeVar]):
        self.F = func_var
        self.R = ret_var
        self.args = args

    def cause_vars(self):
        return [self.F]

    def effect_vars(self):
        return [self.R]

    def fix(self, ts):
        if isinstance(self.F.T, BottomType):
            return
        if isinstance(self.F.T, FunctionType):
            if len(self.F.T.args) != len(self.args):
                raise TypeError(
                    "Function %s requires %d args, got %d"
                    % (self.F, len(self.F.T.args), len(self.args))
                )
            for i, (ao, an) in enumerate(zip(self.F.T.args, self.args)):
                if isinstance(an, BottomType):
                    return
                if ao != an.T:
                    raise TypeError(
                        "Function %s got inconsistent type %s at arg %d"
                        % (self.F, an.T, i)
                    )
            self.R.T = self.F.T.r
            return
        raise TypeError("%s is not a function" % self.F)

    def is_resolved(self):
        return not isinstance(self.R.T, BottomType)
