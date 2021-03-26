# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:52:48 2021

@author: eliphat
"""
import ast
import collections
from . import nodes, prepass, type_system


InferenceResult = collections.namedtuple(
    "InferenceResult",
    ["ts", "env", "ast"]
)


def type_infer(code, prog_name="<gamma>"):
    ts = type_system.TypeSystem(prog_name)
    env_root = nodes.environment.NodeEnv("", None)
    py_ast = ast.parse(code)
    desugar_ast = prepass.desugar.run_desugar(py_ast)
    typhon_ast = prepass.tree_transformer.typhon_tree(env_root, desugar_ast)
    typhon_ast.typing_all_subs(ts)
    ts.solve()
    return InferenceResult(ts, env_root, typhon_ast)
