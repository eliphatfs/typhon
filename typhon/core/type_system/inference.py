# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:37:29 2020
Inference

This is currently only a temporary documentation of the
ideas of the type inference engine.

For the time being we only consider functions of numerical types,
that is,
(int | float) -> (int | float)
as

def f(x):
    return x + 2

then there is an inference:
    f(Type of x): __add__(Type of x, int)

If in global scope:
    f(p)

then constraint:
    f(Type of p)
which infers:
    __add__(Type of p, int)

Then the natural problem occurs that how to infer the return type of functions.
It is trivially reduced to inferring the result type of expressions.


Here are some tough cases:
1. Recurrence
Consider the simple counting function
    def identity(x):
        if x <= 0:
            return x
        return 1 + identity(x - 1)

We have constraints:
    __le__(Type of x, int)
    __add__(int, Type of result)
And inference:
    identity(Type of x): __add__(int, identity(Type of x))
But even worse, recurrence between multiple functions.
It can be seen as a ring on the call graph,
that is
t1: f1(t2)
t2: f2(t3)
...
tn: fn(t1)

@author: eliphat
"""
