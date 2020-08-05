# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:57:50 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, FuncApply


una_opnames = {
    opcode.opmap.get("UNARY_POSITIVE"): "__pos__",
    opcode.opmap.get("UNARY_NEGATIVE"): "__neg__",
    opcode.opmap.get("UNARY_NOT"): "__not__",
    opcode.opmap.get("UNARY_INVERT"): "__invert__",
    opcode.opmap.get("GET_ITER"): "iter",
}


class UnaryOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = list(una_opnames.keys())
    num_actions = 1

    def apply(self, state, result, action):
        stack = state.stack
        stack.append(FuncApply(una_opnames[self.instr.opcode], (stack.pop(),)))
