# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class Deque:
    def __init__(self):
        # 用一个list来模拟双端队列
        self.items = []

    # 判断双端队列是否为空
    def isEmpty(self):
        return self.items == []

    # 假设双端队列的后端是list的位置0处
    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)