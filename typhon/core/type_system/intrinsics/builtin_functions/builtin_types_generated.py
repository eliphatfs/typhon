# -*- coding: utf-8 -*-
from ..intrinsic_function import ArrowCollectionIntrinsic
from ...type_repr import FunctionType, RecordType

NoneType = RecordType("NoneType", {})
ellipsis = RecordType("ellipsis", {})
builtins_bool = RecordType("builtins.bool", {})
builtins_bytes = RecordType("builtins.bytes", {})
builtins_complex = RecordType("builtins.complex", {})
builtins_float = RecordType("builtins.float", {})
builtins_int = RecordType("builtins.int", {})
builtins_object = RecordType("builtins.object", {})
builtins_range = RecordType("builtins.range", {})
builtins_str = RecordType("builtins.str", {})
builtins_BaseException = RecordType("builtins.BaseException", {})
builtins_Exception = RecordType("builtins.Exception", {})
builtins_TypeError = RecordType("builtins.TypeError", {})
builtins_StopAsyncIteration = RecordType("builtins.StopAsyncIteration", {})
builtins_StopIteration = RecordType("builtins.StopIteration", {})
builtins_GeneratorExit = RecordType("builtins.GeneratorExit", {})
builtins_SystemExit = RecordType("builtins.SystemExit", {})
builtins_KeyboardInterrupt = RecordType("builtins.KeyboardInterrupt", {})
builtins_ImportError = RecordType("builtins.ImportError", {})
builtins_ModuleNotFoundError = RecordType("builtins.ModuleNotFoundError", {})
builtins_WindowsError = RecordType("builtins.WindowsError", {})
builtins_EOFError = RecordType("builtins.EOFError", {})
builtins_RuntimeError = RecordType("builtins.RuntimeError", {})
builtins_RecursionError = RecordType("builtins.RecursionError", {})
builtins_NotImplementedError = RecordType("builtins.NotImplementedError", {})
builtins_NameError = RecordType("builtins.NameError", {})
builtins_UnboundLocalError = RecordType("builtins.UnboundLocalError", {})
builtins_AttributeError = RecordType("builtins.AttributeError", {})
builtins_SyntaxError = RecordType("builtins.SyntaxError", {})
builtins_IndentationError = RecordType("builtins.IndentationError", {})
builtins_TabError = RecordType("builtins.TabError", {})
builtins_LookupError = RecordType("builtins.LookupError", {})
builtins_IndexError = RecordType("builtins.IndexError", {})
builtins_KeyError = RecordType("builtins.KeyError", {})
builtins_ValueError = RecordType("builtins.ValueError", {})
builtins_UnicodeError = RecordType("builtins.UnicodeError", {})
builtins_UnicodeEncodeError = RecordType("builtins.UnicodeEncodeError", {})
builtins_UnicodeDecodeError = RecordType("builtins.UnicodeDecodeError", {})
builtins_UnicodeTranslateError = RecordType("builtins.UnicodeTranslateError", {})
builtins_AssertionError = RecordType("builtins.AssertionError", {})
builtins_ArithmeticError = RecordType("builtins.ArithmeticError", {})
builtins_FloatingPointError = RecordType("builtins.FloatingPointError", {})
builtins_OverflowError = RecordType("builtins.OverflowError", {})
builtins_ZeroDivisionError = RecordType("builtins.ZeroDivisionError", {})
builtins_SystemError = RecordType("builtins.SystemError", {})
builtins_ReferenceError = RecordType("builtins.ReferenceError", {})
builtins_MemoryError = RecordType("builtins.MemoryError", {})
builtins_BufferError = RecordType("builtins.BufferError", {})
builtins_Warning = RecordType("builtins.Warning", {})
builtins_UserWarning = RecordType("builtins.UserWarning", {})
builtins_DeprecationWarning = RecordType("builtins.DeprecationWarning", {})
builtins_PendingDeprecationWarning = RecordType("builtins.PendingDeprecationWarning", {})
builtins_SyntaxWarning = RecordType("builtins.SyntaxWarning", {})
builtins_RuntimeWarning = RecordType("builtins.RuntimeWarning", {})
builtins_FutureWarning = RecordType("builtins.FutureWarning", {})
builtins_ImportWarning = RecordType("builtins.ImportWarning", {})
builtins_UnicodeWarning = RecordType("builtins.UnicodeWarning", {})
builtins_BytesWarning = RecordType("builtins.BytesWarning", {})
builtins_ResourceWarning = RecordType("builtins.ResourceWarning", {})
builtins_ConnectionError = RecordType("builtins.ConnectionError", {})
builtins_BlockingIOError = RecordType("builtins.BlockingIOError", {})
builtins_BrokenPipeError = RecordType("builtins.BrokenPipeError", {})
builtins_ChildProcessError = RecordType("builtins.ChildProcessError", {})
builtins_ConnectionAbortedError = RecordType("builtins.ConnectionAbortedError", {})
builtins_ConnectionRefusedError = RecordType("builtins.ConnectionRefusedError", {})
builtins_ConnectionResetError = RecordType("builtins.ConnectionResetError", {})
builtins_FileExistsError = RecordType("builtins.FileExistsError", {})
builtins_FileNotFoundError = RecordType("builtins.FileNotFoundError", {})
builtins_IsADirectoryError = RecordType("builtins.IsADirectoryError", {})
builtins_NotADirectoryError = RecordType("builtins.NotADirectoryError", {})
builtins_InterruptedError = RecordType("builtins.InterruptedError", {})
builtins_PermissionError = RecordType("builtins.PermissionError", {})
builtins_ProcessLookupError = RecordType("builtins.ProcessLookupError", {})
builtins_TimeoutError = RecordType("builtins.TimeoutError", {})
NoneType.add_function_member(
    "__bool__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
NoneType.members["__doc__"] = NoneType
NoneType.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([NoneType], builtins_bool)
    ])
)
NoneType.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
NoneType.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
NoneType.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([NoneType], builtins_bool)
    ])
)
NoneType.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
NoneType.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
ellipsis.members["__doc__"] = NoneType
ellipsis.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([ellipsis], builtins_bool)
    ])
)
ellipsis.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
ellipsis.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
ellipsis.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([ellipsis], builtins_bool)
    ])
)
ellipsis.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
ellipsis.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_bool.add_nomial_parent(builtins_int)
builtins_bool.add_function_member(
    "__abs__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__add__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__and__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__bool__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__ceil__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.members["__doc__"] = builtins_str
builtins_bool.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__float__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_float)
    ])
)
builtins_bool.add_function_member(
    "__floor__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__floordiv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_bool.add_function_member(
    "__ge__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__gt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__index__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__int__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__invert__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__le__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__lshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__lt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__mod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__mul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bool.add_function_member(
    "__neg__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__or__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__pos__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__pow__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__radd__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rand__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_bool.add_function_member(
    "__rlshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rmul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__ror__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__round__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rpow__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rrshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rsub__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rxor__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_bool.add_function_member(
    "__sub__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__truediv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_float), 
        FunctionType([builtins_int], builtins_float)
    ])
)
builtins_bool.add_function_member(
    "__trunc__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__xor__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "bit_length",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "conjugate",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bool.members["denominator"] = builtins_int
builtins_bool.members["imag"] = builtins_int
builtins_bool.members["numerator"] = builtins_int
builtins_bool.members["real"] = builtins_int
builtins_bool.add_function_member(
    "__rfloordiv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rmod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bool.add_function_member(
    "__rtruediv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_float), 
        FunctionType([builtins_int], builtins_float)
    ])
)
builtins_bytes.add_nomial_parent(builtins_object)
builtins_bytes.add_function_member(
    "__add__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "__contains__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_bytes.members["__doc__"] = builtins_str
builtins_bytes.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_bytes.add_function_member(
    "__ge__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__gt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "__le__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__len__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "__lt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__mod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_range], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "__mul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_bytes.add_function_member(
    "__rmul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_bytes.add_function_member(
    "capitalize",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "center",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "count",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "decode",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_bytes.add_function_member(
    "endswith",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, NoneType], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "expandtabs",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes), 
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "find",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "fromhex",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "hex",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_bytes.add_function_member(
    "index",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_bytes], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "isalnum",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "isalpha",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "isascii",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "isdigit",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "islower",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "isspace",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "istitle",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "isupper",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "join",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bytes), 
        FunctionType([builtins_str], builtins_bytes), 
        FunctionType([builtins_range], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "ljust",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "lower",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "lstrip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bytes), 
        FunctionType([NoneType], builtins_bytes), 
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "maketrans",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bytes], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "replace",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bytes, builtins_bool], builtins_bytes), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_int], builtins_bytes), 
        FunctionType([builtins_bytes, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_bytes, builtins_bytes], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "rfind",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_int, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "rindex",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_bytes, builtins_bool], builtins_int), 
        FunctionType([builtins_bytes, builtins_int], builtins_int), 
        FunctionType([builtins_bytes, NoneType], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_bytes], builtins_int)
    ])
)
builtins_bytes.add_function_member(
    "rjust",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int, builtins_bytes], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes), 
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "rstrip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bytes), 
        FunctionType([NoneType], builtins_bytes), 
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "startswith",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_bool), 
        FunctionType([builtins_bytes, NoneType], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_bytes, builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes, builtins_int], builtins_bool), 
        FunctionType([builtins_bytes, NoneType], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool)
    ])
)
builtins_bytes.add_function_member(
    "strip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_bytes), 
        FunctionType([NoneType], builtins_bytes), 
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "swapcase",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "title",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "translate",
    ArrowCollectionIntrinsic([
        FunctionType([NoneType, builtins_bytes], builtins_bytes), 
        FunctionType([NoneType], builtins_bytes), 
        FunctionType([NoneType], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "upper",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "zfill",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bytes), 
        FunctionType([builtins_int], builtins_bytes)
    ])
)
builtins_bytes.add_function_member(
    "__getitem__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_complex.add_nomial_parent(builtins_object)
builtins_float.add_nomial_parent(builtins_object)
builtins_int.add_nomial_parent(builtins_object)
builtins_int.add_function_member(
    "__abs__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__add__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__and__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__bool__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__ceil__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.members["__doc__"] = builtins_str
builtins_int.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__float__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_float)
    ])
)
builtins_int.add_function_member(
    "__floor__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__floordiv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_int.add_function_member(
    "__ge__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__gt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__index__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__int__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__invert__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__le__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__lshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__lt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__mod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__mul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_int], builtins_bool)
    ])
)
builtins_int.add_function_member(
    "__neg__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__or__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__pos__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__pow__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__radd__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rand__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_int.add_function_member(
    "__rfloordiv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rlshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rmod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rmul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__ror__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__round__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rpow__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rrshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rshift__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rsub__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__rtruediv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_float), 
        FunctionType([builtins_int], builtins_float)
    ])
)
builtins_int.add_function_member(
    "__rxor__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_int.add_function_member(
    "__sub__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__truediv__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_float), 
        FunctionType([builtins_int], builtins_float)
    ])
)
builtins_int.add_function_member(
    "__trunc__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "__xor__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_int], builtins_int)
    ])
)
builtins_int.add_function_member(
    "bit_length",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.add_function_member(
    "conjugate",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_int.members["denominator"] = builtins_int
builtins_int.members["imag"] = builtins_int
builtins_int.members["numerator"] = builtins_int
builtins_int.members["real"] = builtins_int
builtins_object.members["__doc__"] = builtins_str
builtins_object.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_object], builtins_bool)
    ])
)
builtins_object.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_object.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_object.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_object], builtins_bool)
    ])
)
builtins_object.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_object.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_range.add_nomial_parent(builtins_object)
builtins_range.add_function_member(
    "__bool__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_range.add_function_member(
    "__contains__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_bool), 
        FunctionType([builtins_bytes], builtins_bool), 
        FunctionType([builtins_int], builtins_bool), 
        FunctionType([builtins_str], builtins_bool), 
        FunctionType([builtins_range], builtins_bool), 
        FunctionType([ellipsis], builtins_bool), 
        FunctionType([NoneType], builtins_bool), 
        FunctionType([builtins_object], builtins_bool)
    ])
)
builtins_range.members["__doc__"] = builtins_str
builtins_range.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_range], builtins_bool)
    ])
)
builtins_range.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_range.add_function_member(
    "__getitem__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int)
    ])
)
builtins_range.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_range.add_function_member(
    "__len__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_range.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_range], builtins_bool)
    ])
)
builtins_range.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_range.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_range.add_function_member(
    "count",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int), 
        FunctionType([builtins_bytes], builtins_int), 
        FunctionType([builtins_int], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_range], builtins_int), 
        FunctionType([ellipsis], builtins_int), 
        FunctionType([NoneType], builtins_int), 
        FunctionType([builtins_object], builtins_int)
    ])
)
builtins_range.add_function_member(
    "index",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_int)
    ])
)
builtins_range.members["start"] = builtins_bool
builtins_range.members["step"] = builtins_bool
builtins_range.members["stop"] = builtins_int
builtins_str.add_nomial_parent(builtins_object)
builtins_str.add_function_member(
    "__add__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__contains__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.members["__doc__"] = builtins_str
builtins_str.add_function_member(
    "__eq__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__format__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__ge__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__gt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__hash__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_str.add_function_member(
    "__le__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__len__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_int)
    ])
)
builtins_str.add_function_member(
    "__lt__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__mod__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_range], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__mul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__ne__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "__repr__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__rmul__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__str__",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "capitalize",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "casefold",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "center",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "count",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str], builtins_int)
    ])
)
builtins_str.add_function_member(
    "encode",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_str], builtins_bytes), 
        FunctionType([builtins_str], builtins_bytes), 
        FunctionType([builtins_str], builtins_bytes), 
        FunctionType([], builtins_bytes)
    ])
)
builtins_str.add_function_member(
    "endswith",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_bool), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_bool), 
        FunctionType([builtins_str, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_bool), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_bool), 
        FunctionType([builtins_str, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_bool), 
        FunctionType([builtins_str, NoneType], builtins_bool), 
        FunctionType([builtins_str], builtins_bool), 
        FunctionType([builtins_str, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType], builtins_bool), 
        FunctionType([builtins_str], builtins_bool), 
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "expandtabs",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "find",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str], builtins_int)
    ])
)
builtins_str.add_function_member(
    "format",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_bool, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_bool, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_bool, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_bool, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_bool, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_bool, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_bool, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_bool, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_bytes, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_bytes, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_int, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_int, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_int, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_int, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_int, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_int, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_int, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_int, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_str, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_str, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_str, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_str, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_str, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_str, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_str, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_range, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_range, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_range, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_range, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_range, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_range, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_range, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_range, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_bool, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_bool, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_bool, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_int, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_int, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_int, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_str, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_str, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_str, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_range, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_range, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_range, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_range], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_bool], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_int], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_str], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_range], builtins_str), 
        FunctionType([ellipsis, ellipsis, ellipsis], builtins_str), 
        FunctionType([ellipsis, ellipsis, NoneType], builtins_str), 
        FunctionType([ellipsis, ellipsis, builtins_object], builtins_str), 
        FunctionType([ellipsis, ellipsis], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_bool], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_int], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_str], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_range], builtins_str), 
        FunctionType([ellipsis, NoneType, ellipsis], builtins_str), 
        FunctionType([ellipsis, NoneType, NoneType], builtins_str), 
        FunctionType([ellipsis, NoneType, builtins_object], builtins_str), 
        FunctionType([ellipsis, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_object, ellipsis], builtins_str), 
        FunctionType([ellipsis, builtins_object, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_object, builtins_object], builtins_str), 
        FunctionType([ellipsis, builtins_object], builtins_str), 
        FunctionType([ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_bool, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_bool, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_bool, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_bytes, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_int, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_int, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_int, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_str, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_str, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_str, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_range, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_range, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_range, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_range], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_bool], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_int], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_str], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_range], builtins_str), 
        FunctionType([NoneType, ellipsis, ellipsis], builtins_str), 
        FunctionType([NoneType, ellipsis, NoneType], builtins_str), 
        FunctionType([NoneType, ellipsis, builtins_object], builtins_str), 
        FunctionType([NoneType, ellipsis], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_bool], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_bytes], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_int], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_str], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_range], builtins_str), 
        FunctionType([NoneType, NoneType, ellipsis], builtins_str), 
        FunctionType([NoneType, NoneType, NoneType], builtins_str), 
        FunctionType([NoneType, NoneType, builtins_object], builtins_str), 
        FunctionType([NoneType, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_range], builtins_str), 
        FunctionType([NoneType, builtins_object, ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_object, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_object, builtins_object], builtins_str), 
        FunctionType([NoneType, builtins_object], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_bool], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_int], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_str], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_range], builtins_str), 
        FunctionType([builtins_object, ellipsis, ellipsis], builtins_str), 
        FunctionType([builtins_object, ellipsis, NoneType], builtins_str), 
        FunctionType([builtins_object, ellipsis, builtins_object], builtins_str), 
        FunctionType([builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_bool], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_int], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_str], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_range], builtins_str), 
        FunctionType([builtins_object, NoneType, ellipsis], builtins_str), 
        FunctionType([builtins_object, NoneType, NoneType], builtins_str), 
        FunctionType([builtins_object, NoneType, builtins_object], builtins_str), 
        FunctionType([builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_object, builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_object, builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_object], builtins_str), 
        FunctionType([builtins_bool, builtins_bool], builtins_str), 
        FunctionType([builtins_bool, builtins_bytes], builtins_str), 
        FunctionType([builtins_bool, builtins_int], builtins_str), 
        FunctionType([builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool, builtins_range], builtins_str), 
        FunctionType([builtins_bool, ellipsis], builtins_str), 
        FunctionType([builtins_bool, NoneType], builtins_str), 
        FunctionType([builtins_bool, builtins_object], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bool], builtins_str), 
        FunctionType([builtins_bytes, builtins_bytes], builtins_str), 
        FunctionType([builtins_bytes, builtins_int], builtins_str), 
        FunctionType([builtins_bytes, builtins_str], builtins_str), 
        FunctionType([builtins_bytes, builtins_range], builtins_str), 
        FunctionType([builtins_bytes, ellipsis], builtins_str), 
        FunctionType([builtins_bytes, NoneType], builtins_str), 
        FunctionType([builtins_bytes, builtins_object], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_bytes], builtins_str), 
        FunctionType([builtins_int, builtins_int], builtins_str), 
        FunctionType([builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int, builtins_range], builtins_str), 
        FunctionType([builtins_int, ellipsis], builtins_str), 
        FunctionType([builtins_int, NoneType], builtins_str), 
        FunctionType([builtins_int, builtins_object], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_bytes], builtins_str), 
        FunctionType([builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_range], builtins_str), 
        FunctionType([builtins_str, ellipsis], builtins_str), 
        FunctionType([builtins_str, NoneType], builtins_str), 
        FunctionType([builtins_str, builtins_object], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_bool], builtins_str), 
        FunctionType([builtins_range, builtins_bytes], builtins_str), 
        FunctionType([builtins_range, builtins_int], builtins_str), 
        FunctionType([builtins_range, builtins_str], builtins_str), 
        FunctionType([builtins_range, builtins_range], builtins_str), 
        FunctionType([builtins_range, ellipsis], builtins_str), 
        FunctionType([builtins_range, NoneType], builtins_str), 
        FunctionType([builtins_range, builtins_object], builtins_str), 
        FunctionType([builtins_range], builtins_str), 
        FunctionType([ellipsis, builtins_bool], builtins_str), 
        FunctionType([ellipsis, builtins_bytes], builtins_str), 
        FunctionType([ellipsis, builtins_int], builtins_str), 
        FunctionType([ellipsis, builtins_str], builtins_str), 
        FunctionType([ellipsis, builtins_range], builtins_str), 
        FunctionType([ellipsis, ellipsis], builtins_str), 
        FunctionType([ellipsis, NoneType], builtins_str), 
        FunctionType([ellipsis, builtins_object], builtins_str), 
        FunctionType([ellipsis], builtins_str), 
        FunctionType([NoneType, builtins_bool], builtins_str), 
        FunctionType([NoneType, builtins_bytes], builtins_str), 
        FunctionType([NoneType, builtins_int], builtins_str), 
        FunctionType([NoneType, builtins_str], builtins_str), 
        FunctionType([NoneType, builtins_range], builtins_str), 
        FunctionType([NoneType, ellipsis], builtins_str), 
        FunctionType([NoneType, NoneType], builtins_str), 
        FunctionType([NoneType, builtins_object], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_bool], builtins_str), 
        FunctionType([builtins_object, builtins_bytes], builtins_str), 
        FunctionType([builtins_object, builtins_int], builtins_str), 
        FunctionType([builtins_object, builtins_str], builtins_str), 
        FunctionType([builtins_object, builtins_range], builtins_str), 
        FunctionType([builtins_object, ellipsis], builtins_str), 
        FunctionType([builtins_object, NoneType], builtins_str), 
        FunctionType([builtins_object, builtins_object], builtins_str), 
        FunctionType([builtins_object], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range], builtins_str), 
        FunctionType([ellipsis], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([builtins_object], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "format_map",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range], builtins_str), 
        FunctionType([ellipsis], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([builtins_object], builtins_str)
    ])
)
builtins_str.add_function_member(
    "index",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str], builtins_int)
    ])
)
builtins_str.add_function_member(
    "isalnum",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isalpha",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isascii",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isdecimal",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isdigit",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isidentifier",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "islower",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isnumeric",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isprintable",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isspace",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "istitle",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "isupper",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "join",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range], builtins_str)
    ])
)
builtins_str.add_function_member(
    "ljust",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "lower",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "lstrip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "replace",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_str, builtins_bool], builtins_str), 
        FunctionType([builtins_str, builtins_str, builtins_int], builtins_str), 
        FunctionType([builtins_str, builtins_str], builtins_str), 
        FunctionType([builtins_str, builtins_str], builtins_str)
    ])
)
builtins_str.add_function_member(
    "rfind",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str], builtins_int)
    ])
)
builtins_str.add_function_member(
    "rindex",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_int), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_int), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str, builtins_bool], builtins_int), 
        FunctionType([builtins_str, builtins_int], builtins_int), 
        FunctionType([builtins_str, NoneType], builtins_int), 
        FunctionType([builtins_str], builtins_int), 
        FunctionType([builtins_str], builtins_int)
    ])
)
builtins_str.add_function_member(
    "rjust",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool, builtins_str], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int, builtins_str], builtins_str), 
        FunctionType([builtins_int], builtins_str), 
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "rstrip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "startswith",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str, builtins_bool, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_bool, builtins_int], builtins_bool), 
        FunctionType([builtins_str, builtins_bool, NoneType], builtins_bool), 
        FunctionType([builtins_str, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int, builtins_int], builtins_bool), 
        FunctionType([builtins_str, builtins_int, NoneType], builtins_bool), 
        FunctionType([builtins_str, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, NoneType, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType, NoneType], builtins_bool), 
        FunctionType([builtins_str, NoneType], builtins_bool), 
        FunctionType([builtins_str], builtins_bool), 
        FunctionType([builtins_str, builtins_bool], builtins_bool), 
        FunctionType([builtins_str, builtins_int], builtins_bool), 
        FunctionType([builtins_str, NoneType], builtins_bool), 
        FunctionType([builtins_str], builtins_bool), 
        FunctionType([builtins_str], builtins_bool)
    ])
)
builtins_str.add_function_member(
    "strip",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_str], builtins_str), 
        FunctionType([NoneType], builtins_str), 
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "swapcase",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "title",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "translate",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bytes], builtins_str), 
        FunctionType([builtins_str], builtins_str), 
        FunctionType([builtins_range], builtins_str)
    ])
)
builtins_str.add_function_member(
    "upper",
    ArrowCollectionIntrinsic([
        FunctionType([], builtins_str)
    ])
)
builtins_str.add_function_member(
    "zfill",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_str.add_function_member(
    "__getitem__",
    ArrowCollectionIntrinsic([
        FunctionType([builtins_bool], builtins_str), 
        FunctionType([builtins_int], builtins_str)
    ])
)
builtins_BaseException.add_nomial_parent(builtins_object)
builtins_Exception.add_nomial_parent(builtins_BaseException)
builtins_TypeError.add_nomial_parent(builtins_Exception)
builtins_StopAsyncIteration.add_nomial_parent(builtins_Exception)
builtins_StopIteration.add_nomial_parent(builtins_Exception)
builtins_GeneratorExit.add_nomial_parent(builtins_BaseException)
builtins_SystemExit.add_nomial_parent(builtins_BaseException)
builtins_KeyboardInterrupt.add_nomial_parent(builtins_BaseException)
builtins_ImportError.add_nomial_parent(builtins_Exception)
builtins_ModuleNotFoundError.add_nomial_parent(builtins_ImportError)
builtins_WindowsError.add_nomial_parent(builtins_Exception)
builtins_WindowsError.add_nomial_parent(builtins_Exception)
builtins_WindowsError.add_nomial_parent(builtins_Exception)
builtins_WindowsError.add_nomial_parent(builtins_Exception)
builtins_EOFError.add_nomial_parent(builtins_Exception)
builtins_RuntimeError.add_nomial_parent(builtins_Exception)
builtins_RecursionError.add_nomial_parent(builtins_RuntimeError)
builtins_NotImplementedError.add_nomial_parent(builtins_RuntimeError)
builtins_NameError.add_nomial_parent(builtins_Exception)
builtins_UnboundLocalError.add_nomial_parent(builtins_NameError)
builtins_AttributeError.add_nomial_parent(builtins_Exception)
builtins_SyntaxError.add_nomial_parent(builtins_Exception)
builtins_IndentationError.add_nomial_parent(builtins_SyntaxError)
builtins_TabError.add_nomial_parent(builtins_IndentationError)
builtins_LookupError.add_nomial_parent(builtins_Exception)
builtins_IndexError.add_nomial_parent(builtins_LookupError)
builtins_KeyError.add_nomial_parent(builtins_LookupError)
builtins_ValueError.add_nomial_parent(builtins_Exception)
builtins_UnicodeError.add_nomial_parent(builtins_ValueError)
builtins_UnicodeEncodeError.add_nomial_parent(builtins_UnicodeError)
builtins_UnicodeDecodeError.add_nomial_parent(builtins_UnicodeError)
builtins_UnicodeTranslateError.add_nomial_parent(builtins_UnicodeError)
builtins_AssertionError.add_nomial_parent(builtins_Exception)
builtins_ArithmeticError.add_nomial_parent(builtins_Exception)
builtins_FloatingPointError.add_nomial_parent(builtins_ArithmeticError)
builtins_OverflowError.add_nomial_parent(builtins_ArithmeticError)
builtins_ZeroDivisionError.add_nomial_parent(builtins_ArithmeticError)
builtins_SystemError.add_nomial_parent(builtins_Exception)
builtins_ReferenceError.add_nomial_parent(builtins_Exception)
builtins_MemoryError.add_nomial_parent(builtins_Exception)
builtins_BufferError.add_nomial_parent(builtins_Exception)
builtins_Warning.add_nomial_parent(builtins_Exception)
builtins_UserWarning.add_nomial_parent(builtins_Warning)
builtins_DeprecationWarning.add_nomial_parent(builtins_Warning)
builtins_PendingDeprecationWarning.add_nomial_parent(builtins_Warning)
builtins_SyntaxWarning.add_nomial_parent(builtins_Warning)
builtins_RuntimeWarning.add_nomial_parent(builtins_Warning)
builtins_FutureWarning.add_nomial_parent(builtins_Warning)
builtins_ImportWarning.add_nomial_parent(builtins_Warning)
builtins_UnicodeWarning.add_nomial_parent(builtins_Warning)
builtins_BytesWarning.add_nomial_parent(builtins_Warning)
builtins_ResourceWarning.add_nomial_parent(builtins_Warning)
builtins_ConnectionError.add_nomial_parent(builtins_WindowsError)
builtins_BlockingIOError.add_nomial_parent(builtins_WindowsError)
builtins_BrokenPipeError.add_nomial_parent(builtins_ConnectionError)
builtins_ChildProcessError.add_nomial_parent(builtins_WindowsError)
builtins_ConnectionAbortedError.add_nomial_parent(builtins_ConnectionError)
builtins_ConnectionRefusedError.add_nomial_parent(builtins_ConnectionError)
builtins_ConnectionResetError.add_nomial_parent(builtins_ConnectionError)
builtins_FileExistsError.add_nomial_parent(builtins_WindowsError)
builtins_FileNotFoundError.add_nomial_parent(builtins_WindowsError)
builtins_IsADirectoryError.add_nomial_parent(builtins_WindowsError)
builtins_NotADirectoryError.add_nomial_parent(builtins_WindowsError)
builtins_InterruptedError.add_nomial_parent(builtins_WindowsError)
builtins_PermissionError.add_nomial_parent(builtins_WindowsError)
builtins_ProcessLookupError.add_nomial_parent(builtins_WindowsError)
builtins_TimeoutError.add_nomial_parent(builtins_WindowsError)
