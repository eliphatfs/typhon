# Typhon
Static Type Inference for Python.
The goal is to infer types without explicit notations as much as possible.
As a by-product, a traspiler targetting C is also included.

## Status: Preliminary
Supports:
- Function with no global side effects (`main` function should have no arguments and return `0`)
- Automatic resolving of dependent functions
- Recurrence in functions (Solving complex recurrences may be slow or buggy)
- `int` and `float` type
- Part of `str` type
- `while`, `if` and `for` statements
- Builtins: `input` and `print`
- Python version: Tested on 3.5, should support anywhere from 3.2 to 3.8

## Roadmap
(Near)
- Support for `is`, `is not` and other conditionals
- Support for `tuple` type and handling sum types
- Support for `break` on python <= 3.7 (Needs to handle dynamic CFG)

(Moderate)
- Support for `list` type
- Memory Management
- Support for `isinstance` and `type` functions
- Exceptions

(Far)
- Support for variable length functions, `*args` and `**kwargs`
- Support for higher order functions in python standard lib (map, reduce, filter)
- Support for higher order functions and lambdas
- Support for user defined classes (basic)
