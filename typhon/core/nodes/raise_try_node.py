import typing
from .base_node import BaseNode, ExprNode, StmtNode
from ..type_system import SubtypeConstraint, FuncCallConstraint
from ..type_system import TypeVar


class RaiseStmtNode(StmtNode):
    def __init__(self, env, expr):
        super().__init__(env)
        self.expr = expr

    def children(self):
        return [self.expr]


class ExceptHandlerNode(BaseNode):
    def __init__(self, env, expr: ExprNode, caught: typing.Optional[ExprNode], body):
        super().__init__(env)
        self.expr = expr
        self.caught = caught
        self.body = body

    def children(self):
        if self.caught is None:
            return [self.expr] + self.body
        else:
            return [self.expr, self.caught] + self.body

    def typing(self, ts):
        if self.caught is None:
            return
        instance = TypeVar("<except instance>")
        ts.add_var(instance)
        ts.add_constraint(FuncCallConstraint(
            self.expr.value_type_var(),
            instance,
            []
        ))
        ts.add_constraint(SubtypeConstraint(
            self.caught.value_type_var(),
            instance
        ))


class TryExceptNode(StmtNode):
    def __init__(self, env, body, handlers, finally_body):
        super().__init__(env)
        self.body = body
        self.handlers = handlers
        self.finally_body = finally_body

    def children(self):
        return self.body + self.handlers + self.finally_body
