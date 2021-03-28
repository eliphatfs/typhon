# -*- coding: utf-8 -*-
import re


def sanitize(name):
    return re.sub('\W|^(?=\d)', '_', name)


from . import func_body_transpiler
