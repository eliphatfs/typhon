# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:16:23 2020
Simulates the python stack machine.

@author: eliphat
"""
import opcode
import collections
from .type_system import concepts
from .type_system import base_types
from . import codegen


TranslationResult = collections.namedtuple(
    "TranslationResult",
    ["body", "impls", "variables"]
)


class Reduction:

    def reduce(self, impls):
        raise NotImplementedError


class FuncApply(Reduction):

    def __init__(self, name, args=None):
        self.name = name
        self.args = args
        self.impl = None

    def reduce(self, impls):
        if self.args is None:
            raise ValueError("No arguments to reduce")
        red = []
        for arg in self.args:
            if isinstance(arg, Reduction):
                red.append(arg.reduce(impls))
            else:
                raise TypeError("Non-reducible argument")
        interface = concepts.Interface(self.name, tuple(a[0] for a in red))
        self.impl = concepts.find_implementation(codegen.base_impls, interface)
        if self.impl is None:
            raise TypeError("Interface %s is not implemented"
                            % repr(interface))
        impls.add(self.impl)
        return (
            self.impl.result_type,
            (concepts.name_of(self.impl)
             + "(" + ', '.join(a[1] for a in red) + ")")
        )


class Constant(Reduction):

    def __init__(self, val):
        self.val = val

    def reduce(self, impls):
        t = base_types.from_const(self.val)
        if self.val is None:
            return t, "_typhon_create_none()"
        if type(self.val) is str:
            return t, '"' + self.val + '"'
        else:
            return t, str(self.val)


class Variable(Reduction):

    def __init__(self, name):
        self.py_type = None
        self.name = name

    def reduce(self, impls):
        return self.py_type, self.name

    def union(self, type_assigned):
        if self.py_type is None:
            self.py_type = type_assigned
        typeset = set((self.py_type, type_assigned))
        if typeset == {base_types.PyInt, base_types.PyFloat}:
            self.py_type = base_types.PyFloat
        if self.py_type == type_assigned:
            return
        raise ValueError("Multiple types for variable %s" % self.name,
                         "This is not yet implemented.")


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
opcode_opname = dict()
for op, name in operator_names.items():
    opcode_opname[opcode.opmap.get(op)] = name
    # TODO: Needs changing when mutable types come into consideration
    opcode_opname[opcode.opmap.get(op.replace("BINARY", "INPLACE"))] = name


names_comparator = {
    "__lt__": "<",
    "__le__": "<=",
    "__eq__": "==",
    "__gt__": ">",
    "__ge__": ">=",
    "__ne__": "!=",
}
comparator_names = {v: k for k, v in names_comparator.items()}


unconditional_jump_ops = {
    opcode.opmap.get("JUMP_FORWARD"): (lambda x, arg: x + arg),
    opcode.opmap.get("JUMP_ABSOLUTE"): (lambda x, arg: arg)
}
conditional_jump_ops = {
    opcode.opmap.get("POP_JUMP_IF_TRUE"): (lambda x: x),
    opcode.opmap.get("POP_JUMP_IF_FALSE"): (lambda x: "!(%s)" % x)
}

stack_ops = set(map(opcode.opmap.get, [
    "NOP",
    "ROT_TWO",
    "ROT_THREE",
    "DUP_TOP",
    "DUP_TOP_TWO"
]))


def handle_stack_op(op, stack):
    if op == opcode.opmap.get("NOP"):
        return
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


def translate(bc_obj):
    stack = list()
    glo = globals()
    import builtins
    for name in dir(builtins):
        glo[name] = getattr(builtins, name)
    variables = dict()
    impls = set()
    # Two step
    # Step 1: Infer variable types
    for instr in bc_obj:
        if instr.opcode in opcode_opname:
            tos = stack.pop()
            tos1 = stack.pop()
            stack.append(FuncApply(opcode_opname[instr.opcode], (tos1, tos)))
        elif instr.opcode in stack_ops:
            handle_stack_op(instr.opcode, stack)
        elif instr.opcode == opcode.opmap["COMPARE_OP"]:
            if instr.argval not in comparator_names:
                raise ValueError("Comparator %s is not yet supported."
                                 % instr.argval)
            tos = stack.pop()
            tos1 = stack.pop()
            compname = comparator_names[instr.argval]
            stack.append(FuncApply(compname, (tos1, tos)))
        elif instr.opcode in unconditional_jump_ops:
            pass
        elif instr.opcode in conditional_jump_ops:
            if stack.pop().reduce(impls)[0] != base_types.PyInt:
                raise TypeError("Jump condition is not integral." +
                                " __bool__ is not yet supported.")
        elif instr.opcode == opcode.opmap["LOAD_FAST"]:
            if instr.argval not in variables:
                raise ValueError("Variable %s is used before initialization"
                                 % instr.argval)
            stack.append(variables[instr.argval])
        elif instr.opcode == opcode.opmap["STORE_FAST"]:
            v = variables.get(instr.argval, Variable(instr.argval))
            v.union(stack.pop().reduce(impls)[0])
            variables[instr.argval] = v
        elif instr.opcode == opcode.opmap["LOAD_GLOBAL"]:
            obj = glo[instr.argval]
            if callable(obj):
                stack.append(FuncApply(instr.argval))
            else:
                raise ValueError("Globals other than print and input" +
                                 "is not yet supported.")
        elif instr.opcode == opcode.opmap["LOAD_CONST"]:
            stack.append(Constant(instr.argval))
        elif instr.opcode == opcode.opmap["POP_TOP"]:
            stack.pop()
        elif instr.opcode == opcode.opmap["CALL_FUNCTION"]:
            arg = [stack.pop() for _ in range(instr.argval)][::-1]
            if not isinstance(stack[-1], FuncApply):
                raise TypeError(repr(stack[-1]) + " is not callable.")
            stack[-1].args = tuple(arg)
        elif instr.opcode == opcode.opmap["RETURN_VALUE"]:
            stack.pop()
        else:
            print("Warning: Unsupported instruction",
                  instr.opcode, "(%s)" % opcode.opname[instr.opcode])
    assert len(stack) == 0, "Side effects to stack."
    body = list()
    # Step 2: Generate body code
    for instr in bc_obj:
        if instr.is_jump_target:
            body.append("BC_%d:" % instr.offset)
        if instr.opcode in opcode_opname:
            tos = stack.pop()
            tos1 = stack.pop()
            stack.append(FuncApply(opcode_opname[instr.opcode], (tos1, tos)))
        elif instr.opcode in stack_ops:
            handle_stack_op(instr.opcode, stack)
        elif instr.opcode == opcode.opmap["COMPARE_OP"]:
            tos = stack.pop()
            tos1 = stack.pop()
            compname = comparator_names[instr.argval]
            stack.append(FuncApply(compname, (tos1, tos)))
        elif instr.opcode in unconditional_jump_ops:
            applica = unconditional_jump_ops[instr.opcode]
            body.append("goto BC_%d" % applica(instr.offset, instr.argval))
        elif instr.opcode in conditional_jump_ops:
            applica = conditional_jump_ops[instr.opcode]
            cond = applica(stack.pop().reduce(impls)[-1])
            body.append("if (%s) goto BC_%d" % (cond, instr.argval))
        elif instr.opcode == opcode.opmap["LOAD_FAST"]:
            stack.append(variables[instr.argval])
        elif instr.opcode == opcode.opmap["STORE_FAST"]:
            func = stack.pop()
            body.append(instr.argval + " = " + func.reduce(impls)[-1])
        elif instr.opcode == opcode.opmap["LOAD_GLOBAL"]:
            stack.append(FuncApply(instr.argval))
        elif instr.opcode == opcode.opmap["LOAD_CONST"]:
            stack.append(Constant(instr.argval))
        elif instr.opcode == opcode.opmap["POP_TOP"]:
            body.append(stack.pop().reduce(impls)[-1])
        elif instr.opcode == opcode.opmap["CALL_FUNCTION"]:
            arg = [stack.pop() for _ in range(instr.argval)][::-1]
            stack[-1].args = tuple(arg)
        elif instr.opcode == opcode.opmap["RETURN_VALUE"]:
            body.append("return " + stack.pop().reduce(impls)[-1])
    return TranslationResult(body, impls, variables)
