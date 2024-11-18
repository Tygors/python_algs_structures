# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class Stack:
    def __init__(self):
        # 用列表来模拟栈,用列表的尾部作为栈的顶端
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)