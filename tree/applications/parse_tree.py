# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from data_structure.tree.node_and_references import BinaryTree
from data_structure.stack import Stack
from typing import List


# 四个规则
"""
1. 如果是左括号，就为当前节点添加一个左子节点，并下沉至该子节点
2. 如果是加减乘除四个符号，就将当前节点的值设为当前符号，然后为当前节点添加一个右子节点，并下沉至该子节点
3. 如果是数字，则将当前节点的值设为该数字，并返回至父节点
4. 如果是右括号，则直接返回到父节点
"""

# 解析树(解析完全括号表达式fp_exp)
def build_parse_tree(fp_exp: str):
    fp_list: List = fp_exp.split()
    # 栈结构用来追踪父节点
    p_stack: Stack = Stack()
    expr_tree = BinaryTree("")
    # 创建好空树后，第一个压栈的便是该空树
    p_stack.push(expr_tree)
    cur_tree = expr_tree

    for token in fp_list:
        # if token == "" or token == " ":
        #     break
        # el
        if token == "(":
            # 如果是左括号，则添加左子节点，并下沉至该子节点
            cur_tree.insert_left("")
            # 下沉至该子节点之前要压栈记录父节点
            p_stack.push(cur_tree)
            # 下沉至该左子节点
            cur_tree = cur_tree.get_left_child()

        elif token in ["+", "-", "*", "/"]:
            # 如果是加减乘除符号，则设置本节点的值为该符号
            cur_tree.set_root_val(token)
            # 然后添加一个右子节点
            cur_tree.insert_right("")
            # 记录父节点后，下沉至该右子节点
            p_stack.push(cur_tree)
            cur_tree = cur_tree.get_right_child()

        elif token not in "+-*/)": # token.isdigit()
            # 如果是数字，则设置本节点值为该数字，然后返回其父节点
            print(token)
            print(type(token))
            tmp = eval(token)
            print(type(tmp))
            cur_tree.set_root_val(tmp)
            parent = p_stack.pop()
            cur_tree = parent

        elif token == ")":
            # 如果是右括号，则直接返回至父节点
            cur_tree = p_stack.pop()
        else:
            raise ValueError("未知操作符unknown operator: " + token)

    return expr_tree



