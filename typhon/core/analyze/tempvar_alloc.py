# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:01:11 2020

@author: eliphat
"""
import collections
from .. import simple_ir as sir


def visit(node, count):
    if isinstance(node, sir.ConditionalJump):
        count[node.cond] += 1
        visit(node.cond, count)
    elif isinstance(node, sir.Return):
        count[node.expr] += 1
        visit(node.expr, count)
    elif isinstance(node, sir.Func):
        for arg in node.args:
            count[arg] += 1
            visit(arg, count)
    elif isinstance(node, sir.Store):
        count[node.expr] += 1
        visit(node.expr, count)


def analyze_tva(ir):
    count = collections.defaultdict(int)
    for block in ir:
        for node in block:
            visit(node, count)
    sv = set()
    for node, cnt in count.items():
        if cnt >= 1:
            sv.add(node)
    return sv
