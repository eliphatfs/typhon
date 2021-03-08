# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:35:15 2021

@author: eliphat
"""
class TyphonType:
    pass


class BottomType(TyphonType):
    def __init__(self):
        self.name = "Bottom"

    def __or__(self, other):
        return other

    def __ror__(self, other):
        return other


class FunctionType(TyphonType):
    def __init__(self, arg_types, return_type, name=None):
        self.r = return_type
        self.args = arg_types
        self.name = name or "<anonymous type %d>" % id(self)


class TypeRecord(TyphonType):
    def __init__(self, qualified_name, member_dict):
        self.members = member_dict
        self.name = qualified_name
        # Every record type should be decided by its qualified name

    def add_function_member(self, name, func):
        self.members[name] = func

    def __or__(self, other):
        if isinstance(other, TypeRecord):
            if self.name == other.name:
                return self
        return NotImplemented
