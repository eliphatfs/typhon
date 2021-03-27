# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:02:51 2021

@author: eliphat
"""
from ..type_repr import RecordType, BottomType
from .intrinsic_function import WrapperIntrinsic


class PyList(RecordType):
    def __init__(self, U=None):
        self.U = U or BottomType()
        self.members = {
            "append": WrapperIntrinsic(self.append)
        }

    @property
    def name(self):
        return "builtins.list[%s]" % self.U.name

    def append(self, obj_T):
        self.U = self.U | obj_T

    def __eq__(self, other):
        return isinstance(other, PyList) and other.U == self.U

    def __or__(self, other):
        if isinstance(other, PyList):
            return PyList(self.U | other.U)
        return NotImplemented
