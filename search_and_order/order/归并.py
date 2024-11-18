# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 归并排序使用的是分治策略
# 属于递归算法
# 稳定算法（保持重复元素的顺序）

# 每次都将一个列表一分为二，如果列表为空或只有一个元素，则相当于是基本情况有序

# 先拆 排序 再 合并，要注意需要用额外的空间来存储切片操作后得到的两半部分


def merge_sort(a_list):
    print(f"正在拆分：{a_list}")
    # 如果还多于一个元素，则还能继续拆分
    # 否则就代表已经有序（因为最多只有一个元素了）
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half_list = a_list[:mid] # 不到mid
        right_half_list = a_list[mid:] # 从mid开始

        # 递归左
        merge_sort(left_half_list)
        # 递归右
        merge_sort(right_half_list)
        print(f"完成一次merge_sort(right_half_list):{right_half_list}，进入排序有序子列表环节")

        # 接下来将两个小的有序列表归并为一个大的有序列表
        # 归并操作不停地从有序子列表中取出最小值，放回初始列表a_list中
        i, j, k = 0, 0, 0 # k用来放回初始列表a_list
        while i < len(left_half_list) and j < len(right_half_list):
            # 合并的方法是从左右两个已经拆分的列表中，逐个对比，把较小的放到原始列表中
            if left_half_list[i] <= right_half_list[j]:
                a_list[k] = left_half_list[i]
                i = i + 1
            else:
                a_list[k] = right_half_list[j]
                j = j + 1
            k = k + 1
        # 如果某一侧的比较小，则会先用完，例如如果righthalf先用完
        # 则i会比left的长度小，此时仍需要将左侧的元素取出（直接逐个取出即可，因为在上一轮合并时已经是有序的）
        while i < len(left_half_list):
            a_list[k] = left_half_list[i]
            i = i + 1
            k = k + 1
        # 同理如果左侧的先用完，则j会比righthalf的长度小
        # 仍需将右侧的元素取出（直接逐个取出即可，因为在上一轮合并时已经是有序的）
        while j < len(right_half_list):
            a_list[k] = right_half_list[j]
            j = j + 1
            k = k + 1

    print(f"***合并:{a_list}")


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(a_list)
    # 遇到【合并】，即函数返回了一次
    """
    正在拆分：[54, 26, 93, 17, 77, 31, 44, 55, 20]
    正在拆分：[54, 26, 93, 17]
    正在拆分：[54, 26]
    正在拆分：[54]
    合并:[54]
    # 第一次从merge_sort(left_half_list)运行到merge_sort(right_half_list)
    # 所以拆分的是左侧最小的列表的右边元素
    正在拆分：[26]
    合并:[26]
    # merge_sort(right_half_list)第一次运行返回，此时lefthalf和righthalf都只有一个元素
    # 这里进行了一次左右两个Half的排序，由于左右两half都只有一个元素，排好后列表中有两个元素
    合并:[26, 54]
    
    # 这里开始拆左侧的偏右侧的子列表
    # 进入merge_sort(right_half_list)
    正在拆分：[93, 17]
    # 递归拆左边
    正在拆分：[93]
    合并:[93]
    正在拆分：[17]
    合并:[17]
    # 完成一次右侧
    合并:[17, 93]
    # 完成了最初列表的左侧排序
    合并:[17, 26, 54, 93]
    
    # 这里开始递归最初列表的右侧
    正在拆分：[77, 31, 44, 55, 20]
    正在拆分：[77, 31]
    正在拆分：[77]
    合并:[77]
    正在拆分：[31]
    合并:[31]
    # 77和31两个子列表，交换位置后合并
    合并:[31, 77]
    
    # 拆出1个元素的左和2个元素的右
    正在拆分：[44, 55, 20]
    正在拆分：[44]
    # 1个元素的优先排好顺序，在这里等待两个元素的排好合并回来后再进行对比交换
    合并:[44]
    
    正在拆分：[55, 20]
    正在拆分：[55]
    合并:[55]
    正在拆分：[20]
    合并:[20]
    # 两个元素的右侧子列表排好合并
    合并:[20, 55]
    # 递归完成一次merge_sort(right_half_list)
    # 此时开始合并[44]left和[20,55]right
    # a_list 此时[...,20]->[...,20,44]->此时标记j还小于右侧的长度，故将其剩下的元素继续取出放到列表中[...,20,44,55]
    合并:[20, 44, 55]
    # 又一次右侧的排好后，与同一层次的左侧对比排序
    合并:[20, 31, 44, 55, 77]
    # 最后将初始列表的右侧排好后，与早已排好的左侧进行对比排序
    # 完成合并后就是最后排好的列表
    合并:[17, 20, 26, 31, 44, 54, 55, 77, 93]
    """