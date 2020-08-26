# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:36:58 2020

@author: eliphat
"""
import opcode
from . import nodes


class ControlFlowGraph:

    def __init__(self, node_list):
        self.nodes = node_list
        self.start_node = node_list[0]


def create_cfg(bytecode):
    node_list = list()
    offsets_to_nodes = dict()

    def add_node(n):
        node_list.append(n)
        offsets_to_nodes[n.instr.offset] = n
        return n

    def jump_instr(ofs):
        val = offsets_to_nodes.get(ofs)
        if val is None:
            raise ValueError("Jump target %d is not start of an instruction."
                             % ofs)
        return val

    for instr in bytecode:
        if instr.opcode in nodes.bin_opnames.keys():
            add_node(nodes.BinaryOpNode(instr))
        elif instr.opcode in nodes.una_opnames.keys():
            add_node(nodes.UnaryOpNode(instr))
        elif instr.opcode in nodes.stack_ops:
            add_node(nodes.StackOpNode(instr))
        elif instr.opcode == opcode.opmap.get('FOR_ITER'):
            f_n = add_node(nodes.ForSwitchNode(instr))
            add_node(nodes.ForIterEndNode(instr))
            add_node(nodes.ForIterNextNode(instr))
            offsets_to_nodes[instr.offset] = f_n
            node_list[-3].nexts.append(node_list[-1])
            node_list[-3].nexts.append(node_list[-2])
        elif instr.opcode == opcode.opmap.get('POP_BLOCK'):
            add_node(nodes.PopBlockNode(instr))
        elif instr.opcode == opcode.opmap.get('SETUP_LOOP'):
            add_node(nodes.SetupBlockNode(instr))
        elif instr.opcode == opcode.opmap.get('CALL_FUNCTION'):
            add_node(nodes.CallFunctionNode(instr))
        elif instr.opcode == opcode.opmap.get('LOAD_GLOBAL'):
            add_node(nodes.LoadGlobalNode(instr))
        elif instr.opcode == opcode.opmap.get('COMPARE_OP'):
            add_node(nodes.CompareNode(instr))
        elif instr.opcode == opcode.opmap.get('LOAD_CONST'):
            add_node(nodes.LoadConstNode(instr))
        elif instr.opcode == opcode.opmap.get('LOAD_FAST'):
            add_node(nodes.LoadFastNode(instr))
        elif instr.opcode == opcode.opmap.get('STORE_FAST'):
            add_node(nodes.StoreFastNode(instr))
        elif instr.opcode in map(opcode.opmap.get,
                                 ('JUMP_FORWARD',
                                  'JUMP_ABSOLUTE',
                                  'CONTINUE_LOOP')):
            add_node(nodes.UnconditionalJumpNode(instr))
        elif instr.opcode in map(opcode.opmap.get,
                                 ('POP_JUMP_IF_TRUE',
                                  'POP_JUMP_IF_FALSE')):
            add_node(nodes.ConditionalJumpNode(instr))
        elif instr.opcode == opcode.opmap.get('RETURN_VALUE'):
            add_node(nodes.ReturnNode(instr))

    def check_cf_range(index, node):
        if index >= len(node_list):
            raise ValueError("Control flow goes out of range at %s."
                             % str(node.instr))

    for i in range(len(node_list)):
        node = node_list[i]
        if isinstance(node, nodes.NodeNoJump):
            check_cf_range(i + 1, node)
            node.nexts.append(node_list[i + 1])
        else:
            if isinstance(node, nodes.UnconditionalJumpNode):
                node.nexts.append(jump_instr(node.instr.argval))
            elif isinstance(node, nodes.ConditionalJumpNode):
                check_cf_range(i + 1, node)
                node.nexts.append(node_list[i + 1])
                node.nexts.append(jump_instr(node.instr.argval))
            elif isinstance(node, nodes.ForIterEndNode):
                node.nexts.append(jump_instr(node.instr.argval))
    for start in node_list:
        for end in start.nexts:
            end.prevs.append(start)
    return ControlFlowGraph(node_list)
