"""
Generation of intrinsic information from dynamically executed instances
A kind of fuzzing, maybe
"""
import builtins
import sys
import operator
import functools
import tqdm
import typhon.core.type_system.type_repr as type_repr
from typhon.core.type_system.intrinsics import intrinsic_function


skip_types = {
    # Collections
    "dict",
    "set",
    "frozenset",
    "list",
    "tuple",
    "bytearray",
    # Generators
    "filter",
    "map",
    "zip",
    "enumerate",
    "reversed",
    # User-defined class related
    "property",
    "super",
    "classmethod",
    "staticmethod",
    # Misc,
    "memoryview",
    "slice",
    "type",
    "__loader__",
}

skip_attrs = {
    "__abstractmethods__",
    "__base__",
    "__bases__",
    "__dict__",
    "__class__",
    "mro",
    "__mro__",
    "__reduce__",
    "__reduce_ex__",
    "__sizeof__",
    "__dictoffset__",
    "__flags__",
    "__module__",
    "__itemsize__",
    "__new__",
    "__init__",
    "__del__",
    "__getattr__",
    "__getattribute__",
    "__setattr__",
    "__delattr__",
    "__dir__",
    "__get__",
    "__set__",
    "__delete__",
    "__set_name__",
    "__slots__",
    "__init_subclass__",
    "__prepare__",
    "__instancecheck__",
    "__subclasscheck__",
    "__class_getitem__",
    "__call__",
    "__await__",
    "__aiter__",
    "__anext__",
    "__aenter__",
    "__aexit__",
    "format",
}


types = {
    type(None): type_repr.RecordType("NoneType", {}),
    type(...): type_repr.RecordType("ellipsis", {}),
}
type_ctors = dict()
funcs = dict()
for k, v in builtins.__dict__.items():
    if k not in skip_types and type(v) is type:
        types[v] = type_repr.RecordType("builtins." + k, {})
        type_ctors[v] = k
for k, v in builtins.__dict__.items():
    if k not in skip_types and type(v) is type:
        for sup in v.__bases__:
            if sup in types:
                types[v].add_nomial_parent(types[sup])
roots = {
    (complex, 1 + 1j)
}


def explore(callee, depth=3, add_to_roots=False, v=False):
    if depth == 0:
        try:
            if v:
                print(callee)
            result = callee()
            if v:
                print(result)
        except Exception as exc:
            if v:
                print(exc)
            return []
        if add_to_roots:
            roots.add((type(result), result))
        if type(result) in types:
            return [type_repr.FunctionType((), types[type(result)])]
        else:
            return []
    try:
        callee(*([1] * depth))
    except TypeError as exc:
        feature = str(exc)
        for d in (depth, depth + 1):
            if ('(%d given)' % d) in feature or ('got %d' % d) in feature:
                # print("No such depth", callee, depth)
                return explore(callee, depth - 1, add_to_roots, v=v)
    except Exception:
        pass
    overloads = []
    reg = dict()
    token = object()
    for _, obj in list(roots) + [(None, token)]:
        if type(obj) not in types:
            print("Warning: %s not in recognized types" % obj, file=sys.stderr)
            continue
        T = types[type(obj)]
        if token is not obj:
            partial = functools.partial(callee, obj)
        else:
            partial = callee
        for overload in explore(partial, depth - 1, add_to_roots, v=v):
            args = (T,) + overload.args if token is not obj else overload.args
            if str(args) in reg:
                if reg[str(args)] != overload.r.name:
                    print(
                        "Warning: Inconsistent return type at %s(%s)"
                        % (callee, [x.name for x in args]), file=sys.stderr
                    )
                continue
            reg[str(args)] = overload.r.name
            overloads.append(type_repr.FunctionType(
                args,
                overload.r
            ))
    return overloads


for i in range(2):
    old_size = len(roots)
    for t in tqdm.tqdm(types.keys()):
        if issubclass(t, BaseException):
            continue
        ctor = intrinsic_function.ArrowCollectionIntrinsic(
            "<ctor>",
            explore(t, add_to_roots=t is not complex)
        )
        if t in type_ctors:
            funcs[type_ctors[t]] = ctor
# print(roots)
for _, obj in tqdm.tqdm(list(roots)):
    for attr in dir(obj):
        if attr in skip_attrs:
            continue
        attr_obj = getattr(obj, attr)
        if type(attr_obj) in types:
            types[type(obj)].members[attr] = types[type(attr_obj)]
        elif callable(attr_obj):
            if attr.startswith("__i") and hasattr(obj, attr.replace("__i", "__")):
                continue
            if attr.startswith("__r") and hasattr(obj, attr.replace("__r", "__")):
                continue
            if attr.startswith("__") and hasattr(operator, attr):
                attr_obj = functools.partial(getattr(operator, attr), obj)
            collect_type = intrinsic_function.ArrowCollectionIntrinsic(
                types[type(obj)].name + "." + attr,
                explore(attr_obj, add_to_roots=False)
            )
            if len(collect_type) == 0:
                continue
            types[type(obj)].add_function_member(
                attr,
                collect_type
            )
head = """# -*- coding: utf-8 -*-
from ..intrinsic_function import ArrowCollectionIntrinsic
from ...type_repr import FunctionType, RecordType
"""
code = [head]
sname = lambda x: x.name.replace(".", "_")
for t in types.values():
    code.append('%s = RecordType("%s", {})' % (sname(t), t.name))

ARROW = "        FunctionType([%s], %s)"
FUNC = """%s.add_function_member(
    "%s",
    ArrowCollectionIntrinsic("%s", [
%s
    ])
)"""
for t in types.values():
    for b in t.nomial_parents:
        code.append(
            "%s.add_nomial_parent(%s)"
            % (sname(t), sname(b))
        )
    for k in t.members.keys():
        if isinstance(t.members[k], intrinsic_function.ArrowCollectionIntrinsic):
            sub_arrs = []
            for sub in t.members[k]:
                parms = ', '.join([sname(a) for a in sub.args])
                sub_arrs.append(ARROW % (parms, sname(sub.r)))
            code.append(FUNC % (sname(t), k, k, ', \n'.join(sub_arrs)))
        else:
            code.append(
                '%s.members["%s"] = %s'
                % (sname(t), k, sname(t.members[k]))
            )
with open("temp/builtin_types_generated.py", "w") as fo:
    for stub in code:
        fo.write(stub)
        fo.write("\n")
