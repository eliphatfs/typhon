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
a = b = c = d = e = 1
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
