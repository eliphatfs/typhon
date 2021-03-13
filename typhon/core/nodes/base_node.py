# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:13:08 2021

@author: eliphat
"""
class BaseNode:
    def __init__(self, env):
        self.env = env

    def children(self):
        return []

    def typing(self, type_system):
        pass
