# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:10:58 2020

@author: eliphat
"""
import typhon


def f():
    print("Hello World")
    return 0


def g():
    a = int(input())
    b = int(input())
    print(a + b)
    return 0


with open("hello_world.c", "w") as fo:
    fo.write(typhon.generate_c(f))
with open("a_plus_b_problem.c", "w") as fo:
    fo.write(typhon.generate_c(g))
