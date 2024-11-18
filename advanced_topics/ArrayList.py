# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 使用数组实现列表


class ArrayList:
    def __init__(self):
        self.size_exponent = 0
        self.max_size = 0
        self.last_index = 0
        self.my_array = []

    def append(self, val):
        if self.last_index > self.max_size - 1:
            self.__resize()
        self.my_array[self.last_index] = val
        self.last_index = self.last_index + 1

    def __resize(self):
        # 如果遇到快要越界，就扩大内存
        new_size = 2 ** self.size_exponent
        print(f"new_size = {new_size}")
        # 初始化新的列表后，将旧数据放到新列表中
        new_array = [0] * new_size
        for i in range(self.max_size):
            new_array[i] = self.my_array[i]

        self.max_size = new_size
        self.my_array = new_array
        self.size_exponent = self.size_exponent + 1

    def __getitem__(self, idx):
        if idx < self.last_index:
            return self.my_array[idx]
        raise LookupError("索引越界index out of bounds")

    def __setitem__(self, key, value):
        if key < self.last_index:
            self.my_array[key] = value
        else:
            raise LookupError("索引越界index out of bounds")

    def insert(self, idx, val):
        if self.last_index > self.max_size - 1:
            self.__resize()
        for i in range(self.last_index, idx - 1, -1):
            self.my_array[i + 1] = self.my_array[i]
        self.last_index = self.last_index + 1
        self.my_array[idx] = val