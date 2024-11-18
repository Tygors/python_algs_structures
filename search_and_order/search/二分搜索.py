# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 二分搜索需要利用列表有序的特性

# 二分搜索从列表中间的元素开始进行比较，而不是按顺序搜索列表

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2 # 向下取整
        if a_list[min] == item:
            return True
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

# 递归版本的二分搜索
def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False

    mid = len(a_list) // 2

    if a_list[mid] == item:
        return True

    elif item < a_list[mid]:
        return binary_search_rec(a_list[:mid], item)

    else:
        return binary_search_rec(a_list[mid+1:], item)

