# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from random import randrange
from data_structure.stack.Stack import Stack
from typing import List


class HeaderNode:
    # 只用来创建头节点实例，没有数据data
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value


class DataNode:
    _next: "DataNode"
    _down: "DataNode"

    def __init__(self, key, val):
        self._key = key
        self._data = val
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, val):
        self._down = val


class SkipList:
    _head: DataNode

    def __init__(self):
        # 刚创建时，跳表没有数据，因此没有头节点
        # 随着key-val的加入，表头指向第一个头节点
        # 通过这个头节点，既可以访问数据节点链表，也可以访问更低的层
        self._head = None

    def search(self, key):
        cur = self._head
        while cur:
            if cur.next is None:
                cur = cur.down

            else:
                if cur.next.key == key:
                    return cur.next.data
                if key < cur.next.key:
                    cur = cur.down
                else:
                    cur = cur.next
        return None

    def insert(self, key, val):
        if self._head is None:
            self._head = HeaderNode()
            tmp = DataNode(key, val)
            self._head.next = tmp
            top = tmp
            while randrange(2) == 1:
                new_head = HeaderNode()
                tmp = DataNode(key, val)
                tmp.down = top
                new_head.next = tmp
                new_head.down = self._head
                self._head = new_head
                top = tmp
        else:
            tower = Stack()
            cur = self._head
            while cur:
                if cur.next is None:
                    tower.push(cur)
                    cur = cur.down
                else:
                    if cur.next.key > key:
                        tower.push(cur)
                        cur = cur.down
                    else:
                        cur = cur.next
                lowest_level: DataNode = tower.pop()
                tmp = DataNode(key, val)
                tmp.next = lowest_level.next
                lowest_level.next = tmp
                top = tmp
                while randrange(2) == 1:
                    if tower.isEmpty():
                        new_head = HeaderNode()
                        tmp = DataNode(key, val)
                        tmp.down = top
                        new_head.next = tmp
                        new_head.down = self._head
                        self._head = new_head
                        tmp = tmp
                    else:
                        next_level: DataNode = tower.pop()
                        tmp = DataNode(key, val)
                        tmp.down = top
                        tmp.next = next_level.next
                        next_level.next = tmp
                        top = tmp

