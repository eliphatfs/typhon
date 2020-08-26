# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:33:06 2020

@author: eliphat
"""
import dis
from . import AbstractImplementation, Polymorphic
from . import gen_format, name_of
from . import generator_main
from .. import type_system, bytecode
from ..type_system import type_solver


class PythonAbstraction(Polymorphic):

    def __init__(self, func):
        self.func = func
        self.bc = dis.Bytecode(self.func)
        self.env = self.func.__module__
        cfg = bytecode.cfg.create_cfg(self.bc)
        self.sir = bytecode.transpiler.transpile(cfg)

    def try_instantiate(self, interface, existence_mem, error='None'):
        arg_vars = dict()
        arg_types = []
        if len(interface.types) != self.bc.codeobj.co_argcount:
            return None
        for i in range(self.bc.codeobj.co_argcount):
            name = self.bc.codeobj.co_varnames[i]
            v = type_solver.VarType(name)
            arg_vars[name] = v
            arg_types.append((interface.types[i], v))
        nodes, tvars, var_vars = type_solver.decl_type_vars(self.sir, arg_vars)
        leqs, inits = type_solver.get_equations(nodes, tvars, arg_types)
        try:
            facts = type_solver.solve_equations(tvars, leqs,
                                                inits, existence_mem)
            return PythonImplementation(interface, self.bc, self.sir,
                                        var_vars, tvars, facts)
        except TypeError as exc:
            if error == 'None':
                import traceback
                traceback.print_exc()
                return None
            raise


class PythonImplementation(AbstractImplementation):

    def __init__(self, interface, bc, ir, var_vars, tvars, solved_types):
        self.interface = interface
        self.ir = ir
        self.tvars = tvars
        self.bc = bc
        self.var_vars = var_vars
        self.solved_types = solved_types

    def implements(self, interface):
        return self.interface == interface

    def run_generator(self):
        return generator_main.generate(self)

    def generate(self):
        types = self.interface.types
        body, _ = self.run_generator()
        modifier = ""
        varnames = self.bc.codeobj.co_varnames
        var_list = ', '.join(t.c_name + ' ' + b
                             for t, b in zip(types, varnames))
        return gen_format.format(
            result_type=self.get_result_type().c_name,
            name=name_of(self.interface.name, self.interface.types),
            code='\n    ' + ';\n    '.join(body) + ";\n",
            modifier=modifier,
            var_list=var_list
        )

    def get_used_types(self):
        return set(self.solved_types.values())

    def get_name(self):
        return name_of(self.interface.name, self.interface.types)

    def type_of_node(self, n):
        return self.solved_types[self.tvars[n]]

    def get_result_type(self):
        return self.type_of_node("__return__")

    def get_dependencies(self):
        _, dep = self.run_generator()
        return dep
