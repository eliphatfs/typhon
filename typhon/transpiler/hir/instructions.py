class HIRInstruction:
    KID = 'HI'


class HIRCodeBlock(list):
    OBJ_KID = "cb"


class HIRICallMember(HIRInstruction):
    KID = "CM"

    def __init__(self, func):
        self.func = func


class ConditionalInstruction(HIRInstruction):

    def __init__(self, block_true, block_orelse):
        self.block_true = block_true
        self.block_orelse = block_orelse


class InstructionWithIntArg(HIRInstruction):
    def __init__(self, arg):
        self.arg = arg


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
