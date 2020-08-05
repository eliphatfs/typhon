# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:01:51 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode


stack_ops = list(map(opcode.opmap.get, [
    "NOP",
    "ROT_TWO",
    "ROT_THREE",
    "DUP_TOP",
    "DUP_TOP_TWO",
    "POP_TOP",
]))


def handle_stack_op(op, stack):
    if op == opcode.opmap.get("NOP"):
        return
    elif op == opcode.opmap.get("POP_TOP"):
        stack.pop().reduce(set())
    elif op == opcode.opmap.get("ROT_TWO"):
        tmp = stack[-1]
        stack[-1] = stack[-2]
        stack[-2] = tmp
    elif op == opcode.opmap.get("ROT_THREE"):
        tmp = stack[-1]
        stack[-1] = stack[-2]
        stack[-2] = stack[-3]
        stack[-3] = tmp
    elif op == opcode.opmap.get("DUP_TOP"):
        stack.append(stack[-1])
    elif op == opcode.opmap.get("DUP_TOP_TWO"):
        stack.append(stack[-2])
        stack.append(stack[-2])
    else:
        raise ValueError("Instruction %d is not an stack operation." % op)


class StackOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = stack_ops
    num_actions = 1

    def apply(self, state, result, action):
        stack = state.stack
        handle_stack_op(self.instr.opcode, stack)
