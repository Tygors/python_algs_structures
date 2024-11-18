# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 用跳表skiplist实现Map类
from skip_list import SkipList


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, val):
        self.collection.insert(key, val)

    def get(self, key):
        return self.collection.search(key)
