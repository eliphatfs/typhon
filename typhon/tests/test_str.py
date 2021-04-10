# -*- coding: utf-8 -*-
import unittest
import typhon


code_lu = """
a = "AaaA"
b = a.upper()
c = b.lower()
"""
code_replace_find = """
a = "AabA"
b = a.replace("Aa", "AB")
c = b.replace("Bb", "bb", 2)
d = c.find("Bb")
e = c.rindex("bb")
"""


class LoopsTest(unittest.TestCase):

    def test_lu(self):
        res = typhon.core.type_infer(code_lu)
        for v in "abc":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type("")
            )

    def test_replace_find(self):
        res = typhon.core.type_infer(code_replace_find)
        for v in "abc":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type("")
            )
        for v in "de":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )
