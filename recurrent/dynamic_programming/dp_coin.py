# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


def make_change_3(coin_value_list, change, min_coins):
    # min_coins代表由每一个找零金额所需的最少硬币数构成的列表
    # 到运行结束的时候，min_coins将包含1到change的所有最优解
    # dp
    # 动态规划算法会从1分找零开始，然后系统地一直计算到所需的找零金额
    # 这样左可以保证在每一步都已经直到任何小于当前值的找零金额所需的最小硬币数
    for cents in range(change + 1):
        # 从1分开始，填充整个找零列表
        coin_count = cents
        for j in [
            c for c in coin_value_list if c <= cents
        ]:
            # 每次遍历出小于当前找零金额所有币值
            # 查表并更新当前零钱所需的硬币数
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    print(min_coins)
    return min_coins[change]


def make_change_4(
        coin_value_list,
        change,
        min_coins,
        coins_used
):
    # 增加记录所用的硬币，即不仅仅计算所需硬币数
    # 通过记录min_coins表中每一项所加的最后一枚硬币，可以扩展make_change_3
    # 如果直到上一次加的硬币数额，则可以减去其面值，从而找到表中的前一项，并通过这一项，找到更早之前所加的硬币
    for cents in range(change + 1):
        # coin_count存放了对应找零总额所需的最少硬币数
        coin_count = cents
        # 先假设new_coin为1
        new_coin = 1
        for j in [
            c for c in coin_value_list if c <= cents
        ]:
            # 每次遍历出小于当前找零金额所有币值
            if min_coins[cents - j] + 1 < coin_count:
                # 如果新遍历出来的币值经过计算后需要的硬币数小于所需最少硬币数，则更新coin_count
                coin_count = min_coins[cents - j] + 1
                # 记录最新加入的硬币面额
                new_coin = j
        # 实际就是用两个列表来记录，一个min_coins记录所需硬币数
        # coins_used记录每个change的最后一个所使用的硬币面额
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    # 传入维护好的每个change所用的最后一枚硬币面额coins_used列表
    coin = change
    while coin > 0:
        # 每次取出当前的那枚硬币面额，然后更新剩下的change,再查表找到该剩下的change所用的最后一枚硬币，直到最后一枚
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


if __name__ == "__main__":
    test_change = 63
    clist = (1, 5, 10,21, 25)
    coins_used = [0] * (test_change + 1)
    coin_count = [0]*(test_change+1)
    #print(make_change_3(clist, test_change,(test_change+1)*[0]))
    print(make_change_4(clist,test_change, coin_count,coins_used))
    print_coins(coins_used,test_change)
    print(coins_used)