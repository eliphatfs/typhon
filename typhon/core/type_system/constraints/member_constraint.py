# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:40:01 2021

@author: eliphat
"""
from ..type_var import TypeVar
from ..type_repr import RecordType, BottomType
from .base_constraint import BaseConstraint


class MemberConstraint(BaseConstraint):
    def __init__(self, v_dst: TypeVar, v_src: TypeVar, record_label: str):
        self.dst = v_dst
        self.src = v_src
        self.k = record_label

    def cause_vars(self):
        return [self.src]

    def effect_vars(self):
        return [self.dst]

    def fix(self):
        T = self.src.T
        if isinstance(T, BottomType):
            return
        if isinstance(T, RecordType):
            if self.k in T.members:
                self.dst.T = T.members[self.k]
        raise TypeError("Type %s does not have member %s" % (T, self.k))

    def is_resolved(self):
        ST = self.src.T
        DT = self.dst.T
        return isinstance(ST, RecordType) and DT == ST.members.get(self.k)
