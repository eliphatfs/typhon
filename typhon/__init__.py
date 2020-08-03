# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:46:37 2020

@author: eliphat
"""
from . import core
import dis


def generate_c(func):
    bc = dis.Bytecode(func)
    result = core.stack_machine.translate(bc)
    includes = set()
    for imp in result.impls:
        includes.update(imp.include)
    file_header = '\n'.join(map(lambda x: "#include <%s>" % x, includes))
    types = {var.py_type for var in result.variables.values()}
    for imp in result.impls:
        types.add(imp.result_type)
        for t in imp.types:
            types.add(t)
    type_header = "".join(map(lambda t: t.definition, types))
    impl_header = "\n".join(map(lambda i: core.codegen.generate(i),
                                result.impls))
    main_header = "int main() {\n\t"
    main_variables = []
    for var in result.variables.values():
        main_variables.append("%s %s;\n\t" % (var.py_type.c_name, var.name))
    main_body = ';\n\t'.join(result.body)
    main_tail = ";\n}\n"
    return (file_header + '\n' + type_header + '\n' + impl_header
            + main_header + ''.join(main_variables) + main_body + main_tail)
