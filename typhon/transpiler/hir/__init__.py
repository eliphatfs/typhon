"""
HIR: High-level Intermediate Representation

The IR has:
    1. Class abstraction
    2. Some room for optimizations as inlining etc.
    3. Stack based
    4. Tree based
"""
from . import instructions, klass, hir_container, tree_to_hir
