# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:04:35 2021

@author: eliphat
"""
import typing
from ..type_var import TypeVar
from ..type_repr import BottomType, FunctionType, PolymorphicType
from ..intrinsics.intrinsic_function import IntrinsicFunction
from .base_constraint import BaseConstraint
from .subtype_constraint import SubtypeConstraint


class FuncCallConstraint(BaseConstraint):
    def __init__(self, func_var: TypeVar, ret_var: TypeVar, args: typing.List[TypeVar]):
        self.F = func_var
        self.R = ret_var
        self.args = args
        self.recorded_return_union = set()
        self.last_intrinsic = None

    def cause_vars(self):
        return [self.F] + self.args

    def effect_vars(self):
        return [self.R]

    def check_compatible(self, func_type):
        if len(func_type.args) != len(self.args):
            return TypeError(
                "Function %s requires %d args, got %d"
                % (self.F, len(func_type.args), len(self.args))
            )
        for i, (ao, an) in enumerate(zip(func_type.args, self.args)):
            if ao != an.T:
                return TypeError(
                    "Function %s got inconsistent type %s at arg %d"
                    % (self.F, an.T.name, i)
                )
        return True

    def fix(self, ts):
        if isinstance(self.F.T, BottomType):
            return
        for v in self.args:
            if isinstance(v.T, BottomType):
                return
        if isinstance(self.F.T, IntrinsicFunction):
            if self.last_intrinsic is not self.F.T:
                self.last_intrinsic = self.F.T
                self.F.T(self.R, self.args)
            return
        if isinstance(self.F.T, PolymorphicType):
            for f_src in self.F.T.func_srcs:
                inst = f_src.expand_on_args(
                    ts,
                    tuple(map(lambda v: v.T, self.args))
                )
                at_ret_tv = inst.env.bindings["@RET"].TV
                if at_ret_tv not in self.recorded_return_union:
                    ts.add_constraint(SubtypeConstraint(self.R, at_ret_tv))
                    self.recorded_return_union.add(at_ret_tv)
            return
        if isinstance(self.F.T, FunctionType):
            check = self.check_compatible(self.F.T)
            if isinstance(check, Exception):
                raise check
            self.R.T = self.F.T.r
            return
        raise TypeError("%s is not a function" % self.F)

    def is_resolved(self):
        # TODO: Not quite correct?
        return not isinstance(self.R.T, BottomType)
