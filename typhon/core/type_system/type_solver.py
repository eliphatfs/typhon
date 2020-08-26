# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:21:17 2020

@author: eliphat
"""
import queue
from .. import simple_ir as sir
from . import base_types
from . import inference
from .. import concepts
from .. import codegen
import functools


Undecided = base_types.BaseType("Undecided", "#error Undecided type\n")


class Type:
    pass


class VarType(Type):  # Variable

    def __init__(self, name):
        self.name = name


class FuncResultType(Type):  # Interface construct

    def __init__(self, func, inputs):
        self.func = func
        self.inputs = inputs


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


def solve_var(type_var, leqs, facts, existence_mem):
    my_type = None
    facts[type_var] = Undecided
    while True:
        old_type = my_type
        for lesser, greater in leqs:
            if lesser is greater:
                continue
            if greater is type_var:
                tau1 = solve_type(lesser, leqs, facts, existence_mem)
                if tau1 is Undecided:
                    continue
                my_type = inference.type_merge(tau1, my_type)
        if old_type == my_type:
            break
    facts[type_var] = my_type
    return my_type


def solve_func(type_var, leqs, facts, existence_mem):
    solve = functools.partial(
                solve_type,
                leqs=leqs,
                facts=facts,
                existence_mem=existence_mem
            )
    interface = concepts.Interface(type_var.func,
                                   tuple(map(solve, type_var.inputs)))
    for x in interface.types:
        if x is Undecided:
            return Undecided
    if interface in existence_mem:
        return existence_mem[interface]
    existence_mem[interface] = Undecided
    impl = codegen.find_implementation(interface, existence_mem)
    # Tries lambda and polymorphic types
    # Maybe split out them for better patterns
    if impl is None:
        raise TypeError("No implementation for interface.", interface)
    existence_mem[interface] = impl.get_result_type()
    return existence_mem[interface]


def solve_type(type_var, leqs, facts, existence_mem):
    if type_var in facts:
        return facts[type_var]
    if isinstance(type_var, FuncResultType):
        return solve_func(type_var, leqs, facts, existence_mem)
    elif isinstance(type_var, VarType):
        return solve_var(type_var, leqs, facts, existence_mem)
    raise TypeError("Mismatched type var.", type_var)


def solve_equations(type_vars, leqs, inits, existence_mem):
    facts = dict()
    for tau, t in inits:
        facts[t] = tau
    for tvar in type_vars.values():
        facts[tvar] = solve_type(tvar, leqs, facts, existence_mem)
    for tvar in type_vars.values():
        if isinstance(tvar, VarType):
            for lesser, greater in leqs:
                if greater is tvar:
                    tau1 = solve_type(lesser, leqs, facts, existence_mem)
                    if inference.type_merge(tau1, facts[tvar]) != facts[tvar]:
                        raise TypeError("Failed to find stable point.", tvar)
    return facts
