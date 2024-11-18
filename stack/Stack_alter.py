# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


class Stack:
    def __init__(self):
        # 用列表来模拟栈,用列表的头部作为栈的顶端
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)