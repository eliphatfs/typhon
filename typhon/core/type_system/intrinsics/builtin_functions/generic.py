from . import add_intrinsic
from .special_method_proxy import SpecialMethodProxy


add_intrinsic("next", SpecialMethodProxy("next(iterator)", "__next__"))
