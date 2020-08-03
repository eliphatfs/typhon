# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:56:10 2020

@author: eliphat
"""
import dis


def f1():
    a = 1
    print(a)


def f2():
    s = 0
    for i in range(10):
        s += i
        if i == 8:
            break
    else:
        s = 10
    print(s)


if __name__ == "__main__":
    print("F1")
    dis.dis(f1)
    print("F2")
    dis.dis(f2)
