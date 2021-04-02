# Typhon
Static Type Inference for Python.
The goal is to infer types without explicit notations as much as possible.
As systems with polymorphism are generally undecidable, we take approximations.

Currently typhon is only tested with python `3.8`.
In the future more versions will be made compatible.

## Status: Rebuilt, Preliminary
Supports:
- Integer arithmetics (full support)
- Assignment to variables and chained assignment
- Basic user-defined function with recursion, without variable length arguments or keyword arguments
- Basic function variables
- Basic higher order functions
- Basic `list` (homogeneously typed elements only, currently; some library functions are missing)
- If/While statements
- IfExp (`a if cond else b`) syntax
- `and`, `or` and `not`
- Transpiling a really, really small syntax subset into a High-level IR

Short-term goals:
- Support more constructs for transpiler
- Implement backend for IR
- Exception handling
- Iterators and `for` loop. Python is strange in that it uses `raise StopIteration` to indicate end of sequence.

Laborious work (possibly generating from dynamically-run test cases?):
- Implement intrinsics for most builtin functions
- Import type information for the standard library

Mid-term goals:
- Import system
- Marshalling between python and transpiled result
- Allow `Any` at some stage for integration
- Tiered optimizing on HIR
- Basic support for user-defined classes (maybe callable classes are not considered at the time)
- More rigorous type checking

## Caveats
- The `while` statement does not support an `else` clause when transpiling.
- Augmented assignment (eg. `a += 1`) will be translated into `a = a + 1`, so inplace functions like `__iadd__` are never called.
- Operators do not fallback at the moment. `NotImplemented` is not supported.
