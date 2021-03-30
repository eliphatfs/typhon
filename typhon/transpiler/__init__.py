# -*- coding: utf-8 -*-
import re


def sanitize(name):
    return re.sub(r'\W|^(?=\d)', '_', name)


class CommonTranspiler(object):
    def __init__(self, indent=0, indent_str="    "):
        self.indent = indent
        self.indent_str = indent_str
        self.buffer = []
        self.need_indent = False

    def to_code(self):
        return ''.join(self.buffer)

    def write(self, thing):
        if self.need_indent:
            self.buffer.append(self.indent * self.indent_str)
            self.need_indent = False
        self.buffer.append(thing)

    def newline(self):
        self.write("\n")
        self.need_indent = True


from . import func_body_transpiler, func_to_class
