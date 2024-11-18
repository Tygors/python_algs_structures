# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 队列是先进先出FIFO的数据结构，其有一个重要变体，优先级队列
# 优先级队列也是从头部移除元素，不过元素的逻辑顺序是由优先级决定


# 优先级最高的元素在队列的最前面，优先级最低的元素在队列最后面

# 实现优先级队列的经典方法是用 二叉堆 数据结构

# 二叉堆的入队和出队 都是O(logn)

# 二叉堆由最小堆和最大堆，最大堆的最大键值在队首

"""
以下实现最小堆（队首[即列表0处]是键最小的）
"""

from typing import List


class BinaryHeap:
    # 完全二叉树可以用一个列表来表示，而不需要”列表之列表“或”节点与引用“、
    # 由于树是完全的，因此对于列表中处于位置p的节点来说，它的左子节点正好处于2p+1,同理右子节点在2p+2
    # n位置的节点，父节点为(n-1)/2
    def __init__(self):
        self._heap = []

    def is_empty(self) -> bool:
        return not bool(self._heap)

    def get_heap(self):
        return self._heap


    # 根据新元素的大小insert到正确的位置，以保持堆的结构性质
    # 如果新元素小于其父元素，则将二者交换
    def _perc_up(self, i):
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self._heap[i] < self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]

            i = parent_idx

    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    # 删除后分两步重建堆
    # 1. 取出列表的最后一个元素，将其移到根节点
    # 2. 将新的根节点沿着树推到正确的位置
    def _perc_down(self, i):
        # 每次都找到该层较小的位置
        while i * 2 + 1 < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = self._heap[sm_child], self._heap[i]

            else:
                break
            i = sm_child

    def _get_min_child(self, i):
        if i * 2 + 1 > len(self._heap) - 1:
            return i * 2 + 1
        # 比较第i个元素的左右两个子节点，返回较小那个的位置
        if self._heap[i*2+1] < self._heap[i*2+2]:
            return i*2+1
        return i*2+2

    def delete(self):
        # 删除了最小的，并且把最后一个元素放到了根节点
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # 交换完成后，弹出并返回作为删除了最小元素
        res = self._heap.pop()
        # 将根节点元素推到其对应的位置
        self._perc_down(0)
        return res

    # 构建堆(给定列表)
    def heapify(self, not_a_heap: List):
        # 列表元素赋值，不会影响原列表（对象地址不同）
        self._heap = not_a_heap[:]
        i = len(self._heap) // 2 - 1
        while i >= 0:
            print(self.get_heap())
            self._perc_down(i)
            i = i - 1


if __name__ == "__main__":
    t = BinaryHeap()
    n_a_h = [9, 6, 5, 2, 3]
    t.heapify(n_a_h)
    print(t.get_heap())
