# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 冒泡排序多次遍历列表。它比较相邻的元素，将不合顺序的进行交换
# 每一轮遍历都将下一个最大值放到正确的位置上
# 从第一个位置开始，一直判断是否需要交换顺序，则本质上是找大的，并向前挪


# 把最大的元素一个一个放到列表最后的位置
def bubble_sort(a_list):
    # 给含有n个元素的列表排序，总要遍历n-1轮
    for i in range(len(a_list) - 1, 0, -1): # 不包括0
        # 每一轮遍历，都从第一个元素出发，到未被排序的最后一个元素
        for j in range(i):
            # 每次都比较当前元素和下一个元素的大小，把大的元素交换放置到后面的位置
            if a_list[j] > a_list[j + 1]:
                # temp = a_list[j]
                # a_list[j] = a_list[j + 1]
                # a_list[j + 1] = temp
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]


def short_bubble_sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        exchanges = False
        # 这个标志用来标记在遍历过程中是否已经出现过不需要交换的情况，则表明已经都有序
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                exchanges = True
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

        if not exchanges:
            break


if __name__ == "__main__":
    test_list = [3,2,1,5,4]
    print("before:",test_list)
    # bubble_sort(test_list)
    short_bubble_sort(test_list)
    print("after:", test_list)