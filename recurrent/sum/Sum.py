# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


"""
递归三原则
阿西莫夫提出机器人三原则
所有的递归算法都要遵守三个重要的原则：
(1) 递归算法必须有【基本情况】 ；
(2) 递归算法必须改变其状态并向基本情况靠近；
(3) 递归算法必须递归地调用自己。
"""

def repeat_list_sum(n_l):
    the_sum = 0
    for num in n_l:
        the_sum += num
    return the_sum

# 基本情况是指使算法停止递归的条件，这通常是小到足以直接解决的问题。
# list_sum 算法的基本情况就是列表的长度为 1。
def list_sum(n_l):
    # 退出的条件
    if len(n_l) == 1:
        return n_l[0]
    else:
        return n_l[0] + list_sum(n_l[1:])


if __name__ == "__main__":
    num_list = [1, 3, 5, 7, 9]
    print(list_sum(num_list))
    print(repeat_list_sum(num_list))