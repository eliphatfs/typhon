import unittest
import typhon


code_integer = """
a = 1
b = 1 + 2 - 3 * 4 // 5
c = a + b - a
d = a * ((b // a) % c)
e = c & d ^ b
f = ~e | ~(d ** c)
"""
code_multi_assignment = """
a = b = c = d = 1
e = a + b - c + d
"""
code_conditional = """
a = 1
b = 1 or a or 3
c = True and False and True
d = not c
e = not b
f = d or e
g = 1 < 2 < a
"""
code_raise = """
a = 1
exc = Exception()
try:
    raise exc
except Exception as exc_caught:
    pass
"""
code_assign_expr = """
a = (b := 3)
"""
code_numerics = """
a = 1
b = a + 2.0
c = b + 2j
d = 4 - 5j
e = c * d + b
f = 1.3 ** 4
g = 2.718 ** 5.02
"""


class BasicExpressionTest(unittest.TestCase):

    def test_int_arithmetic(self):
        res = typhon.core.type_infer(code_integer)
        for v in "abcdef":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )

    def test_multiple_assignment(self):
        res = typhon.core.type_infer(code_multi_assignment)
        for v in "abcde":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )

    def test_conditional(self):
        res = typhon.core.type_infer(code_conditional)
        for v in "ab":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )
        for v in "cdefg":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(True)
            )

    def test_raise(self):
        res = typhon.core.type_infer(code_raise)
        self.assertEqual(
            res.env.query_name("a").TV.T,
            res.ts.query_val_type(0)
        )
        self.assertEqual(
            res.env.query_name("exc").TV.T.name,
            "builtins.Exception"
        )
        self.assertEqual(
            res.env.query_name("exc_caught").TV.T.name,
            "builtins.Exception"
        )

    def test_assign_expr(self):
        res = typhon.core.type_infer(code_assign_expr)
        self.assertEqual(
            res.env.query_name("a").TV.T,
            res.ts.query_val_type(0)
        )
        self.assertEqual(
            res.env.query_name("b").TV.T,
            res.ts.query_val_type(0)
        )

    def test_numerics(self):
        res = typhon.core.type_infer(code_numerics)
        self.assertEqual(
            res.env.query_name("a").TV.T,
            res.ts.query_val_type(0)
        )
        for floating in "bfg":
            self.assertEqual(
                res.env.query_name(floating).TV.T,
                res.ts.query_val_type(0.0)
            )
        for cplx in "cde":
            self.assertEqual(
                res.env.query_name(cplx).TV.T,
                res.ts.query_val_type(0.0 + 0.0j)
            )
