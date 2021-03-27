# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:59:17 2021

@author: eliphat
"""
from . import add_intrinsic
from ..intrinsic_function import WrapperIntrinsic
from ..py_list import PyList


add_intrinsic("list", WrapperIntrinsic(lambda: PyList()))
