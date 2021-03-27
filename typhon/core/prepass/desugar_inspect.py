# -*- coding: utf-8 -*-
"""
Util for fetching source code after desugar.
Requires `astor`, preferably 0.8.1 as is developped against.

Created on Sat Mar 27 15:23:04 2021

@author: eliphat
"""
import ast
try:
    import astor
except ImportError:
    pass


from . import desugar


syms = dict()


class Back(astor.SourceGenerator):

    def visit_Symbol(self, node):
        if node not in syms:
            syms[node] = len(syms)
        self.write("$sym_%d" % syms[node])

    def visit_LetBinding(self, node):
        self.write(
            'let ', node.symbol,
            ' = ', node.bound_expr,
            ' in ', node.inner
        )


def run_desugar_with_src(src):
    return astor.to_source(
        desugar.run_desugar(ast.parse(src)),
        source_generator_class=Back
    )
