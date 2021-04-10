"""
Generation of intrinsic information from dynamically executed instances
A kind of fuzzing, maybe
"""
import builtins
import sys
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
    "__aexit__"
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
    3, 'utf-8', 'ignore'
}


def explore(callee, depth=3, add_to_roots=False):
    if depth == 0:
        try:
            result = callee()
            # print(result)
        except Exception:
            return []
        if add_to_roots:
            roots.add(result)
        if type(result) in types:
            return [type_repr.FunctionType((), types[type(result)])]
        else:
            return []
    try:
        callee(*([1] * depth))
    except TypeError as exc:
        feature = str(exc)
        if ('(%d given)' % depth) in feature or ('got %d' % depth) in feature:
            # print("No such depth", callee, depth)
            return explore(callee, depth - 1, add_to_roots)
    except Exception:
        pass
    overloads = []
    reg = dict()
    for obj in list(roots):
        if type(obj) not in types:
            print("Warning: %s not in recognized types" % obj, file=sys.stderr)
            continue
        T = types[type(obj)]
        partial = functools.partial(callee, obj)
        for overload in explore(partial, depth - 1, add_to_roots):
            args = (T,) + overload.args
            if args in reg:
                if reg[args] != overload.r:
                    print(
                        "Warning: Inconsistent return type at %s(%s)"
                        % (callee, [x.name for x in args]), file=sys.stderr
                    )
                continue
            reg[args] = overload.r
            overloads.append(type_repr.FunctionType(
                args,
                overload.r
            ))
    overloads.extend(explore(callee, depth - 1, add_to_roots))
    return overloads


for i in range(2):
    old_size = len(roots)
    for t in tqdm.tqdm(types.keys()):
        if issubclass(t, BaseException):
            continue
        ctor = intrinsic_function.ArrowCollectionIntrinsic(
            explore(t, add_to_roots=t is not complex)
        )
        if t in type_ctors:
            funcs[type_ctors[t]] = ctor
for obj in tqdm.tqdm(list(roots)):
    for attr in dir(obj):
        if attr in skip_attrs:
            continue
        attr_obj = getattr(obj, attr)
        if type(attr_obj) in types:
            types[type(obj)].members[attr] = types[type(attr_obj)]
        elif callable(attr_obj):
            collect_type = intrinsic_function.ArrowCollectionIntrinsic(
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
    ArrowCollectionIntrinsic([
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
            code.append(FUNC % (sname(t), k, ', \n'.join(sub_arrs)))
        else:
            code.append(
                '%s.members["%s"] = %s'
                % (sname(t), k, sname(t.members[k]))
            )
with open("temp/builtin_types_generated.py", "w") as fo:
    for stub in code:
        fo.write(stub)
        fo.write("\n")
