# -*- coding: utf-8 -*-
from ....abstract_variable import AbstractVariable
from ...type_var import TypeVar
registry = dict()


def add_intrinsic(name, intrinsic):
    registry[name] = AbstractVariable(
        TypeVar(name, intrinsic),
        name
    )

from . import type_constructors
