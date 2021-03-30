# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:16:01 2021

@author: eliphat
"""
from . import sanitize, CommonTranspiler


class F2C(CommonTranspiler):
    def __init__(self, env, func, indent=0, indent_str="    "):
        super().__init__(indent, indent_str)
        self.env = env
        self.func = func

    def write_declare(self, T, name):
        self.write(sanitize(T.name))
        self.write(" * ")
        self.write(name)
        self.write(";")
        self.newline()

    def declarations(self):
        symbol_use = {k: i for i, k in enumerate(self.env.symbols.keys())}
        for sym in self.env.symbols.keys():
            name = "_sym_%d" % symbol_use[sym]
            ty = self.env.symbols[name].TV.T
            self.write_declare(ty, name)
        for name, abs_var in self.env.bindings.items():
            self.write_declare(abs_var.TV.T, name)
        if self.env.parent is not None:
            pass

    def constructor(self):
        self.write(self.func.TV.T)
        self.write("() {")
        self.indent += 1
        for name in self.env.bindings.keys():
            self.write(name)
            self.write(" = new auto;")
            self.newline()
        self.indent -= 1
        self.write("}")
