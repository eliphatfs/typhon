# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:46:37 2020

@author: eliphat
"""
from . import core
import dis


def _resolve(ordered, visited, impl):
    if impl not in visited:
        visited.add(impl)
        obj, inter = impl
        for dependency in obj.get_dependencies(inter.types):
            _resolve(ordered, visited, dependency)
        ordered.append(impl)


def resolve_impl_dependencies(impls):
    ordered = list()
    visited = set()
    for impl in impls:
        _resolve(ordered, visited, impl)
    return ordered


def generate_c(func):
    bc = dis.Bytecode(func)
    result = core.stack_machine.translate(bc, func.__module__)
    includes = set()
    impls = resolve_impl_dependencies(result.impls)
    for imp, interface in impls:
        if hasattr(imp, 'include'):
            includes.update(imp.include)
    file_header = '\n'.join(map(lambda x: "#include <%s>" % x, includes))
    types = {var.py_type for var in result.variables.values()}
    for imp, interface in impls:
        types.add(imp.get_result_type(interface.types))
        for t in interface.types:
            types.add(t)
    type_header = "".join(map(lambda t: t.definition, types))
    impl_header = "\n".join(map(lambda i: i[0].generate(i[1].types),
                                impls))
    main_header = "int main() {\n    "
    main_variables = []
    for var in result.variables.values():
        main_variables.append("%s %s;\n    " % (var.py_type.c_name, var.name))
    main_body = ';\n    '.join(result.body)
    main_tail = ";\n}\n"
    return (file_header + '\n' + type_header + '\n' + impl_header
            + main_header + ''.join(main_variables) + main_body + main_tail)
