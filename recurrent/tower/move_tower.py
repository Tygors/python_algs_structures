# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


count = 0
def move_disk(from_pole, to_pole):
    global count
    count+=1
    #print(f"moving disk from {from_pole} to {to_pole}")


def move_tower(height, from_pole, to_pole, with_pole):
    # with_pole是中间
    if height < 1:
        # 基本情况是高度为0
        return
    # 将除了最后一个盘子以外的其他所有盘子从起点柱子移到中间柱子
    move_tower(height-1, from_pole, with_pole, to_pole)
    # 简单地将最后一个盘子移动到当前的终点柱子上
    move_disk(from_pole, to_pole)
    # 将之前的盘子从中间柱子移到终点柱子上，即将其放置在最大的盘子之上
    move_tower(height-1, with_pole, to_pole, from_pole)


if __name__ == "__main__":
    move_tower(64, "pillar1","pillar2","pillar3")
    print("total step:",count)