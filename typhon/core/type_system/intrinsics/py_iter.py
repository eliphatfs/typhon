# -*- coding: utf-8 -*-
from ..type_repr import RecordType, BottomType
from .intrinsic_function import WrapperIntrinsic


class PyIter(RecordType):
    def __init__(self, U=None):
        self.U = U or BottomType()
        self.members = {
            "__iter__": WrapperIntrinsic(lambda: self),
            "__next__": WrapperIntrinsic(self.next_item)
        }

    @property
    def name(self):
        return "builtins.iter[%s]" % self.U.name

    def next_item(self):
        return self.U

    def __eq__(self, other):
        return isinstance(other, PyIter) and other.U == self.U

    def __or__(self, other):
        if isinstance(other, PyIter):
            return PyIter(self.U | other.U)
        return NotImplemented