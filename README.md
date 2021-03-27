# Typhon
Static Type Inference for Python.
The goal is to infer types without explicit notations as much as possible.
As systems with polymorphism are generally undecidable, we take approximations.

Currently typhon is only tested with python `3.8`. It should work from `3.6` to `3.8`.
In the future more versions will be made compatible.

## Status: Rebuilt, Preliminary
Supports:
- Integer arithmetics (full support)
- Assignment to variables and chained assignment
- Basic user-defined function with recursion, without variable length arguments or keyword arguments
- Basic function variables
- Basic higher order functions
- If/While statements
- IfExp (`a if cond else b`) syntax
- `and`, `or` and `not`

Short-term goals:
- Syntaxes related with `list`
- Transpiler to some statically typed language with current constructs,
  probably C++ since transpiler is designed as a co-product only.
  The major part in `typhon` is the type inference engine.
  C++ is complicated, but it is also more versatile since it is complicated.
- Type checking for implicit `__bool__` calls, and so on (no implications on interference)

Laborious work (possibly generating from dynamically-run test cases?):
- Implement intrinsics for most builtin functions
- Import type information for the standard library

Mid-term goals:
- Exception handling
- Iterators and `for` loop. Python is strange in that it uses `raise StopIteration` to indicate end of sequence.
- Basic support for user-defined classes (maybe callable classes are not considered at the time)
- Memory management
- Marshalling between python and transpiled result
