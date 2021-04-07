from .base_node import StmtNode


class RaiseNode(StmtNode):
    def __init__(self, env, expr):
        super().__init__(env)
        self.expr = expr

    def children(self):
        return [self.expr]
