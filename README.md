# Typhon
Static Type Inference for Python.
The goal is to infer types without explicit notations as much as possible.
As systems with polymorphism are generally undecidable, we take approximations.

Currently typhon is only tested with python `3.8`.
In the future more versions will be made compatible.

## Status: Rebuilt, Preliminary
Supports:
- Most stuff with `int`, `float`, `complex` and `str`
- Assignment to variables and chained assignment
- Basic user-defined function with recursion, without variable length arguments or keyword arguments
- Basic function variables
- Basic higher order functions
- Basic `list` (homogeneously typed elements only, currently; some library functions are missing)
- If/While/For statements
- IfExp (`a if cond else b`) syntax
- `and`, `or` and `not`
- Transpiling a really, really small syntax subset into a High-level IR
- Basic support for exception

Short-term goals:
- Support more constructs for transpiler
- Import system

Laborious work (possibly generating from dynamically-run test cases?):
- Import type information for the standard library
- Built-in types and standard library at HIR backend (How to?)

Mid-term goals:
- Support tuples and inhomogeneously typed always-finite lists
- Support extended slicing
- Tiered optimizing on HIR
- Better intrinsic generation (current is somehow incomplete)
- Marshalling between python and transpiled result
- Allow `Any` at some stage for integration
- Basic support for user-defined classes (maybe callable classes are not considered at the time)
- More rigorous type checking (for typing rules that do not affect inference)
- Support Lambdas
- Support `raise ... from` syntax and `try ... else` syntax
- Support formatted string value syntax

## Caveats
- Augmented assignment (eg. `a += 1`) will be translated into `a = a + 1`, so inplace functions like `__iadd__` are never called.
- Operators do not fallback at the moment. `NotImplemented` is not supported.
