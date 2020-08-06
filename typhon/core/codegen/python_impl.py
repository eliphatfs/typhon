# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:33:06 2020

@author: eliphat
"""
import dis
from . import AbstractImplementation, base_impls, gen_format, name_of
from ..bytecode import representations
from .. import stack_machine


class PythonImplementation(AbstractImplementation):

    def __init__(self, func):
        base_impls[func.__qualname__].append(self)
        self.func = func
        self.bc = dis.Bytecode(self.func)
        self.memoize = dict()

    def run_analyzer(self, types):
        if types in self.memoize:
            return self.memoize[types]
        self.memoize[types] = None
        analyzer = stack_machine.Analyzer(self.bc)
        for i in range(self.bc.codeobj.co_argcount):
            name = self.bc.codeobj.co_varnames[i]
            v = representations.Variable(name)
            v.py_type = types[i]
            analyzer.result.variables[name] = v
        analyzer.run()
        self.memoize[types] = analyzer.result
        return analyzer.result

    def implements(self, interface):
        if len(interface.types) != self.bc.codeobj.co_argcount:
            return False
        try:
            self.run_analyzer(interface.types)
            return True
        except Exception:
            return False

    def run_generator(self, variables):
        generator = stack_machine.CodeGenerator(self.bc, variables)
        generator.run()
        return generator.result

    def generate(self, types):
        result = self.run_analyzer(types)
        result = self.run_generator(result.variables)
        modifier = "static"
        varnames = self.bc.codeobj.co_varnames
        var_list = ', '.join(t.c_name + ' ' + b
                             for t, b in zip(types, varnames))
        return gen_format.format(
            result_type=self.get_result_type(types).c_name,
            name=name_of(self),
            code=' ' * 4 + ';\n    '.join(result.body) + ";\n",
            modifier=modifier,
            var_list=var_list
        )

    def get_name(self):
        return self.func.__qualname__

    def get_result_type(self, types):
        return self.run_analyzer(types).return_type

    def get_dependencies(self, types):
        return self.run_generator().impls
