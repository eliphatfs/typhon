# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:58:32 2021

@author: eliphat
"""
import ast
from .ast_extensions import Symbol, LetBinding


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

    def visit_BoolOp(self, node):
        handled = self.visit(node.values[0])
        if len(node.values) == 1:
            return handled
        rest = ast.BoolOp(
            op=node.op,
            values=node.values[1:]
        )
        sym_handled = Symbol()
        let_bound = lambda expr: LetBinding(
            symbol=sym_handled,
            bound_expr=handled,
            inner=expr
        )
        if isinstance(node.op, ast.And):
            return ast.copy_location(let_bound(ast.IfExp(
                test=sym_handled,
                body=self.visit_BoolOp(rest),
                orelse=sym_handled
            )), node)
        elif isinstance(node.op, ast.Or):
            return ast.copy_location(let_bound(ast.IfExp(
                test=sym_handled,
                body=sym_handled,
                orelse=self.visit_BoolOp(rest)
            )), node)

    def visit_BinOp(self, node):
        func = ast.Attribute(value=self.visit(node.left),
                             attr=bin_op_map[type(node.op)],
                             ctx=ast.Load())
        call = ast.Call(func=func, args=[self.visit(node.right)], keywords=[])
        return ast.copy_location(call, node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.Not):
            return ast.copy_location(ast.IfExp(
                test=self.visit(node.operand),
                body=ast.Constant(value=False),
                orelse=ast.Constant(value=True),
            ), node)
        else:
            func = ast.Attribute(value=self.visit(node.operand),
                                 attr=unary_op_map[type(node.op)],
                                 ctx=ast.Load())
            call = ast.Call(func=func, args=[], keywords=[])
            return ast.copy_location(call, node)

    def visit_Compare(self, node):
        if len(node.ops) > 1:
            return self.visit(ast.copy_location(
                ast.BoolOp(
                    op=ast.And(),
                    values=[
                        ast.Compare(left=left, ops=[op], comparators=[right])
                        for left, op, right in zip([node.left] + node.comparators, node.ops, node.comparators)
                    ]
                ), node
            ))
        else:
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
