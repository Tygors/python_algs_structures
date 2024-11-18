# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from data_structure.tree.node_and_references import BinaryTree

# 几乎不会有中序递归的存在
# 除非只是想要按顺序遍历二叉树


def in_order(tree: BinaryTree):
    if tree:
        # 中序即先递归左，再中，然后再递归右
        in_order(tree.get_left_child())
        print(tree.get_root_val())
        in_order(tree.get_right_child())


# 通过中序遍历解析树，可以还原不带括号的表达式

# 修改中序遍历算法，可以得到完全括号表达式

def print_exp(tree):
    res = ""
    if tree:
        lc = tree.get_left_child()
        rc = tree.get_right_child()
        if lc:
            res = "(" + print_exp(lc)
        else:
            res = print_exp(lc)
            
        res = res + str(tree.get_root_val())

        if rc:
            res = res + print_exp(rc) + ")"
        else:
            res = res + print_exp(rc)
    return res


if __name__ == "__main__":
    x = BinaryTree("*")
    x.insert_left("+")
    l: BinaryTree = x.get_left_child()
    l.insert_left(4)
    l.insert_right(5)
    x.insert_right(7)
    print(print_exp(x))
    from data_structure.tree.traverse.post import post_order_evaluation
    print(post_order_evaluation(x))