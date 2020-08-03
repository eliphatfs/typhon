# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:16:23 2020
Simulates the python stack machine.

@author: eliphat
"""
import opcode
import collections
import builtins
from .type_system import concepts
from .type_system import base_types
from . import codegen


TranslationResult = collections.namedtuple(
    "TranslationResult",
    ["body", "impls", "variables"]
)


class Reduction:

    def reduce(self, impls):
        raise NotImplementedError


class FuncApply(Reduction):

    def __init__(self, name, args=None):
        self.name = name
        self.args = args
        self.impl = None

    def reduce(self, impls):
        if self.args is None:
            raise ValueError("No arguments to reduce")
        red = []
        for arg in self.args:
            if isinstance(arg, Reduction):
                red.append(arg.reduce(impls))
            else:
                raise TypeError("Non-reducible argument")
        interface = concepts.Interface(self.name, tuple(a[0] for a in red))
        self.impl = concepts.find_implementation(codegen.base_impls, interface)
        if self.impl is None:
            raise TypeError("Interface %s is not implemented"
                            % repr(interface))
        impls.add(self.impl)
        return (
            self.impl.result_type,
            (concepts.name_of(self.impl)
             + "(" + ', '.join(a[1] for a in red) + ")")
        )


class Constant(Reduction):

    def __init__(self, val):
        self.val = val

    def reduce(self, impls):
        t = base_types.from_const(self.val)
        if self.val is None:
            return t, "_typhon_create_none()"
        if type(self.val) is str:
            return t, '"' + self.val + '"'
        else:
            return t, str(self.val)


class Variable(Reduction):

    def __init__(self, name):
        self.py_type = None
        self.name = name

    def reduce(self, impls):
        return self.py_type, self.name

    def union(self, type_assigned):
        if self.py_type is None:
            self.py_type = type_assigned
        typeset = set((self.py_type, type_assigned))
        if typeset == {base_types.PyInt, base_types.PyFloat}:
            self.py_type = base_types.PyFloat
        if self.py_type == type_assigned:
            return
        raise ValueError("Multiple types for variable %s" % self.name,
                         "This is not yet implemented.")


def translate(bc_obj):
    stack = list()
    glo = globals()
    for name in dir(builtins):
        glo[name] = getattr(builtins, name)
    variables = dict()
    impls = set()
    # Two step
    # Step 1: Infer variable types
    for instr in bc_obj:
        if instr.opcode == opcode.opmap["BINARY_ADD"]:
            tos = stack.pop()
            tos1 = stack.pop()
            stack.append(FuncApply("__add__", (tos1, tos)))
        if instr.opcode == opcode.opmap["LOAD_FAST"]:
            if instr.argval not in variables:
                raise ValueError("Variable %s is used before initialization"
                                 % instr.argval)
            stack.append(variables[instr.argval])
        if instr.opcode == opcode.opmap["STORE_FAST"]:
            v = variables.get(instr.argval, Variable(instr.argval))
            v.union(stack.pop().reduce(impls)[0])
            variables[instr.argval] = v
        if instr.opcode == opcode.opmap["LOAD_GLOBAL"]:
            obj = glo[instr.argval]
            if callable(obj):
                stack.append(FuncApply(instr.argval))
            else:
                raise ValueError("Globals other than print and input" +
                                 "is not yet supported.")
        if instr.opcode == opcode.opmap["LOAD_CONST"]:
            stack.append(Constant(instr.argval))
        if instr.opcode == opcode.opmap["POP_TOP"]:
            stack.pop()
        if instr.opcode == opcode.opmap["CALL_FUNCTION"]:
            arg = [stack.pop() for _ in range(instr.argval)][::-1]
            if not isinstance(stack[-1], FuncApply):
                raise TypeError(repr(stack[-1]) + " is not callable.")
            stack[-1].args = tuple(arg)
        if instr.opcode == opcode.opmap["RETURN_VALUE"]:
            stack.pop()
    assert len(stack) == 0, "Side effects to stack."
    body = list()
    # Step 2: Generate body code
    for instr in bc_obj:
        if instr.opcode == opcode.opmap["BINARY_ADD"]:
            tos = stack.pop()
            tos1 = stack.pop()
            stack.append(FuncApply("__add__", (tos1, tos)))
        if instr.opcode == opcode.opmap["LOAD_FAST"]:
            stack.append(variables[instr.argval])
        if instr.opcode == opcode.opmap["STORE_FAST"]:
            func = stack.pop()
            body.append(instr.argval + " = " + func.reduce(impls)[-1])
        if instr.opcode == opcode.opmap["LOAD_GLOBAL"]:
            stack.append(FuncApply(instr.argval))
        if instr.opcode == opcode.opmap["LOAD_CONST"]:
            stack.append(Constant(instr.argval))
        if instr.opcode == opcode.opmap["POP_TOP"]:
            body.append(stack.pop().reduce(impls)[-1])
        if instr.opcode == opcode.opmap["CALL_FUNCTION"]:
            arg = [stack.pop() for _ in range(instr.argval)][::-1]
            stack[-1].args = tuple(arg)
        if instr.opcode == opcode.opmap["RETURN_VALUE"]:
            body.append("return " + stack.pop().reduce(impls)[-1])
    return TranslationResult(body, impls, variables)
