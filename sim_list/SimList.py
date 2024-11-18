# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class SimList:
    def __init__(self):
        # 无序（元素值本身）列表是元素的集合，即每一个元素都有一个相对于其他元素的位置
        self.items = []

    def add(self, item):
        self.items.append(item)

    # 假设元素已经在列表中
    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def insert(self, index, item):
        self.items.insert(index, item)

    def pop(self, pos=-1):
        return self.items.pop(pos)