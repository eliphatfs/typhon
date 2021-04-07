# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:02:51 2021

@author: eliphat
"""
from ..type_repr import RecordType, BottomType
from .intrinsic_function import WrapperIntrinsic
from .py_numerics import py_int
from .py_none import py_none
from .py_iter import PyIter


class PyList(RecordType):
    def __init__(self, U=None):
        self._u = U or BottomType()
        self._it = PyIter(self._u)
        self.members = {
            "append": WrapperIntrinsic(self.append),
            "__getitem__": WrapperIntrinsic(self.get_item),
            "__setitem__": WrapperIntrinsic(self.set_item),
            "__iter__": WrapperIntrinsic(self.iterator),
        }

    @property
    def U(self):
        return self._u

    @U.setter
    def U(self, nu):
        if self._u == nu:
            return
        self._u = nu
        self._it = PyIter(nu)

    @property
    def name(self):
        return "builtins.list[%s]" % self.U.name

    def append(self, obj_T):
        self.U = self.U | obj_T
        return py_none

    def get_item(self, index_T):
        if index_T != py_int:
            raise TypeError("List index should be of integral type.")
        return self.U

    def set_item(self, index_T, obj_T):
        if index_T != py_int:
            raise TypeError("List index should be of integral type.")
        self.U = self.U | obj_T
        return py_none

    def iterator(self):
        return self._it

    def __eq__(self, other):
        return isinstance(other, PyList) and other.U == self.U

    def __or__(self, other):
        if self == other:
            return self
        return NotImplemented
