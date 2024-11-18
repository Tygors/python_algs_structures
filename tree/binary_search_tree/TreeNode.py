# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child: TreeNode = left
        self.right_child: TreeNode = right
        self.parent: TreeNode = parent

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        # 只有root的parent为None
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        # 如果修改的节点还有子节点，则需要修改该子节点的父节点为当前节点
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_successor(self) -> "TreeNode":
        # 利用二叉搜索树属性
        # 后继节点需要微大于待删除节点
        # 如果有右子节点，则一定在右子树的最小节点处
        # 如果没有右子节点，且自己就是左子节点，则只能是其父节点微大于它
        # 如果没有右子节点，且自己是右子节点，则需要再从父节点的其他子树去找

        successor: TreeNode = None
        # 1. 如果有右子节点，则后继节点就是右子树中最小的节点
        if self.right_child:
            successor = self.right_child.find_min()
        # 没有右子节点
        else:
            if self.parent:
                # 2. 如果没有右子节点，并且其本身是父节点的左子节点，那么父节点就是后继节点
                if self.is_left_child():
                    successor = self.parent

                # 3. 如果节点是父节点右子节点，并且其本身没有右子节点，那么后继节点就是除其本身外父节点的后继节点
                # 本身是右子节点
                else:
                    # 先把自己删掉
                    self.parent.right_child = None
                    # 再从除自己外的，父节点开始去找后继节点
                    successor = self.parent.find_successor()
                    # 把自己接回原来的位置
                    self.parent.right_child = self
        return successor

    def find_min(self):
        # 用来查找子树中最小的键
        # 在任意的二叉搜索树中，最小的键就是最左边的左节点
        # 沿着子树中每个节点的left_child走，直到遇到一个没有左子节点的节点
        cur = self
        while cur.left_child:
            cur = cur.left_child
        return cur

    def splice_out(self):
        # 用来将后继节点删掉，即后继节点的父节点和子节点需要妥当处理
        # 这个方法可以直接访问待拼接的节点，并进行正确的修改
        # 如果是一个叶子节点，则将后继节点自身删除
        if self.is_leaf():
            # 一般以左叶子节点出现的后继节点在右子树的最小节点处
            if self.is_left_child():
                self.parent.left_child = None
            # 以右叶子节点出现的后继节点，出现在右子树的末端的一个没有左子节点的父节点处
            else:
                self.parent.right_child = None
        # 如果并不是叶子节点，则
        # 1. 如果有左子节点，且自己本身是左节点，将左子节点作为父节点的左子节点，然后修改左子节点的父节点为后继节点本身的父节点
        elif self.has_any_children():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                # 如果后继节点本身是右节点，则将后继节点的左子节点设置为后继节点父节点的右子节点（即本身自己的位置）
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                # 如果后继节点本身是左节点，则将右子节点放到自己的位置上，即后继节点父节点的左子节点
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                # 如果后继节点本身是右节点，则将右子节点放到自己的位置，即后继节点父节点的右子节点
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            # 这里就是中序的特征，依次达到顺序遍历树的目的
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem
