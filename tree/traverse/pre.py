# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from data_structure.tree.node_and_references import BinaryTree


def pre_order(tree: BinaryTree):
    if tree:
        # 前序即先拿到root，再递归左右
        print(tree.get_root_val())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())



"""
def pre_order(self):
    # 如果是作为内部方法，则必须要检查左右子节点是否存在，然后再向下递归
    print(self.key. end=' ')
    if self.left_child:
        self.left_child.pre_order()
        
    if self.right_child:
        self.right_child.pre_order()
"""