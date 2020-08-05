# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:07:31 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode
from ..type_system import base_types


unconditional_jump_ops = {
    opcode.opmap.get("JUMP_FORWARD"): (lambda x, arg: x + arg),
    opcode.opmap.get("JUMP_ABSOLUTE"): (lambda x, arg: arg),
    opcode.opmap.get("CONTINUE_LOOP"): (lambda x, arg: arg),
}
conditional_jump_ops = {
    opcode.opmap.get("POP_JUMP_IF_TRUE"): (lambda x: x),
    opcode.opmap.get("POP_JUMP_IF_FALSE"): (lambda x: "!(%s)" % x)
}


class UnconditionalJumpOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = list(unconditional_jump_ops.keys())
    num_actions = 1


class ConditionalJumpOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = list(conditional_jump_ops.keys())
    num_actions = 1

    def apply(self, state, result, action):
        state.stack.pop()


class AnalyzeConditionalJump(ConditionalJumpOpcode):
    usage = Usage.Analyze

    def apply(self, state, result, action):
        if state.stack.pop().reduce(set())[0] != base_types.PyInt:
            raise TypeError("Jump condition is not integral." +
                            " __bool__ is not yet supported.")


class CodeGenConditionalJumpOpcode(ConditionalJumpOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        instr = self.instr
        applica = conditional_jump_ops[instr.opcode]
        cond = applica(state.stack.pop().reduce(result.impls)[-1])
        result.body.append("if (%s) goto BC_%d" % (cond, instr.argval))


class CodeGenUnconditionalJumpOpcode(UnconditionalJumpOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        result.body.append("goto BC_%d" % self.instr.argval)
