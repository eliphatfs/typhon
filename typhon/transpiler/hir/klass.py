class HIRVariable:
    OBJ_KID = "v0"

    def __init__(self, name, v_type):
        self.name = name
        self.v_type = v_type


class HIRFunction:
    OBJ_KID = "fn"

    def __init__(self, name, parent_class, return_class, arg_classes, local_classes, body_block):
        self.name = name
        self.parent_class = parent_class
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
