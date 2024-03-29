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
f = c.index("bb")
"""
code_bytes_basic = """
a = b"abbc"
b = a.replace(b"bb", b"aa")
c = b.index(b"aaa")
"""


class StrTest(unittest.TestCase):

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
        for v in "def":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )

    def test_bytes_basic(self):
        res = typhon.core.type_infer(code_bytes_basic)
        for v in "ab":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(b"")
            )
        for v in "c":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )
