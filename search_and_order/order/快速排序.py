# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 快排也采用分治策略，但不用额外的存储空间
# 首先选出一个基准值 pivot ,可以选第一个，也可以找三个，取中间（三数取中法）
# 基准值位置通常成为分割点


def quick_sort(a_list):
    # 这里0假定选取的第一个元素为基准值
    quick_sort_helper(a_list, 0, len(a_list)-1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        # split为基准值的位置
        split = partition(a_list, first, last)
        # 分别对分割后的左右两部分递归调用
        quick_sort_helper(a_list, first, split-1)
        quick_sort_helper(a_list, split+1, last)


def partition(a_list, first, last):
    pivot_val = a_list[first]
    # 划分操作首先找到两个坐标，分别位于列表剩余元素的开头和末尾
    # 划分的目的是根据待排序元素与基准值的大小，将他们放到正确的那边，并同时逐渐接近分割点
    # 到最后，两个坐标将汇聚于分割点
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        # 首先加大左标记，直到遇到一个大于基准值的元素
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        # 然后减少右标记，直到遇到一个小于基准值的元素
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        # 直到两个标记交错，则完成，此时右标记就是分割点（因为交错了，此时就是分割点的位置）
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
    # 最后再将初始的基准值位置0，和最后正确的基准值位置（右标记）进行交换，此时基准值落位，且左侧均小于基准值，右侧均大于基准值
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before:",a_list)
    quick_sort(a_list)
    print("after",a_list)