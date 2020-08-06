# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:39:55 2020

@author: eliphat
"""
import opcode
from . import Usage, BaseOpcode
from ..type_system import inference


class ReturnValueOpcode(BaseOpcode):
    usage = Usage.General
    opcodes = [opcode.opmap.get("RETURN_VALUE")]
    num_actions = 1

    def apply(self, state, result, action):
        state.stack.pop().reduce(set())


class AnalyzerReturnValueOpcode(ReturnValueOpcode):
    usage = Usage.Analyze

    def apply(self, state, result, action):
        t, _ = state.stack.pop().reduce(set())
        result.return_type = inference.type_merge(result.return_type, t)


class CodeGenReturnValue(ReturnValueOpcode):
    usage = Usage.CodeGen

    def apply(self, state, result, action):
        result.body.append("return "
                           + state.stack.pop().reduce(result.impls)[-1])
