# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:38:24 2020

@author: eliphat
"""
import enum
import collections
from .representations import Reduction, FuncApply, Constant, Variable, TempVar


StaticBlock = collections.namedtuple(
    "StaticBlock",
    ["opcode", "end", "stack"]
)


class Usage(enum.IntEnum):
    General = 0
    CodeGen = 1
    Analyze = 2


class BaseOpcode:
    usage = Usage.General
    opcodes = []
    num_actions = 0

    def __init__(self, instr):
        self.instr = instr

    def apply(self, state, result, action):
        pass


from . import binary_ops, block_ops
from . import call_function_op
from . import global_ops
from . import jump_ops
from . import load_const_op, local_var_ops, loop_ops
from . import return_val_op
from . import stack_ops
from . import unary_ops


def subclasses(t):
    direct = set(t.__subclasses__())
    indirect = set()
    for sub in direct:
        indirect.update(subclasses(sub))
    return direct.union(indirect)


def get_constructors(usage):
    total = subclasses(BaseOpcode)
    mapping = dict()
    for sub in total:
        for op in sub.opcodes:
            mapping[op] = None
    for sub in total:
        if sub.usage == usage:
            for op in sub.opcodes:
                if mapping[op] is not None:
                    raise TypeError("Multiple Handlers for Op %d of %s"
                                    % (op, str(usage)))
                mapping[op] = sub
    for sub in total:
        if sub.usage == Usage.General:
            for op in sub.opcodes:
                if mapping[op] is None:
                    mapping[op] = sub
    return mapping
