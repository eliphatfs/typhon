# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:36:04 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, Constant


class LoadConstOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("LOAD_CONST")]
    num_actions = 1

    def apply(self, state, result, action):
        state.stack.append(Constant(self.instr.argval))
