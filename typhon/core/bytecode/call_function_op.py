# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:37:55 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode


class CallFunctionOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("CALL_FUNCTION")]
    num_actions = 1

    def apply(self, state, result, action):
        arg = [state.stack.pop() for _ in range(self.instr.argval)][::-1]
        state.stack[-1].args = tuple(arg)
