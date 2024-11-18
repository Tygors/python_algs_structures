# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


def make_change_1(coin_value_list, change):
    # 递归找零方案，计算量很大，因为有些节点重复计算
    if change in coin_value_list:
        # 基本情况，使用一枚硬币就可以
        return 1
    # 初始化一个变量表示【最少需要】的硬币数，赋值为正无穷
    min_coins = float("inf")
    # 如果没有一个面值与需要找零金额相等，就对每一个小于找零金额的硬币进行递归调用
    for i in [c for c in coin_value_list if c <= change]:
        # 每一个当前可能消去的硬币金额，都会返回一个最小的硬币数
        num_coins = 1 + make_change_1(
            coin_value_list, change-i
        )
        min_coins = min(num_coins, min_coins)
    return min_coins


# 减少计算量的关键在于记住已有的结果，避免重复计算。
# 一种简单的做法是把最少硬币数的计算结果存储在一张表中，在计算新的最少硬币数之前，检查结果是否已在表中

# 记忆化搜索（DFS）
def make_change_2(coin_value_list, change, known_results):
    # 可以减少一些已经经过计算的中间节点结果，例如26消掉10和1后还剩下15， 26消掉515也剩下15.。。会出现多次15.而这些15仍会重复向下递归
    min_coins = change
    if change in coin_value_list:
        # 如果满足基本情况，则将结果表对应位置置为1
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        # 检查如果结果已在表中，则直接使用结果，不需要重复计算
        return known_results[change]
    else:
        # 如果结果表中还没有，则递归计算并把得到的最少硬币结果存在表中
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(
                coin_value_list,
                change - i,
                known_results
            )
            # if num_coins < min_coins:
            #     min_coins = num_coins
            min_coins = min(num_coins, min_coins)
            known_results[change] = min_coins
    return min_coins


if __name__ == "__main__":
    print(make_change_1((1, 5, 10, 25), 63))
    print(make_change_2((1, 5, 10, 25), 63,[0]*64))