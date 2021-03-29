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


class ContextChange(ast.NodeTransformer):
    def __init__(self, target_context):
        self.target_context = target_context

    def visit_Load(self, node):
        return ast.copy_location(self.target_context(), node)

    def visit_Store(self, node):
        return ast.copy_location(self.target_context(), node)


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
            inner=expr,
            ex_stmts=[]
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
        if len(node.targets) > 1:
            source_sym = Symbol()
            return self.visit(ast.copy_location(ast.Expr(LetBinding(
                symbol=source_sym,
                bound_expr=node.value,
                ex_stmts=[
                    ast.Assign(targets=[t], value=source_sym)
                    for t in node.targets
                ],
                inner=source_sym
            )), node))
        target = node.targets[0]
        if isinstance(target, ast.Subscript):
            return self.visit(ast.copy_location(ast.Expr(ast.Call(
                func=ast.Attribute(
                    value=target.value,
                    attr="__setitem__",
                    ctx=ast.Load()
                ),
                args=[target.slice, node.value],
                keywords=[]
            )), node))
        return self.generic_visit(node)

    def visit_Index(self, node):
        return self.generic_visit(node.value)

    def visit_Subscript(self, node):
        if isinstance(node.ctx, ast.Load):
            return self.visit(ast.copy_location(ast.Call(
                func=ast.Attribute(
                    value=node.value,
                    attr="__getitem__",
                    ctx=ast.Load()
                ),
                args=[node.slice],
                keywords=[]
            ), node))
        return self.generic_visit(node)

    def visit_List(self, node):
        if not isinstance(node.ctx, ast.Load):
            return self.generic_visit(node)
        list_sym = Symbol()
        node = self.generic_visit(node)
        return ast.copy_location(LetBinding(
            symbol=list_sym,
            bound_expr=ast.copy_location(
                ast.parse("list()", mode="eval").body,
                node
            ),
            inner=list_sym,
            ex_stmts=[
                ast.Expr(value=ast.Call(
                    func=ast.Attribute(
                        value=list_sym, attr="append", ctx=ast.Load()
                    ),
                    args=[elt],
                    keywords=[]
                ))
                for elt in node.elts
            ]
        ), node)

    def visit_AugAssign(self, node):
        return self.visit(ast.copy_location(ast.Assign(
            targets=[node.target],
            value=ast.BinOp(
                left=ContextChange(ast.Load).visit(node.target),
                op=node.op,
                right=node.value
            ),
        ), node))

    def wrap_test(self, test):
        return ast.Call(
            func=ast.Name(id='bool', ctx=ast.Load()),
            args=[test], keywords=[]
        )

    def visit_If(self, node):
        self.generic_visit(node)
        return ast.copy_location(ast.If(
            test=self.wrap_test(node.test),
            body=node.body,
            orelse=node.orelse
        ), node)

    def visit_While(self, node):
        self.generic_visit(node)
        return ast.copy_location(ast.While(
            test=self.wrap_test(node.test),
            body=node.body,
            orelse=node.orelse
        ), node)

    def visit_IfExp(self, node):
        self.generic_visit(node)
        return ast.copy_location(ast.IfExp(
            test=self.wrap_test(node.test),
            body=node.body,
            orelse=node.orelse
        ), node)

    def visit_Assert(self, node):
        self.generic_visit(node)
        return ast.copy_location(ast.Assert(
            test=self.wrap_test(node.test),
            msg=node.msg
        ), node)

def run_desugar(tree):
    return ast.fix_missing_locations(Desugar().visit(tree))
