# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:09:26 2020
Playing with bytecodes to implement simple loops, and to profile the instructions.
Requires CPython 3.5.x or lower for the handcrafted byte code to work properly.

@author: eliphat
"""
import types
import opcode
import dis
import numba


@numba.jit
def f_jit(y):
    x = 0
    for i in range(y):
        x += i
    return x


def f():
    x = 0
    for i in range(1000000):
        x += i
    return x


def f_us():
    x = 0
    for i in range(1000000):
        x += i
    return x


def w():
    x = 0
    i = 0
    while i < 1000000:
        x += i
        i += 1
    return x


def w_us():
    x = 0
    i = 0
    while i < 1000000:
        x += i
        i += 1
    return x


def f_glo_2():
    global x
    x = 0
    for i in range(1000000):
        x += i
    return x


f_glo = compile("""
x = 0
for i in range(1000000):
    x += i
""", "", "exec", optimize=2)


"""
Equiv BC:
    0: LOAD_CONST 1 (0)
    3: LOAD_GLOBAL 0 (range)
    6: LOAD_CONST 2 (1000000)
    9: CALL_FUNCTION 1
    12: GET_ITER
    13: FOR_ITER 7
    16: ROT_TWO
    17: ROT_THREE
    18: INPLACE_ADD
    19: ROT_TWO
    20: JUMP_ABSOLUTE 13
    23: RETURN_VALUE
"""
bc_new = [
    opcode.opmap["LOAD_CONST"], 1, 0,
    opcode.opmap["LOAD_GLOBAL"], 0, 0,
    opcode.opmap["LOAD_CONST"], 2, 0,
    opcode.opmap["CALL_FUNCTION"], 1, 0,
    opcode.opmap["GET_ITER"],
    opcode.opmap["FOR_ITER"], 7, 0,
    opcode.opmap["ROT_TWO"],
    opcode.opmap["ROT_THREE"],
    opcode.opmap["INPLACE_ADD"],
    opcode.opmap["ROT_TWO"],
    opcode.opmap["JUMP_ABSOLUTE"], 13, 0,
    opcode.opmap["RETURN_VALUE"]
]

co = f.__code__
# dis.dis(co)
bc_old = co.co_code
co = types.CodeType(
        co.co_argcount,
        co.co_kwonlyargcount,
        co.co_nlocals,
        co.co_stacksize,
        co.co_flags,
        bytes(bc_new),
        co.co_consts,
        co.co_names,
        co.co_varnames,
        co.co_filename,
        'f_opt',
        co.co_firstlineno,
        co.co_lnotab,
        co.co_freevars,
        co.co_cellvars
    )


f.__code__ = co
# dis.dis(f)
# print(f())
