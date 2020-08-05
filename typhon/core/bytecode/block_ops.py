# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:23:44 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, StaticBlock


class PopBlockOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("POP_BLOCK")]
    num_actions = 1

    def apply(self, state, result, action):
        state.blocks.pop()


class SetupBlockOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("SETUP_LOOP")]
    num_actions = 1

    def apply(self, state, result, action):
        state.blocks.append(StaticBlock(
            self.instr.opcode,
            self.instr.argval,
            list()
        ))
