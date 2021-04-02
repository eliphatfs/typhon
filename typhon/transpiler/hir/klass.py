class HIRFunction:
    OBJ_KID = "fn"

    def __init__(self, name, return_class, arg_classes, local_classes, body_block):
        self.name = name
        self.return_class = return_class
        self.arg_classes = arg_classes
        self.local_classes = local_classes
        self.body_block = body_block


class HIRClass:
    OBJ_KID = "cs"

    def __init__(self, name):
        self.name = name
        self.funcs = list()
        self.fields = list()

    def find_sub(self, name):
        for f in self.funcs:
            if f.name == name:
                return f
        for f in self.fields:
            if f.name == name:
                return f
        raise ValueError("find_sub failed on %s for %s" % (self.name, name))
