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
            s += i
            continue
        s += i
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


def f6():
    return range(10)[1:7:3]


def f7(a, b):
    return a + b


def f8(a, b):
    return f7(a, b)


def dictify(obj, recursive=False):
    d = dict()
    for name in dir(obj):
        if name in ['__globals__', '__locals__']:
            continue
        attr = getattr(obj, name)
        d[name] = dictify(attr, True) if recursive else attr
    return d


def f9():

    def _f9(a=[]):
        pass

    return _f9


class ErrorFloat:

    def __float__(self):
        return "I'm not a float"


if __name__ == "__main__":
    dis.show_code(f9)
    dis.dis(f9)
