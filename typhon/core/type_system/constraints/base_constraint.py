# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:31:02 2021

@author: eliphat
"""

class BaseConstraint:
    def cause_vars(self):
        raise NotImplementedError()

    def effect_vars(self):
        raise NotImplementedError()

    def fix(self):
        raise NotImplementedError()

    def is_resolved(self):
        raise NotImplementedError()
