import unittest
import typhon


code_basic = """
def add(a, b):
    return a + b

r = add(1, 3)
"""
code_recursion = """
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

r = fib(30)
"""
code_higher_order = """
def identity(a):
    def _id():
        return a
    return _id

def add(a):
    def _add(b):
        return a + b
    return _add

n = identity(3)()
r = add(n)(5)
"""


class UserDefinedFunctionTest(unittest.TestCase):

    def test_basic(self):
        res = typhon.core.type_infer(code_basic)
        self.assertEqual(
            res.env.query_name("r").TV.T,
            res.ts.query_val_type(0)
        )

    def test_recursion(self):
        res = typhon.core.type_infer(code_recursion)
        self.assertEqual(
            res.env.query_name("r").TV.T,
            res.ts.query_val_type(0)
        )

    def test_higher_order(self):
        res = typhon.core.type_infer(code_higher_order)
        self.assertEqual(
            res.env.query_name("n").TV.T,
            res.ts.query_val_type(0)
        )
        self.assertEqual(
            res.env.query_name("r").TV.T,
            res.ts.query_val_type(0)
        )
