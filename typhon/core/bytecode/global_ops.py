# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:34:52 2020

@author: eliphat
"""
import sys
import opcode
from . import Usage, BaseOpcode, FuncApply


class LoadGlobalOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("LOAD_GLOBAL")]
    num_actions = 1

    def apply(self, state, result, action):
        import builtins
        instr = self.instr
        if not hasattr(builtins, instr.argval):
            obj = getattr(sys.modules['__main__'], instr.argval)
            if callable(obj):
                return state.stack.append(FuncApply(instr.argval))
            else:
                raise ValueError("Globals other than functions" +
                                 "are not yet supported.")
        obj = getattr(builtins, instr.argval)
        if callable(obj):
            state.stack.append(FuncApply(instr.argval))
        else:
            raise ValueError("Globals other than functions" +
                             "are not yet supported.")
