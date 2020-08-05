# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:34:52 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, FuncApply


class LoadGlobalOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("LOAD_GLOBAL")]
    num_actions = 1

    def apply(self, state, result, action):
        import builtins
        instr = self.instr
        obj = getattr(builtins, instr.argval)
        if callable(obj):
            state.stack.append(FuncApply(instr.argval))
        else:
            raise ValueError("Globals other than builtin functions" +
                             "are not yet supported.")
