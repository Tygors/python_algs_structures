# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 当二叉搜索树不平衡时， get和put 等操作的性能可能降到O(n)
# AVL能自动维持平衡（特殊的二叉搜索树）

# AVL树映射抽象数据类型的方式于普通的二叉搜索树一样，唯一的差别是性能
# 实现AVL树时，需要记录每个节点的平衡因子，balance factor
# balance_factor = height(left_subtree) - height(right_subtree)
# 当平衡因子大于0，成为左倾，小于0，即右倾。等于0则树是平衡的，当-1、0、1时都定义为平衡树

"""
更新平衡因子是递归过程，两种基本情况
1. 递归调用抵达根节点
2. 父节点的平衡因子调整为零，如果子树的平衡因子为零，那么祖先节点的平衡因子将不会有变化
"""

from ..binary_search_tree.BinarySearchTree import BinarySearchTree
from ..binary_search_tree.TreeNode import TreeNode

class AVLTreeNode(TreeNode):
    def __init__(self, key, val, balance_factor, left=None, right=None, parent=None):
        TreeNode.__init__(self, key, val, left, right,parent)
        self.balance_factor = balance_factor


class AVLBinarySearchTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

    # 重载_put方法
    def _put(self, key, value, cur_node: AVLTreeNode):
        if key < cur_node.key:
            if cur_node.left_child:
                self._put(key, value, cur_node.left_child)
            else:
                cur_node.left_child = AVLBinarySearchTree(key, value, 0, parent=cur_node)
                self.update_balance(cur_node.left_child)

        else:
            if cur_node.right_child:
                self._put(key, value, cur_node.right_child)
            else:
                cur_node.right = AVLBinarySearchTree(key, value, 0, parent=cur_node)
                self.update_balance(cur_node.right_child)

    def update_balance(self, node: AVLTreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    # 左旋
    """
    1. 将右子节点提升为子树的根节点
    2. 将旧根节点作为新根节点的左子节点
    3. 如果新根节点已经有一个左子节点，将其作为新左子节点的右子节点
    """
    def rotate_left(self, rotation_root: AVLTreeNode):
        # 记录子树的新根节点
        new_root: AVLTreeNode = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)


    # 右旋
    """
    1. 将左子节点提升为子树得到根节点
    2. 将旧根节点作为新根节点的右子节点
    3. 如果新根节点已经有一个右子节点，将其作为新右子节点的左子节点
    """
    def rotate_right(self, rotation_root: AVLTreeNode):
        # 记录子树的新根节点
        new_root: AVLTreeNode = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)


    """
    如果子树需要左旋，首先检查右子树的平衡因子，如果右子树左倾，就对右子树做一次右旋，再围绕原节点做一次左旋
    如果子树需要右旋，首先检查左子树的平衡因子，如果左子树右倾，就对左子树做一次左旋，再围绕原节点做一次右旋
    """
    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

