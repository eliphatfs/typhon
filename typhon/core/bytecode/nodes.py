# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:33:06 2020

@author: eliphat
"""
import opcode


operator_names = {
    "BINARY_ADD": "__add__",
    "BINARY_POWER": "pow",
    "BINARY_MULTIPLY": "__mul__",
    "BINARY_SUBTRACT": "__sub__",
    "BINARY_FLOOR_DIVIDE": "__floordiv__",
    "BINARY_TRUE_DIVIDE": "__truediv__",
    "BINARY_MATRIX_MULTIPLY": "__matmul__",
    "BINARY_MODULO": "__mod__",

    "BINARY_LSHIFT": "__lshift__",
    "BINARY_RSHIFT": "__rshift__",
    "BINARY_XOR": "__xor__",
    "BINARY_AND": "__and__",
    "BINARY_OR": "__or__",
}
bin_opnames = dict()
for op, name in operator_names.items():
    bin_opnames[opcode.opmap.get(op)] = name
    # TODO: Needs changing when mutable types come into consideration
    bin_opnames[opcode.opmap.get(op.replace("BINARY", "INPLACE"))] = name

una_opnames = {
    opcode.opmap.get("UNARY_POSITIVE"): "__pos__",
    opcode.opmap.get("UNARY_NEGATIVE"): "__neg__",
    opcode.opmap.get("UNARY_NOT"): "__not__",
    opcode.opmap.get("UNARY_INVERT"): "__invert__",
    opcode.opmap.get("GET_ITER"): "iter",
}

stack_ops = set(map(opcode.opmap.get, [
    "NOP",
    "ROT_TWO",
    "ROT_THREE",
    "DUP_TOP",
    "DUP_TOP_TWO",
    "POP_TOP",
]))

names_comparator = {
    "__lt__": "<",
    "__le__": "<=",
    "__eq__": "==",
    "__gt__": ">",
    "__ge__": ">=",
    "__ne__": "!=",
}
comparator_names = {v: k for k, v in names_comparator.items()}


class Node:

    def __init__(self, instr):
        self.instr = instr
        self.prevs = list()
        self.nexts = list()


class NodeNoJump(Node):
    pass


class BinaryOpNode(NodeNoJump):

    def __init__(self, instr):
        super().__init__(instr)
        self.op = bin_opnames[self.instr.opcode]


class UnaryOpNode(NodeNoJump):

    def __init__(self, instr):
        super().__init__(instr)
        self.op = una_opnames[self.instr.opcode]


class StackOpNode(NodeNoJump):

    def handle_stack_op(self, stack):
        op = self.instr.opcode
        if op == opcode.opmap.get("NOP"):
            return
        elif op == opcode.opmap.get("POP_TOP"):
            stack.pop()
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


class ForSwitchNode(Node):
    pass


class ForIterEndNode(Node):
    pass


class ForIterNextNode(NodeNoJump):
    pass


class PopBlockNode(NodeNoJump):
    pass


class SetupBlockNode(NodeNoJump):
    pass


class CallFunctionNode(NodeNoJump):
    pass


class LoadGlobalNode(NodeNoJump):
    pass


class CompareNode(NodeNoJump):

    def __init__(self, instr):
        super().__init__(instr)
        self.op = comparator_names[self.instr.argval]


class LoadConstNode(NodeNoJump):
    pass


class LoadFastNode(NodeNoJump):
    pass


class StoreFastNode(NodeNoJump):
    pass


class UnconditionalJumpNode(Node):
    pass


class ConditionalJumpNode(Node):

    def __init__(self, instr):
        super().__init__(instr)
        if instr.opcode == opcode.opmap.get("POP_JUMP_IF_FALSE"):
            self.needs_inverting = True
        else:
            self.needs_inverting = False


class ReturnNode(Node):
    pass
