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


if not os.path.exists("./temp"):
    os.mkdir("./temp")
with open("temp/hello_world.c", "w") as fo:
    fo.write(typhon.generate_c(f))
with open("temp/a_plus_b_problem.c", "w") as fo:
    fo.write(typhon.generate_c(g))
with open("temp/sum_1_to_1000000.c", "w") as fo:
    fo.write(typhon.generate_c(h))
