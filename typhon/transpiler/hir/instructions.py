class HIRInstruction:
    KID = 'HI'

    def ser(self):
        return [self.KID]


class HIRCodeBlock(list):
    OBJ_KID = "cb"


class HIRDummyCodeBlock(HIRCodeBlock):
    pass


class HIRICallMember(HIRInstruction):
    KID = "CM"

    def __init__(self, func):
        self.func = func

    def ser(self):
        return [self.KID, id(self.func)]


class ConditionalInstruction(HIRInstruction):

    def __init__(self, block_true, block_orelse):
        self.block_true = block_true
        self.block_orelse = block_orelse

    def ser(self):
        return [self.KID, id(self.block_true), id(self.block_orelse)]


class InstructionWithIntArg(HIRInstruction):
    def __init__(self, arg):
        self.arg = arg

    def ser(self):
        return [self.KID, self.arg]


class HIRIIf(ConditionalInstruction):
    KID = "IF"


class HIRIWhile(ConditionalInstruction):
    KID = "WH"


class HIRILoadLocal(InstructionWithIntArg):
    KID = "LL"


class HIRIStoreLocal(InstructionWithIntArg):
    KID = "SL"


class HIRILoadArgument(InstructionWithIntArg):
    KID = "LA"


class HIRIStoreArgument(InstructionWithIntArg):
    KID = "SA"


class HIRIReturn(HIRInstruction):
    KID = "FR"


class HIRIPop(HIRInstruction):
    KID = "SP"


class HIRINewObject(HIRInstruction):
    KID = "NO"

    def __init__(self, o_class):
        self.o_class = o_class

    def ser(self):
        return [self.KID, id(self.o_class)]


class HIRIPushInt32(InstructionWithIntArg):
    KID = "I4"
