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

StaticBlock = collections.namedtuple(
    "StaticBlock",
    ["opcode", "end"]
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
            raise ValueError("No arguments to reduce.")
        red = []
        for arg in self.args:
            if isinstance(arg, Reduction):
                red.append(arg.reduce(impls))
            else:
                raise TypeError("Non-reducible argument.")
        interface = concepts.Interface(self.name, tuple(a[0] for a in red))
        self.impl = concepts.find_implementation(codegen.base_impls, interface)
        if self.impl is None:
            raise TypeError("Interface %s is not implemented."
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
        raise ValueError("Multiple types for variable %s." % self.name +
                         " This is not yet implemented.")


class TempVar(Reduction):

    def __init__(self, py_type, name):
        self.py_type = py_type
        self.name = name

    def reduce(self, impls):
        return self.py_type, self.name


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
    opcode.opmap.get("JUMP_ABSOLUTE"): (lambda x, arg: arg),
    opcode.opmap.get("CONTINUE_LOOP"): (lambda x, arg: arg),
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


class StackMachine:

    def __init__(self):
        self.stack = list()
        self.blocks = list()
        self.variables = dict()
        name_visitors = {
            "COMPARE_OP": self.visit_comparator_op,
            "LOAD_FAST": self.visit_load_fast,
            "STORE_FAST": self.visit_store_fast,
            "LOAD_GLOBAL": self.visit_load_global,
            "LOAD_CONST": self.visit_load_const,
            "POP_TOP": self.visit_pop_top,
            "CALL_FUNCTION": self.visit_call_function,
            "RETURN_VALUE": self.visit_return,
            "FOR_ITER": self.visit_for,
            "BREAK_LOOP": self.visit_break_loop,
            "SETUP_LOOP": self.visit_setup_block,
            "POP_BLOCK": self.visit_pop_block,
        }
        self.visitors = dict()
        for name, visitor in name_visitors.items():
            self.visitors[opcode.opmap.get(name)] = visitor
        for op in una_opnames.keys():
            self.visitors[op] = self.visit_unary_op
        for op in bin_opnames.keys():
            self.visitors[op] = self.visit_binary_op
        for op in stack_ops:
            self.visitors[op] = self.visit_stack_op
        for op in unconditional_jump_ops.keys():
            self.visitors[op] = self.visit_unconditional_jump
        for op in conditional_jump_ops.keys():
            self.visitors[op] = self.visit_conditional_jump

    def feed(self, instr):
        if instr.opcode not in self.visitors:
            print("Warning: Unsupported instruction",
                  instr.opcode, "(%s)" % opcode.opname[instr.opcode])
        else:
            self.visitors[instr.opcode](instr)

    def visit_for(self, instr):
        # This is not what python does.
        # Modified for a stack balance check.
        self.stack.append(FuncApply("_typhon_iter_step", (self.stack.pop(),)))

    def visit_setup_block(self, instr):
        self.blocks.append(StaticBlock(instr.opcode, instr.argval))

    def visit_pop_block(self, instr):
        self.blocks.pop()

    def visit_break_loop(self, instr):
        assert self.blocks[-1].opcode == opcode.opmap.get("SETUP_LOOP")

    def visit_unary_op(self, instr):
        stack = self.stack
        stack.append(FuncApply(una_opnames[instr.opcode], (stack.pop(),)))

    def visit_binary_op(self, instr):
        stack = self.stack
        tos = stack.pop()
        tos1 = stack.pop()
        stack.append(FuncApply(bin_opnames[instr.opcode], (tos1, tos)))

    def visit_stack_op(self, instr):
        handle_stack_op(instr.opcode, self.stack)

    def visit_comparator_op(self, instr):
        if instr.argval not in comparator_names:
            raise ValueError("'%s' is not yet supported." % instr.argval)
        stack = self.stack
        tos = stack.pop()
        tos1 = stack.pop()
        compname = comparator_names[instr.argval]
        stack.append(FuncApply(compname, (tos1, tos)))

    def visit_unconditional_jump(self, instr):
        return

    def visit_conditional_jump(self, instr):
        self.stack.pop()

    def visit_load_fast(self, instr):
        variables = self.variables
        stack = self.stack
        if instr.argval not in variables:
            raise ValueError("Variable %s is used before initialization."
                             % instr.argval)
        stack.append(variables[instr.argval])

    def visit_store_fast(self, instr):
        v = self.variables.get(instr.argval, Variable(instr.argval))
        self.stack.pop()
        self.variables[instr.argval] = v

    def visit_load_global(self, instr):
        import builtins
        obj = getattr(builtins, instr.argval)
        if callable(obj):
            self.stack.append(FuncApply(instr.argval))
        else:
            raise ValueError("Globals other than builtin functions" +
                             "are not yet supported.")

    def visit_load_const(self, instr):
        self.stack.append(Constant(instr.argval))

    def visit_pop_top(self, instr):
        self.stack.pop()

    def visit_call_function(self, instr):
        arg = [self.stack.pop() for _ in range(instr.argval)][::-1]
        self.stack[-1].args = tuple(arg)

    def visit_return(self, instr):
        self.stack.pop()


class Analyzer(StackMachine):

    def visit_conditional_jump(self, instr):
        if self.stack.pop().reduce(set())[0] != base_types.PyInt:
            raise TypeError("Jump condition is not integral." +
                            " __bool__ is not yet supported.")

    def visit_store_fast(self, instr):
        v = self.variables.get(instr.argval, Variable(instr.argval))
        v.union(self.stack.pop().reduce(set())[0])
        self.variables[instr.argval] = v

    def visit_call_function(self, instr):
        arg = [self.stack.pop() for _ in range(instr.argval)][::-1]
        if not isinstance(self.stack[-1], FuncApply):
            raise TypeError(repr(self.stack[-1]) + " is not callable.")
        self.stack[-1].args = tuple(arg)

    def visit_pop_top(self, instr):
        self.stack.pop().reduce(set())

    def visit_return(self, instr):
        self.stack.pop().reduce(set())


class CodeGenerator(StackMachine):

    def __init__(self, variables):
        super().__init__()
        self.impls = set()
        self.body = list()
        self.variables = variables
        self.stack_var_id = 0

    def allocate_stack_var(self):
        self.stack_var_id += 1
        return "__stack_" + str(self.stack_var_id)

    def feed(self, instr):
        if instr.is_jump_target:
            self.body.append("BC_%d:" % instr.offset)
        super().feed(instr)

    def replace_top_with_temp_variable(self):
        t, expr = self.stack[-1].reduce(self.impls)
        tv = TempVar(t, self.allocate_stack_var())
        self.body.append(t.c_name + " " + tv.name + " = " + expr)
        self.stack[-1] = tv

    def visit_for(self, instr):
        it = self.stack.pop()
        self.stack.append(FuncApply("_typhon_iter_step", (it,)))
        t, expr = FuncApply("_typhon_iter_is_over", (it,)).reduce(self.impls)
        if t != base_types.PyInt:
            raise TypeError("Iteration end condition should be boolean type.")
        self.body.append("if (%s) goto BC_%d;" % (expr, instr.argval))
        self.replace_top_with_temp_variable()

    def visit_unary_op(self, instr):
        super().visit_unary_op(instr)
        self.replace_top_with_temp_variable()

    def visit_binary_op(self, instr):
        super().visit_binary_op(instr)
        self.replace_top_with_temp_variable()

    def visit_break_loop(self, instr):
        super().visit_break_loop(instr)
        self.body.append("goto BC_%d" % self.blocks[-1].end)

    def visit_unconditional_jump(self, instr):
        self.body.append("goto BC_%d" % instr.argval)

    def visit_conditional_jump(self, instr):
        applica = conditional_jump_ops[instr.opcode]
        cond = applica(self.stack.pop().reduce(self.impls)[-1])
        self.body.append("if (%s) goto BC_%d" % (cond, instr.argval))

    def visit_store_fast(self, instr):
        func = self.stack.pop()
        self.body.append(instr.argval + " = " + func.reduce(self.impls)[-1])

    def visit_call_function(self, instr):
        super().visit_call_function(instr)
        self.replace_top_with_temp_variable()

    def visit_return(self, instr):
        self.body.append("return " + self.stack.pop().reduce(self.impls)[-1])


def translate(bc_obj):
    # Two step
    # Step 1: Infer variable types
    analyzer = Analyzer()
    for instr in bc_obj:
        analyzer.feed(instr)
    assert len(analyzer.stack) == 0, "Side effects to stack."
    assert len(analyzer.blocks) == 0, "Side effects to static blocks."
    generator = CodeGenerator(analyzer.variables)
    # Step 2: Generate body code
    for instr in bc_obj:
        generator.feed(instr)
    return TranslationResult(
        generator.body,
        generator.impls,
        generator.variables
    )
