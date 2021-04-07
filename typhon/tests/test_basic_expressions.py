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
raise exc
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
