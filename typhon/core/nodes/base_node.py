# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:13:08 2021

@author: eliphat
"""
from ..type_system import PolymorphicType
from ..type_system.type_var import TypeVar


class BaseNode:
    def __init__(self, env):
        self.env = env

    def children(self):
        return []

    def typing(self, type_system):
        pass

    def pprint(self, depth=0):
        children = self.children()
        me = "  " * depth + type(self).__name__
        if type(self).__str__ is not object.__str__:
            me += "[" + str(self) + ']'
        lines = [me]
        for child in children:
            lines.append(child.pprint(depth + 1))
        return '\n'.join(lines)

    def __repr__(self):
        return self.pprint()


class StmtNode(BaseNode):
    pass


class RootNodeMixin:

    def typing_all_subs(self, type_system):
        self.add_env_typevars(self.env, type_system)
        self.typing_sub(self, type_system)

    def add_env_typevars(self, env, ts):
        for c in env.children:
            self.add_env_typevars(c, ts)
        for symbol in env.symbols.keys():
            env.symbols[symbol] = TypeVar(
                env.qualname + "$sym_%d" % abs(id(symbol))
            )
        for abs_var in env.bindings.values():
            if abs_var.TV is not None:
                continue
            if abs_var.func_binding is not None:
                abs_var.TV = TypeVar(
                    env.qualname + abs_var.name,
                    init_type=PolymorphicType(abs_var.name, {abs_var.func_binding})
                )
            else:
                abs_var.TV = TypeVar(
                    env.qualname + abs_var.name
                )
            ts.add_var(abs_var.TV)

    def typing_sub(self, node, ts):
        for c in node.children():
            self.typing_sub(c, ts)
        node.typing(ts)


class ExprNode(BaseNode):
    def value_type_var(self):
        raise NotImplementedError()


class DeterminedValue:
    def __init__(self, type_var, val):
        self.v = val
        self.TV = type_var
