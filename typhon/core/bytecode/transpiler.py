# -*- coding: utf-8 -*-
"""
Transpiles py bytecode to Simple IR with abstract interpretation.
Created on Tue Aug 25 17:14:10 2020

@author: eliphat
"""
import uuid
import queue
import collections
from .. import simple_ir as sir
from . import nodes


StaticBlock = collections.namedtuple(
    "StaticBlock",
    ["opcode", "end", "stack"]
)


def clone(sb):
    return StaticBlock(sb.opcode, sb.end, sb.stack.copy())


class State:

    @staticmethod
    def from_blocks(blocks):
        s = State()
        s.blocks = blocks
        return s

    def __init__(self):
        self.blocks = [StaticBlock(-1, -1, list())]

    def copy(self):
        return State.from_blocks([clone(x) for x in self.blocks])

    def push(self, obj):
        self.blocks[-1].stack.append(obj)

    def top(self):
        return self.blocks[-1].stack[-1]

    def pop(self):
        return self.blocks[-1].stack.pop()

    def new_block(self, instr):
        self.blocks.append(StaticBlock(instr.opcode, instr.argval, list()))

    def pop_block(self):
        return self.blocks.pop()


def transpile(cfg):
    basic_blocks = []
    visited = set()
    node_to_block = dict()

    def new_basic_block():
        return sir.BasicBlock("Block_" + uuid.uuid4().hex)

    def basic_block_for(n):
        return node_to_block.get(n, new_basic_block())

    Q = queue.Queue()
    Q.put((cfg.start_node, State(), new_basic_block()))
    while not Q.empty():
        cur, state, block = Q.get()
        if cur in visited:
            continue
        basic_blocks.append(block)
        node_to_block[cur] = block
        while True:
            visited.add(cur)
            if isinstance(cur, nodes.BinaryOpNode):
                tos = state.pop()
                tos1 = state.pop()
                state.push(block.add(sir.Func(cur.op).apply([tos1, tos])))
            elif isinstance(cur, nodes.UnaryOpNode):
                tos = state.pop()
                state.push(block.add(sir.Func(cur.op).apply([tos])))
            elif isinstance(cur, nodes.StackOpNode):
                cur.handle_stack_op(state.blocks[-1].stack)
            elif isinstance(cur, nodes.ForSwitchNode):
                cond = sir.Func("_typhon_iter_is_over").apply([state.top()])
                for t in cur.nexts:
                    if isinstance(t, nodes.ForIterEndNode):
                        target_block = basic_block_for(t)
                        Q.put((t, state.copy(), target_block))
                        block.add(sir.ConditionalJump(cond, target_block))
                for t in cur.nexts:
                    if isinstance(t, nodes.ForIterNextNode):
                        target_block = basic_block_for(t)
                        Q.put((t, state.copy(), target_block))
                        block.add(sir.UnconditionalJump(target_block))
                break
            elif isinstance(cur, nodes.ForIterEndNode):
                for t in cur.nexts:
                    target_block = basic_block_for(t)
                    Q.put((t, state.copy(), target_block))
                    block.add(sir.UnconditionalJump(target_block))
                break
            elif isinstance(cur, nodes.ForIterNextNode):
                elem = sir.Func("_typhon_iter_step").apply([state.top()])
                state.push(block.add(elem))
            elif isinstance(cur, nodes.PopBlockNode):
                state.pop_block()
            elif isinstance(cur, nodes.SetupBlockNode):
                state.new_block(cur.instr)
            elif isinstance(cur, nodes.CallFunctionNode):
                arg = [state.pop() for _ in range(cur.instr.argval)][::-1]
                state.push(block.add(state.pop().apply(arg)))
            elif isinstance(cur, nodes.LoadGlobalNode):
                import builtins
                instr = cur.instr
                if hasattr(builtins, instr.argval):
                    obj = getattr(builtins, instr.argval)
                    if callable(obj):
                        state.push(sir.Func(instr.argval))
                    else:
                        raise ValueError("Globals other than functions" +
                                         "are not yet supported.")
                else:
                    import sys
                    scope = sys.modules["__main__"]
                    obj = getattr(scope, instr.argval)
                    if callable(obj):
                        state.push(sir.Func(instr.argval))
                    else:
                        raise ValueError("Globals other than functions" +
                                         "are not yet supported.")
            elif isinstance(cur, nodes.CompareNode):
                tos = state.pop()
                tos1 = state.pop()
                state.push(block.add(sir.Func(cur.op).apply([tos1, tos])))
            elif isinstance(cur, nodes.LoadConstNode):
                state.push(sir.Constant(cur.instr.argval))
            elif isinstance(cur, nodes.LoadFastNode):
                state.push(sir.Variable(cur.instr.argval))
            elif isinstance(cur, nodes.StoreFastNode):
                state.push(block.add(sir.Store(sir.Variable(cur.instr.argval),
                                               state.pop())))
            elif isinstance(cur, nodes.UnconditionalJumpNode):
                for t in cur.nexts:
                    target_block = basic_block_for(t)
                    Q.put((t, state.copy(), target_block))
                    block.add(sir.UnconditionalJump(target_block))
                break
            elif isinstance(cur, nodes.ConditionalJumpNode):
                if cur.needs_inverting:
                    state.push(sir.Func("__not__").apply([state.pop()]))
                cond = state.pop()
                for t in cur.nexts:
                    if t.instr.offset == cur.instr.argval:
                        target_block = basic_block_for(t)
                        Q.put((t, state.copy(), target_block))
                        block.add(sir.ConditionalJump(cond, target_block))
                for t in cur.nexts:
                    if t.instr.offset != cur.instr.argval:
                        target_block = basic_block_for(t)
                        Q.put((t, state.copy(), target_block))
                        block.add(sir.UnconditionalJump(target_block))
                break
            elif isinstance(cur, nodes.ReturnNode):
                block.add(sir.Return(state.pop()))
                break
            if len(cur.nexts) == 1 and len(cur.nexts[0].prevs) == 1:
                cur = cur.nexts[0]
            elif len(cur.nexts) > 1:
                raise ValueError("Invalid CFG Node: %s" % str(cur.instr))
            else:
                target_block = basic_block_for(cur.nexts[0])
                block.add(sir.UnconditionalJump(target_block))
                Q.put((cur.nexts[0], state.copy(), target_block))
                break
    return basic_blocks
