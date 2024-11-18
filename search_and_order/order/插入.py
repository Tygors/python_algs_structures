# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 插入排序在列表较低的一端维护一个有序的子列表
# 即在索引较小的一侧开始


# 一开始假设最左侧的单个元素也是有序的子列表
# 每次遍历出新的元素，则插入到左侧对应的位置
# 具体的做法是在有序子列表右侧的第一个元素作为当前元素
# 每次都移动有序子列表的最后一个元素（右移）
# 遇到小于当前元素，则不移，将当前元素插入到该位置
def insert_sort(a_list):
    # 假设第0元素是有序的
    for i in range(1, len(a_list)):
        print(a_list)
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos>0 and a_list[cur_pos-1]>cur_val:
            # 每次都右移，直到遇到不大于当前元素的，则不移
            a_list[cur_pos] = a_list[cur_pos-1]
            # 元素移动后，指针也移动
            cur_pos = cur_pos-1
        # 如果上面循环没有进入过，则当前值和位置都不变
        # 如果进入过循环，则位置cur_pos更新到需要插入的位置
        a_list[cur_pos] = cur_val


if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print("before:", test_list)
    insert_sort(test_list)
    print("after:", test_list)
