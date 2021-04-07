from ..intrinsic_function import IntrinsicFunction
from ...type_repr import BottomType
from ...type_var import TypeVar
from ... import MemberConstraint, FuncCallConstraint


class SpecialMethodProxy(IntrinsicFunction):
    def __init__(self, signature: str, method_name: str):
        self.name = "<intrinsic %s @%d>" % (method_name, id(self))
        self.book = set()
        self.method_name = method_name
        self.signature = signature  # string, for error-reporting only

    def __call__(self, out_type_var, arg_type_vars):
        if len(arg_type_vars) < 1:
            raise TypeError(
                "%s requires at least an argument" % self.signature
            )
        arg = arg_type_vars[0]
        if isinstance(arg.T, BottomType) or (out_type_var, arg) in self.book:
            return
        self.book.add((out_type_var, arg))
        ts = arg.parent_system
        half = TypeVar("<%s>" % self.method_name)
        ts.add_var(half)
        ts.add_constraint(MemberConstraint(half, arg, self.method_name))
        ts.add_constraint(FuncCallConstraint(half, out_type_var, arg_type_vars[1:]))
