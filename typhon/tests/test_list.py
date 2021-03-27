import unittest
import typhon


code_calls = """
a = list()
a.append(False)
a.append(True)
b = list()
b.append(a)
c = [1, 2, 3]
d = [[], []]
"""
code_empty_visit = """
a = []
a[0] = 1
a.append(2)
b = a[0]
c = a[1] = 0
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
        self.assertEqual(
            res.env.query_name("c").TV.T.name,
            "builtins.list[builtins.int]"
        )
        self.assertEqual(
            res.env.query_name("d").TV.T.name,
            "builtins.list[builtins.list[Bottom]]"
        )

    def test_empty_visit(self):
        # Though this will fail with a runtime OOR,
        # it typechecks.
        res = typhon.core.type_infer(code_empty_visit)
        self.assertEqual(
            res.env.query_name("a").TV.T.name,
            "builtins.list[builtins.int]"
        )
        self.assertEqual(
            res.env.query_name("b").TV.T.name,
            "builtins.int"
        )
        self.assertEqual(
            res.env.query_name("c").TV.T.name,
            "builtins.int"
        )
