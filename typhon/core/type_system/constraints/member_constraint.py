# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:40:01 2021

@author: eliphat
"""
from ..type_var import TypeVar
from ..type_repr import RecordType, BottomType
from ..system import TypeSystem
from .base_constraint import BaseConstraint
from .equality_constraint import EqualityConstraint


class MemberConstraint(BaseConstraint):
    def __init__(self, v_dst: TypeVar, v_src: TypeVar, record_label: str):
        self.dst = v_dst
        self.src = v_src
        self.k = record_label

    def cause_vars(self):
        return [self.src]

    def effect_vars(self):
        return [self.dst]

    def fix(self, ts: TypeSystem):
        T = self.src.T
        if isinstance(T, BottomType):
            return
        if isinstance(T, RecordType):
            if self.k in T.members:
                rec = T.members[self.k]
                if isinstance(rec, TypeVar):
                    ts.add_constraint(EqualityConstraint(self.dst, rec))
                else:
                    self.dst.T = rec
                return
        raise TypeError("Type %s does not have member %s" % (T, self.k))

    def is_resolved(self):
        return isinstance(self.src.T, RecordType)
