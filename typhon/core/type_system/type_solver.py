# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:21:17 2020

@author: eliphat
"""
import queue
import collections
from .. import simple_ir as sir
from . import base_types
from . import inference
from .. import concepts
from .. import codegen


Undecided = base_types.BaseType("Undecided", "#error Undecided type\n")


class Type:
    pass


class VarType(Type):  # Variable

    def __init__(self, name):
        self.name = name
        self.type = None


class FuncResultType(Type):  # Interface construct

    def __init__(self, func, inputs):
        self.func = func
        self.inputs = inputs
        self.type = None


def decl_type_vars(ir, arg_vars):
    nodes = {node for block in ir for node in block}
    type_vars = dict()
    type_vars["__return__"] = VarType("__return__")
    var_vars = arg_vars
    Q = queue.Queue()
    for node in nodes:
        Q.put(node)
    while not Q.empty():
        cur = Q.get()
        if isinstance(cur, sir.Func):
            type_vars[cur] = FuncResultType(None, None)
            # We put in types in the second run
            for arg in cur.args:
                if arg not in nodes:
                    nodes.add(arg)
                    Q.put(arg)
        elif isinstance(cur, sir.ConditionalJump):
            if cur.cond not in nodes:
                nodes.add(cur.cond)
                Q.put(cur.cond)
        elif isinstance(cur, sir.Constant):
            type_vars[cur] = VarType(str(cur.val))
        elif isinstance(cur, sir.Variable):
            if cur.name not in var_vars:
                var_vars[cur.name] = VarType(str(cur.name))
            type_vars[cur] = var_vars[cur.name]
        elif isinstance(cur, sir.Return):
            if cur.expr not in nodes:
                nodes.add(cur.expr)
                Q.put(cur.expr)
        elif isinstance(cur, sir.Store):
            if cur.expr not in nodes:
                nodes.add(cur.expr)
                Q.put(cur.expr)
            if cur.v not in nodes:
                nodes.add(cur.v)
                Q.put(cur.v)
    for node in nodes:
        if isinstance(node, sir.Func):
            type_vars[node].func = node.name
            type_vars[node].inputs = [type_vars[arg] for arg in node.args]
    return nodes, type_vars, var_vars


def get_equations(nodes, type_vars, arg_var_types):
    leqs = []  # (a, b) -> a <= b
    inits = arg_var_types  # (t, b) -> b: t
    for n in nodes:
        if isinstance(n, sir.Store):
            leqs.append((type_vars[n.expr], type_vars[n.v]))
        elif isinstance(n, sir.Constant):
            inits.append((base_types.from_const(n.val), type_vars[n]))
        elif isinstance(n, sir.Return):
            leqs.append((type_vars[n.expr], type_vars["__return__"]))
    return leqs, inits


def solve_equations(type_vars, leqs, inits, existence_mem):
    booked = set()
    Q = queue.Queue()
    for tau, t in inits:
        t.type = tau
        booked.add(t)
        Q.put(t)
    leq_cache = collections.defaultdict(list)
    for lesser, greater in leqs:
        leq_cache[lesser].append(greater)
    func_cache = collections.defaultdict(list)
    fname_cache = collections.defaultdict(list)
    for tvar in type_vars.values():
        if isinstance(tvar, FuncResultType):
            if len(tvar.inputs) == 0:
                interface = concepts.Interface(tvar.func, ())
                imp = codegen.find_implementation(interface, existence_mem)
                if imp is None:
                    raise TypeError("No implementation for interface.",
                                    interface)
                nt = inference.type_merge(tvar.type, imp.get_result_type())
                if nt is not None:
                    tvar.type = nt
                    if tvar not in booked:
                        booked.add(tvar)
                        Q.put(tvar)
            for s in tvar.inputs:
                func_cache[s].append(tvar)
            fname_cache[tvar.func].append(tvar)
    while not Q.empty():
        t = Q.get()
        booked.remove(t)
        for post in leq_cache[t]:
            old = post.type
            merged = inference.type_merge(old, t.type)
            if old != merged:
                post.type = merged
                if isinstance(post, VarType):
                    if post.name == '__return__':
                        for i, exist_tv in existence_mem.items():
                            if exist_tv.type is None:
                                codegen.find_implementation(i, existence_mem)
                                if exist_tv.type is not None:
                                    for fvar in fname_cache[i.name]:
                                        if fvar not in booked:
                                            booked.add(fvar)
                                            Q.put(fvar)
                if post not in booked:
                    booked.add(post)
                    Q.put(post)
        for post in func_cache[t]:
            args = tuple(map(lambda x: x.type, post.inputs))
            if any(x is None for x in args):
                continue
            interface = concepts.Interface(post.func, args)
            if interface in existence_mem:
                tx = existence_mem[interface].type
                if tx is None:
                    continue
                post.type = inference.type_merge(post.type, tx)
                if post not in booked:
                    booked.add(post)
                    Q.put(post)
            else:
                imp = codegen.find_implementation(interface, existence_mem)
                if imp is None:
                    raise TypeError("No implementation for interface.",
                                    interface)
                nt = inference.type_merge(post.type, imp.get_result_type())
                if nt is not None:
                    post.type = nt
                    if post not in booked:
                        booked.add(post)
                        Q.put(post)
    return {x: x.type for x in type_vars.values()}
