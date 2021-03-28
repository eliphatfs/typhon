# -*- coding: utf-8 -*-
import unittest
import typhon


code_sums = """
s = 0
i = 1
while i <= 100000:
    s += i
    i += 1
"""
code_break_continue = """
i = 0
while True:
    i += 1
    if i == 20:
        break
    else:
        continue
"""


class LoopsTest(unittest.TestCase):

    def test_sums(self):
        res = typhon.core.type_infer(code_sums)
        for v in "si":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )

    def test_break_continue(self):
        res = typhon.core.type_infer(code_break_continue)
        for v in "i":
            self.assertEqual(
                res.env.query_name(v).TV.T,
                res.ts.query_val_type(0)
            )
