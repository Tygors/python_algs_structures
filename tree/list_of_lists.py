# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 以列表之列表 构建二叉树


def make_binary_tree(root):
    return [root, [], []]

# 插入左子树
def insert_left(root, new_child):
    old_child = root.pop(1) # 弹出原来的左子树
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])

    else:
        root.insert(1, [new_child,[], []])

    return root

# 插入右子树
def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])

    else:
        root.insert(2, [new_child, [], []])

    return root

# 树的访问函数
def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


if __name__ == "__main__":
    a_tree = make_binary_tree(3)
    print(a_tree) # [3, [], []]
    insert_left(a_tree, 4)
    print(a_tree)# [3, [4, [], []], []]
    insert_left(a_tree, 5)
    print(a_tree) # [3, [5, [4, [], []], []], []]