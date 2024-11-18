# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 存储于列表等集合中得到数据项彼此存在线性或顺序的关系
# 每个数据项都有一个相对于其他数据项的位置，其实就是下标

# 顺序搜索沿着下标顺序逐个查看，找到元素或达到列表末尾


# 无序（元素值）列表的顺序搜索
def sequential_search(a_list, item) -> bool:
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True

        pos += 1

    return False

# 有序列表的顺序搜索
# 如果不存在元素，则效率会提高，因为可能在列表中间就被发现
def ordered_sequential_search(a_list, item):
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        # 如果上一个判断不等于且到下面这一条已经大于，则表示不存在
        if a_list[pos] > item:
            return False
        pos += 1
    return False