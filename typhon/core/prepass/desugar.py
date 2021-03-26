# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:58:32 2021

@author: eliphat
"""
import ast


bin_op_map = {
    ast.Add: "__add__",
    ast.Sub: "__sub__",
    ast.Mult: "__mul__",
    ast.MatMult: "__matmul__",
    ast.Div: "__truediv__",
    ast.Mod: "__mod__",
    ast.Pow: "__pow__",
    ast.LShift: "__lshift__",
    ast.RShift: "__rshift__",
    ast.BitOr: "__or__",
    ast.BitXor: "__xor__",
    ast.BitAnd: "__and__",
    ast.FloorDiv: "__floordiv__",
}
unary_op_map = {
    ast.Invert: "__invert__",
    ast.UAdd: "__pos__",
    ast.USub: "__neg__",
}
compare_op_map = {
    ast.Eq: "__eq__",
    ast.NotEq: "__ne__",
    ast.Lt: "__lt__",
    ast.LtE: "__le__",
    ast.Gt: "__gt__",
    ast.GtE: "__ge__",
}


class Desugar(ast.NodeTransformer):

    def visit_Pass(self, node):
        return None

    def visit_Return(self, node):
        if node.value is None:
            return ast.copy_location(
                ast.Return(value=ast.Constant(value=None)),
                node
            )
        return self.generic_visit(node)

    def visit_BinOp(self, node):
        func = ast.Attribute(value=self.visit(node.left),
                             attr=bin_op_map[type(node.op)],
                             ctx=ast.Load())
        call = ast.Call(func=func, args=[self.visit(node.right)], keywords=[])
        return ast.copy_location(call, node)

    def visit_UnaryOp(self, node):
        func = ast.Attribute(value=self.visit(node.operand),
                             attr=unary_op_map[type(node.op)],
                             ctx=ast.Load())
        call = ast.Call(func=func, args=[], keywords=[])
        return ast.copy_location(call, node)

    def visit_Compare(self, node):
        assert len(node.ops) == 1
        func = ast.Attribute(value=self.visit(node.left),
                             attr=compare_op_map[type(node.ops[0])],
                             ctx=ast.Load())
        call = ast.Call(func=func, args=[self.visit(node.comparators[0])], keywords=[])
        return ast.copy_location(call, node)

    def visit_Assign(self, node):
        self.generic_visit(node)
        stmts = []
        for t, s in reversed(list(zip(node.targets, node.targets[1:] + [node.value]))):
            stmts.append(ast.copy_location(
                ast.Assign(targets=[t], value=s),
                node
            ))
        return stmts


def run_desugar(tree):
    return ast.fix_missing_locations(Desugar().visit(tree))
