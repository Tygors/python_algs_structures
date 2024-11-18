# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 希尔排序也称 递减增量排序
# 将列表分成多个子列表，并对每一个子列表应用插入排序

# 切分方法并不是连续切分，而是使用增量i（步长）


def shell_sort(a_list):
    sublist_cnt = len(a_list) // 2 # 商向下取整
    while sublist_cnt > 0:
        # 例如第一次是在四个子列表里分别排序
        # 第二次则是只拆分成两个子列表（步长减半）
        # 第三次就在整个列表里插入排序（因为整体已经比较有序，所以性能比普通的一次插入排序好）
        for start_pos in range(sublist_cnt):
            gap_insertion_sort(a_list, start_pos, sublist_cnt)

        print(f"size:{sublist_cnt},list:{a_list}")
        sublist_cnt = sublist_cnt//2


def gap_insertion_sort(a_list, start, gap):
    # 对子列表用插入排序
    for i in range(start+gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos-gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos-gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val

if __name__ == "__main__":
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before:", test_list)
    shell_sort(test_list)
    print("after:", test_list)
