# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:46:37 2020

@author: eliphat
"""
from . import core
import dis


def dep_closure(initial):
    f = set(initial)
    stack = list(initial)
    while len(stack) > 0:
        for dep in stack.pop().get_dependencies():
            if dep not in f:
                stack.append(dep)
                f.add(dep)
    return f


def generate_c(func):
    mian = core.codegen.python_impl\
        .PythonAbstraction(func)\
        .try_instantiate(core.concepts.Interface("main", []), dict(), 'raise')
    mian_dep = mian.get_dependencies()
    all_dep = dep_closure(mian_dep)
    all_dep.add(mian)
    includes = set()
    for imp in all_dep:
        if hasattr(imp, 'include'):
            includes.update(imp.include)
    file_header = '\n'.join(map(lambda x: "#include <%s>" % x, includes))
    types = {t for dep in all_dep for t in dep.get_used_types()}
    type_header = "".join(map(lambda t: t.definition, types))
    impls = list(map(lambda i: i.generate(), all_dep))
    impl_header = '\n'.join(map(lambda s: s[:s.find("{")] + ';', impls))
    return (file_header + '\n' + type_header + '\n'
            + impl_header + '\n'.join(impls))
