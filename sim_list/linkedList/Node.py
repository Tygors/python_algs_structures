# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# node节点是构建链表的基本数据结构
# 至少包含列表元素（数据变量）和指向下一个节点的引用，指向None代表后面没有元素

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None # 初始值都设置为将节点接地

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

