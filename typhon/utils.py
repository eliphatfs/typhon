# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:54:41 2020

@author: eliphat
"""


def subclasses(t):
    direct = set(t.__subclasses__())
    indirect = set()
    for sub in direct:
        indirect.update(subclasses(sub))
    return direct.union(indirect)
