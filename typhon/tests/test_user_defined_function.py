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
code_func_variable = """
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

F = add
s = F(1, 2)
F = sub
d = F(3, -5)
"""
code_scoping = """
def A():
    a = 1
    return a

def B():
    b = None
    return b

def AA():
    a = False
    return a

def Poly(a):
    return a

def Glob():
    return a

b = A()
b = Poly(b + 1)
a = B()
a = Glob()
a = Poly(B())
z = Poly(b > 0)
z = AA()
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

    def test_function_variable(self):
        res = typhon.core.type_infer(code_func_variable)
        self.assertEqual(
            res.env.query_name("s").TV.T,
            res.ts.query_val_type(0)
        )
        self.assertEqual(
            res.env.query_name("d").TV.T,
            res.ts.query_val_type(0)
        )

    def test_scoping(self):
        res = typhon.core.type_infer(code_scoping)
        self.assertEqual(
            res.env.query_name("a").TV.T,
            res.ts.query_val_type(None)
        )
        self.assertEqual(
            res.env.query_name("b").TV.T,
            res.ts.query_val_type(0)
        )
        self.assertEqual(
            res.env.query_name("z").TV.T,
            res.ts.query_val_type(True)
        )
