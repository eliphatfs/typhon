# -*- coding: utf-8 -*-
import re


def sanitize(name):
    return re.sub(r'\W|^(?=\d)', '_', name)


from . import hir
