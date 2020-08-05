# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:16:23 2020
Simulates the python stack machine.

@author: eliphat
"""
import opcode
import collections
from .type_system import base_types
from . import bytecode


TranslationResult = collections.namedtuple(
    "TranslationResult",
    ["body", "impls", "variables"]
)


class StackMachineState:

    def __init__(self):
        self.blocks = [bytecode.StaticBlock(-1, -1, list())]

    @property
    def stack(self):
        return self.blocks[-1].stack


class StackMachine:
    usage = bytecode.Usage.General

    def __init__(self, bc):
        self.state = StackMachineState()
        self.result = TranslationResult(list(), set(), dict())
        ctors = bytecode.get_constructors(self.usage)
        self.ops = list()
        for instr in bc:
            ctor = ctors.get(instr.opcode)
            if ctor is None:
                print("Warning: Unsupported instruction",
                      instr.opcode, "(%s)" % opcode.opname[instr.opcode])
            else:
                self.ops.append(ctor(instr))

    def run(self):
        for op in self.ops:
            op.apply(self.state, self.result, 0)


class Analyzer(StackMachine):
    usage = bytecode.Usage.Analyze


class CodeGenerator(StackMachine):
    usage = bytecode.Usage.CodeGen

    def __init__(self, bc, variables):
        super().__init__(bc)
        self.result = TranslationResult(list(), set(), variables)
        self.stack_var_id = 0

    def run(self):
        for op in self.ops:
            if op.instr.is_jump_target:
                self.result.body.append("BC_%d:" % op.instr.offset)
            op.apply(self.state, self.result, 0)
            if len(self.state.stack) == 0:
                continue
            if isinstance(self.state.stack[-1], bytecode.FuncApply):
                if self.state.stack[-1].args is not None:
                    self.replace_top_with_temp_variable()

    def allocate_stack_var(self):
        self.stack_var_id += 1
        return "__stack_" + str(self.stack_var_id)

    def replace_top_with_temp_variable(self):
        t, expr = self.state.stack[-1].reduce(self.result.impls)
        tv = bytecode.TempVar(t, self.allocate_stack_var(), expr)  # FIXME
        self.result.body.append(t.c_name + " " + tv.name + " = " + expr)
        self.state.stack[-1] = tv


def translate(bc_obj):
    # Two step
    # Step 1: Infer variable types
    analyzer = Analyzer(bc_obj)
    analyzer.run()
    assert len(analyzer.state.stack) == 0, "Side effects to stack."
    assert len(analyzer.state.blocks) == 1, "Side effects to static blocks."
    generator = CodeGenerator(bc_obj, analyzer.result.variables)
    # Step 2: Generate body code
    generator.run()
    return generator.result
