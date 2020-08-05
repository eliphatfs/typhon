# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:30:20 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode, Variable


class LoadFastOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("LOAD_FAST")]
    num_actions = 1

    def apply(self, state, result, action):
        variables = result.variables
        stack = state.stack
        instr = self.instr
        if instr.argval not in variables:
            raise ValueError("Variable %s is used before initialization."
                             % instr.argval)
        stack.append(variables[instr.argval])


class StoreFastOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("STORE_FAST")]
    num_actions = 1

    def apply(self, state, result, action):
        instr = self.instr
        v = result.variables.get(instr.argval, Variable(instr.argval))
        state.stack.pop()
        result.variables[instr.argval] = v


class AnalyzeStoreFastOpcode(StoreFastOpcode):
    usage = Usage.Analyze

    def apply(self, state, result, action):
        instr = self.instr
        v = result.variables.get(instr.argval, Variable(instr.argval))
        v.union(state.stack.pop().reduce(set())[0])
        result.variables[instr.argval] = v


class CodeGenStoreFastOpcode(StoreFastOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        func = state.stack.pop()
        result.body.append(self.instr.argval + " = "
                           + func.reduce(result.impls)[-1])
