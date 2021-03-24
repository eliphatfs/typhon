# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:35:15 2021

@author: eliphat
"""
class TyphonType:
    def __init__(self):
        self.name = "<undefined type>"


class BottomType(TyphonType):
    def __init__(self):
        self.name = "Bottom"

    def __or__(self, other):
        return other

    def __ror__(self, other):
        return other

    def __eq__(self, other):
        return isinstance(other, BottomType)


class FunctionType(TyphonType):
    def __init__(self, arg_types, return_type):
        self.r = return_type
        self.args = arg_types

    @property
    def name(self):
        return "(" + ', '.join(x.name for x in self.args) + ") -> " + self.r.name

    def __eq__(self, other):
        if isinstance(other, FunctionType):
            if self.r == other.r:
                if all(L == R for L, R in zip(self.args, other.args)):
                    return True
        return False

    def __or__(self, other):
        if self == other:
            return self
        elif isinstance(other, FunctionType):
            raise TypeError("Union between '->' types are not yet supported. " + 
                            "Called on: %s and %s"
                            % (self.name, other.name))
        return NotImplemented


class RecordType(TyphonType):
    def __init__(self, qualified_name, member_dict):
        self.members = member_dict
        self.name = qualified_name
        # Every record type should be decided by its qualified name
        # Is this true?

    def add_function_member(self, name, func):
        self.members[name] = func

    def __eq__(self, other):
        if isinstance(other, RecordType):
            return self.name == other.name
        return False

    def __or__(self, other):
        if self == other:
            return self
        elif isinstance(other, RecordType):
            raise TypeError("Union between records are not yet supported. " +
                            "Called on: %s and %s"
                            % (self.name, other.name))
        return NotImplemented


class PolymorphicType(TyphonType):
    def __init__(self, name, func_srcs):
        self.name = name
        self.func_srcs = set()

    def __eq__(self, other):
        return isinstance(other, PolymorphicType) and other.func_srcs == self.func_srcs

    def __or__(self, other):
        if self == other:
            return self
        elif isinstance(other, PolymorphicType):
            return PolymorphicType(
                self.name + " | " + other.name,
                self.func_srcs | other.func_srcs
            )
        return NotImplemented
