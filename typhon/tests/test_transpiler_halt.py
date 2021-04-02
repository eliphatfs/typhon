# -*- coding: utf-8 -*-
import unittest
import typhon
# import pprint


code_fib = """
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)

f(35)
"""


class TranspilerHaltTest(unittest.TestCase):

    def test_fib(self):
        res = typhon.core.type_infer(code_fib)
        tth = typhon.transpiler.hir.tree_to_hir.TreeToHIR()
        tth.root_transpile(res.ast)
        # pprint.pprint(tth.hir.ser())
