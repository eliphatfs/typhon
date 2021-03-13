# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:31:02 2021

@author: eliphat
"""

class BaseConstraint:
    def cause_vars():
        raise NotImplementedError()

    def effect_vars():
        raise NotImplementedError()

    def fix():
        raise NotImplementedError()

    def is_resolved():
        raise NotImplementedError()
