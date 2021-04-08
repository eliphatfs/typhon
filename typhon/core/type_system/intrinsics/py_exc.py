# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:11:47 2021

@author: eliphat
"""
from ..type_repr import RecordType


py_base_exc = RecordType("builtins.BaseException", {})
py_exc = RecordType("builtins.Exception", {})
py_stop_iter = RecordType("builtins.StopIteration", {})
