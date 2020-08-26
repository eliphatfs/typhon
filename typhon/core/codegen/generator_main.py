# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:33:30 2020

@author: eliphat
"""
from . import find_implementation
from .. import simple_ir as sir
from ..analyze.tempvar_alloc import analyze_tva
from ..concepts import Interface


def generate(impl):
    body = []
    dep = []
    tva = analyze_tva(impl.ir)
    t_vars_c = dict()

    def genexpr(self, stmt=False):
        if isinstance(self, sir.Func):
            if self in t_vars_c:
                return t_vars_c[self]
            interface = Interface(self.name,
                                  tuple(map(impl.type_of_node, self.args)))
            imp = find_implementation(interface, None)
            dep.append(imp)
            arglist = ', '.join(map(genexpr, self.args))
            expr = imp.get_name() + "(" + arglist + ")"
            if self in tva:
                body.append("%s stack_%d = %s"
                            % (impl.type_of_node(self).c_name,
                               len(t_vars_c), expr))
                t_vars_c[self] = "stack_%d" % len(t_vars_c)
                if stmt:
                    return None
                return t_vars_c[self]
            return expr
        elif isinstance(self, sir.Constant):
            if self.val is None:
                return "_typhon_create_none()"
            if type(self.val) is str:
                return '"' + self.val + '"'
            else:
                return str(self.val)
        elif isinstance(self, sir.Variable):
            return self.name
        elif isinstance(self, sir.Store):
            return self.v.name + " = " + genexpr(self.expr)
        elif isinstance(self, sir.ConditionalJump):
            return "if (%s) goto %s" % (genexpr(self.cond),
                                        self.target_block.name)
        elif isinstance(self, sir.UnconditionalJump):
            return "goto %s" % self.target_block.name
        elif isinstance(self, sir.Return):
            return "return %s" % genexpr(self.expr)

    for var_var in impl.var_vars:
        body.append(impl.solved_types[impl.var_vars[var_var]].c_name
                    + " " + var_var)
    for block in impl.ir:
        body.append(block.name + ":")
        for red in block:
            gen = genexpr(red, True)
            if gen is not None:
                body.append(gen)
    return body, dep
