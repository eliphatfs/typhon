# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:52:31 2020

@author: eliphat
"""
from collections import namedtuple


Interface = namedtuple(
    "Interface",
    ["name", "types"]
)


class AbstractImplementation:

    def implements(self, interface):
        raise NotImplementedError

    def generate(self, types):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_result_type(self, types):
        raise NotImplementedError

    def get_depedencies(self, types):
        raise NotImplementedError
