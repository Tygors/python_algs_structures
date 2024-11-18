# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 可以用解析树，来计算解析树，并返回计算结果

# 计算解析树的函数需要利用树的层次性。通过递归计算没课子树得到整棵解析树的结果


# 设计递归计算函数，从确定基本情况开始
# 针对树进行操作的递归算法，基本情况就是检查叶子节点，因为树的叶子节点必定是操作数

import operator
from data_structure.tree.node_and_references import BinaryTree

def evaluate(parse_tree: BinaryTree):
    operator_tokens = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        # 如果不是叶子节点，则递归
        fn = operator_tokens[parse_tree.get_root_val()]
        res = fn(evaluate(left_child) ,evaluate(right_child))
        print("当前计算结果为：",res)
        return res

    else:
        # 叶子节点，没有左右子节点，则直接返回叶子节点的值，即操作数
        return parse_tree.get_root_val()