# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None


    def insert_left(self, new_node):
        # 如果原来的对象存在左节点，则需要将原来的左节点作为新左节点的左节点
        # 如果原对象不存在左节点，则直接将新节点作为左节点即可
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    # 插入右节点
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    # 二叉树的访问函数
    def get_root_val(self):
        return self.key

    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child