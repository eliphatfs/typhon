# Typhon
Static Type Inference for Python.
The goal is to infer types without explicit notations as much as possible.
As systems with polymorphism are generally undecidable, we take approximations.

Currently typhon is only tested with python `3.8`. It should work from `3.6` to `3.8`.
In the future more versions will be made compatible.

## Status: Rebuilt, Preliminary
Supports:
- Integer arithmetics
- Assignment to variables and chained assignment
- Basic user-defined function with recursion, without variable length arguments or keyword arguments
- Basic function variables
- Basic higher order functions
- If/While statements

Short-term goals:
- Supporting `a if cond else b` syntax
- Supporting `and`, `or` and `not` syntaxes
- Type checking for implicit `__bool__` calls, and so on (no implications on interference)
- Basic support for generic classes. More specifically, intrinsics for the `list` type
- Transpiler to some statically typed language with current constructs,
  probably C++ since transpiler is designed as a co-product only.
  The major part in `typhon` is the type inference engine.
  C++ is complicated, but it is also more versatile since it is complicated.
- Implement intrinsics for most builtin functions

Also short-term, but lacks a clear design:
- Iterators and `for` loop. Python is strange in that it uses `raise StopIteration` to indicate end of sequence.

Laborious work (possibly generating from dynamically-run test cases?):
- Implement intrinsics for most builtin functions
- Import type information for the standard library

Mid-term goals:
- Basic support for user-defined classes (maybe callable classes are not considered at the time)
- Exception handling
- Memory management
- Marshalling between python and transpiled result
