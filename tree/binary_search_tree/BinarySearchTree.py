# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


"""
除了（两种从集合中获取键值对的方法）列表二分搜索和散列表，还有二叉搜索树，也是映射的一种实现
二叉搜索树的性质：小于父节点的键都在左子树中，大于父节点的键则都在右子树中。也称作二叉搜索性

"""

from TreeNode import TreeNode


# 使用【节点与引用】表示法来实现二叉搜索树
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


    """
    1. 从根节点开始搜索二叉树，比较新键与当前节点的键。如果新键更小，搜索左子树。如果新键更大，搜索右子树
    2. 当没有可供搜索的左（右）子节点时，就说明已经找到了新键的插入位置
    3. 向树中插入一个节点，做法是创建一个TreeNode对象，并将其插入到前一步发现正确的位置上
    """
    def put(self, key, value):
        # 检查是否已经有根节点
        if self.root:
            self._put(key, value, self.root)

        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, val, cur: TreeNode):
        if key < cur.key:
            if cur.left_child:
                self._put(key, val, cur.left_child)
            else:
                cur.left_child = TreeNode(key, val, parent=cur)

        else:
            if cur.right_child:
                self._put(key, val, cur.right_child)
            else:
                cur.right_child = TreeNode(key, val, parent=cur)

    # 设置__setitem__方法，重载[]运算符
    def __setitem__(self, key, value):
        self.put(key, value)

    # get方法只是递归地搜索二叉树，直到访问到不匹配的叶子节点或者找到匹配的键
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value

        return None

    def _get(self, key, cur):
        if not cur:
            return None
        if cur.key == key:
            return cur
        if key < cur.key:
            return self._get(key, cur.left_child)
        return self._get(key, cur.right_child)

    def __getitem__(self, item):
        # 返回指定键对应的值或者None
        return self.get(item)

    # 重载 in 操作，通过设置__contains__方法
    def __contains__(self, key) -> bool:
        # 检查树中是否有某个键
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError(f"抱歉，树中未找到键为{key}的节点")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError(f"抱歉，树中未找到键为{key}的节点")

    # 找到要删除的节点后，需要考虑三种情况
    # 1. 没有子节点
    # 2. 只有一个子节点
    # 3. 有两个子节点
    def _delete(self, cur: TreeNode):
        # 第1种情况，没有子节点，即为叶子节点
        if cur.is_leaf():
            if cur.is_left_child():
                cur.parent.left_child = None
            else:
                cur.parent.right_child = None
        # 第3种情况，待删除节点有两个子节点
        elif cur.has_both_children():
            # 有两个子节点，需要找到next-largest节点，即如果是小堆，当要删除5的时候，可能需要找到6 或者7这样的后继节点，然后移动到对应的位置上
            # 后继节点必定不会多于一个

            # 找到后继节点
            successor = cur.find_successor()
            # 删除后继节点
            successor.splice_out()
            # 将后继节点放到树中待删除节点的位置
            cur.key = successor.key
            cur.value = successor.value

        # 第2种情况
        else:
            # 如果只有左节点
            if cur.left_child:
                # 如果本身是一个左节点
                if cur.is_left_child():
                    cur.left_child.parent = cur.parent
                    cur.parent.left_child = cur.left_child

                # 如果本身是一个右节点
                elif cur.is_right_child():
                    cur.left_child.parent = cur.parent
                    cur.parent.right_child = cur.left_child
                # 如果本身是根节点
                else:
                    cur.replace_value(cur.left_child.key, cur.left_child.value, cur.left_child.left_child, cur.left_child.right_child)

            # 如果只有右节点
            else:
                if cur.is_left_child():
                    cur.right_child.parent = cur.parent
                    cur.parent.left_child = cur.right_child

                elif cur.is_right_child():
                    cur.right_child.parent = cur.parent
                    cur.parent.right_child = cur.right_child

                else:
                    cur.replace_value(cur.right_child.key, cur.right_child.value, cur.right_child.left_child, cur.right_child.right_child)

    def __delitem__(self, key):
        self.delete(key)

