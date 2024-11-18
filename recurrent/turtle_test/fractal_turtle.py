# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# from turtle import *
import turtle
from time import sleep
#turtle = Turtle()

def turtle_tree(branch_len, turtle):
    # 1.先向右拐到底
    # 2.尝试第一次向左画，长度小于设置的值，因此调整角度后退到上一节点（每次回退到上一节点，也就是回到上一次递归调用函数的下一条语句处）
    # 3.退到上一节点后，向左前进，然后继续向右
    # 总结：先画右子树，再画左子树
    print(f"本轮次需要操作的长度为{branch_len}")
    if branch_len > 5:
        turtle.forward(branch_len)
        #print(f"前进{branch_len}")

        turtle.right(20)
        #input("前画笔向右20")
        turtle_tree(branch_len - 15, turtle)

        turtle.left(40)
        #input("画笔向左40")
        turtle_tree(branch_len - 15, turtle)

        turtle.right(20)
        #input("后画笔向右20")
        turtle.backward(branch_len)
        #input(f"后退{branch_len}")


if __name__ == "__main__":
    turtle.left(90)
    turtle_tree(46, turtle)
    turtle.exitonclick()