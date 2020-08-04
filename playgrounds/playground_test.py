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


def f3():
    s = "hi"
    print(s.startswith)
    s.startswith("u")
    if 'i' in s or s is not None:
        return


def f4():
    a = 0
    lambda x: 5

    def _f4_i():
        return a
    dis.show_code(_f4_i)
    dis.dis(_f4_i)
    return [x for x in range(10)]


def f5():
    a = 0
    while a < 10:
        a += 1


class ErrorFloat:

    def __float__(self):
        return "I'm not a float"


if __name__ == "__main__":
    print("F1")
    dis.dis(f1)
    print("F2")
    dis.dis(f2)
    print("F3")
    dis.dis(f3)
    print("F4")
    dis.dis(f4)
    print("F5")
    dis.dis(f5)
