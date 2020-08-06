# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:10:58 2020

@author: eliphat
"""
import os
import typhon


def f():
    print("Hello World")
    return 0


def g():
    a = int(input())
    b = int(input())
    print(a + b)
    return 0


def h():
    s = 0
    i = 0
    while i <= 1000000:
        s += i
        i += 1
    print(s)
    return 0


def i():
    s = 3 > ~2
    k = not s
    if k:
        print("Haha!")
    else:
        print("Wuwu.")
    return 0


def j():
    return 2 @ 5


def k():
    for i in range(100, 1000):
        first = i // 100
        second = (i % 100) // 10
        third = i % 10
        if i == first ** 3 + second ** 3 + third ** 3:
            print(i)
            break
    return 0


def add(a, b):
    return a + b


def m():
    print(add(1, 3))
    return 0


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def n():
    print(fib(int(input())))
    return 0


if not os.path.exists("./temp"):
    os.mkdir("./temp")
with open("temp/hello_world.c", "w") as fo:
    fo.write(typhon.generate_c(f))
with open("temp/a_plus_b_problem.c", "w") as fo:
    fo.write(typhon.generate_c(g))
with open("temp/sum_1_to_1000000.c", "w") as fo:
    fo.write(typhon.generate_c(h))
with open("temp/unary_condition.c", "w") as fo:
    fo.write(typhon.generate_c(i))
try:
    fo.write(typhon.generate_c(j))
except Exception as exc:
    print("Transpilation fails with exception:", exc)
with open("temp/water_flower_number.c", "w") as fo:
    fo.write(typhon.generate_c(k))
with open("temp/func_call.c", "w") as fo:
    fo.write(typhon.generate_c(m))
with open("temp/fib.c", "w") as fo:
    fo.write(typhon.generate_c(n))
