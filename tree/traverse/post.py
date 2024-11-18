# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from data_structure.tree.node_and_references import BinaryTree
import operator

def post_order(tree: BinaryTree):
    if tree:
        # 后序即先递归左，然后再递归右，最后才是root
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_val())


# 后序计算求值函数
def post_order_evaluation(tree: BinaryTree):
    operator_tokens = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    res_1 = None
    res_2 = None
    if tree:
        res_1 = post_order_evaluation(tree.get_left_child())
        res_2 = post_order_evaluation(tree.get_right_child())
        if res_1 and res_2:
            return operator_tokens[tree.get_root_val()](res_1, res_2)

        return tree.get_root_val()