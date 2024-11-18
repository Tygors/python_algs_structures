# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 选择排序在冒牌排序的基础上做了改进，每次遍历列表时只做一次交换


def selection_sort(a_list):
    for i in range(len(a_list)-1, -1, -1):
        # 每次遍历，都从0处开始找到当前的最后一个元素
        # 只交换一次最大的放最后
        # 假设当前最大的元素位于最后一个元素位置
        max_pos = i
        for pos in range(i):
            if a_list[pos] > a_list[max_pos]:
                max_pos = pos
        if max_pos != i:
            a_list[max_pos], a_list[i] = a_list[i], a_list[max_pos]


if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print("before:", test_list)
    selection_sort(test_list)
    print("after:", test_list)
