# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:41:23 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, FuncApply
from ..type_system import base_types


class ForIterOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("FOR_ITER")]
    num_actions = 1

    def apply(self, state, result, action):
        # This is not what exactly python does.
        # Modified for a stack balance check.
        stack = state.stack
        stack.append(FuncApply("_typhon_iter_step", (stack.pop(),)))


class BreakLoopOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("BREAK_LOOP")]
    num_actions = 1

    def apply(self, state, result, action):
        assert state.blocks[-1].opcode == opcode.opmap.get("SETUP_LOOP")


class CodeGenForOpcode(ForIterOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        it = state.stack.pop()
        state.stack.append(FuncApply("_typhon_iter_step", (it,)))
        t, expr = FuncApply("_typhon_iter_is_over", (it,)).reduce(result.impls)
        if t != base_types.PyInt:
            raise TypeError("Iteration end condition should be boolean type.")
        result.body.append("if (%s) goto BC_%d;" % (expr, self.instr.argval))


class CodeGenBreakOpcode(BreakLoopOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        result.body.append("goto BC_%d" % state.blocks[-1].end)
