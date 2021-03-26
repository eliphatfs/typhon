# -*- coding: utf-8 -*-
from .base_node import ExprNode
from ..type_system import SubtypeConstraint
from ..type_system import TypeVar


class IfElseExprNode(ExprNode):
    def __init__(self, env, test: ExprNode, yes: ExprNode, no: ExprNode):
        super().__init__(env)
        self.test = test
        self.yes = yes
        self.no = no
        self.result_tv = None

    def children(self):
        return [self.test, self.yes, self.no]

    def typing(self, ts):
        self.result_tv = ts.add_var(TypeVar("<ifexp>"))
        ts.add_constraint(SubtypeConstraint(
            self.result_tv,
            self.yes.value_type_var()
        ))
        ts.add_constraint(SubtypeConstraint(
            self.result_tv,
            self.no.value_type_var()
        ))

    def value_type_var(self):
        return self.result_tv
