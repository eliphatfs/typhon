# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:11:24 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, FuncApply


operator_names = {
    "BINARY_ADD": "__add__",
    "BINARY_POWER": "pow",
    "BINARY_MULTIPLY": "__mul__",
    "BINARY_SUBTRACT": "__sub__",
    "BINARY_FLOOR_DIVIDE": "__floordiv__",
    "BINARY_TRUE_DIVIDE": "__truediv__",
    "BINARY_MATRIX_MULTIPLY": "__matmul__",
    "BINARY_MODULO": "__mod__",

    "BINARY_LSHIFT": "__lshift__",
    "BINARY_RSHIFT": "__rshift__",
    "BINARY_XOR": "__xor__",
    "BINARY_AND": "__and__",
    "BINARY_OR": "__or__",
}
bin_opnames = dict()
for op, name in operator_names.items():
    bin_opnames[opcode.opmap.get(op)] = name
    # TODO: Needs changing when mutable types come into consideration
    bin_opnames[opcode.opmap.get(op.replace("BINARY", "INPLACE"))] = name


class BinaryOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = list(bin_opnames.keys())
    num_actions = 1

    def apply(self, state, result, action):
        stack = state.stack
        tos = stack.pop()
        tos1 = stack.pop()
        stack.append(FuncApply(bin_opnames[self.instr.opcode], (tos1, tos)))


names_comparator = {
    "__lt__": "<",
    "__le__": "<=",
    "__eq__": "==",
    "__gt__": ">",
    "__ge__": ">=",
    "__ne__": "!=",
}
comparator_names = {v: k for k, v in names_comparator.items()}


class ComparatorOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("COMPARE_OP")]
    num_actions = 1

    def apply(self, state, result, action):
        instr = self.instr
        if instr.argval not in comparator_names:
            raise ValueError("'%s' is not yet supported." % instr.argval)
        stack = state.stack
        tos = stack.pop()
        tos1 = stack.pop()
        compname = comparator_names[instr.argval]
        stack.append(FuncApply(compname, (tos1, tos)))
