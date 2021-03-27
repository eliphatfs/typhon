import unittest
import typhon


code_calls = """
a = list()
a.append(False)
a.append(True)
b = list()
b.append(a)
"""


class ListTest(unittest.TestCase):

    def test_calls(self):
        res = typhon.core.type_infer(code_calls)
        self.assertEqual(
            res.env.query_name("a").TV.T.name,
            "builtins.list[builtins.bool]"
        )
        self.assertEqual(
            res.env.query_name("b").TV.T.name,
            "builtins.list[builtins.list[builtins.bool]]"
        )