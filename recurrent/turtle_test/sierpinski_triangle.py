# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 谢尔平斯基三角形是三路递归

# 从一个大三角形开始，通过连接每条边的中点将它分割成四个新的三角形；
# 忽略中间的三角形，利用同样的方法分割其余三个三角形

# 基本情况根据我们想要的分割次数设定。这个次数有时被称为分形图的“度”

#from turtle import *
import turtle
from time import sleep

def draw_triangle(points, color, my_turtle):
    # points是一个坐标列表
    my_turtle.fillcolor(color)
    my_turtle.up()
    # 笔先移到第一个点
    my_turtle.goto(points[0])
    # 放下笔
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1])
    my_turtle.goto(points[2])
    my_turtle.goto(points[0])
    my_turtle.end_fill()


def get_mid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


def sierpinski(points, degree, my_turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow','violet', 'orange']
    sleep(3)
    draw_triangle(points, colormap[degree], my_turtle)

    if degree > 0:
        print(f"{degree}1")
        sierpinski(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0],points[2])],
            degree - 1,
            my_turtle
        )
        print(f"{degree}2")
        sierpinski(
            [points[1], get_mid(points[1], points[2]), get_mid(points[1], points[0])],
            degree - 1,
            my_turtle
        )
        print(f"{degree}3")
        sierpinski(
            [points[2], get_mid(points[2], points[0]), get_mid(points[1], points[2])],
            degree - 1,
            my_turtle
        )
        print(f"{degree}---------")



if __name__ == "__main__":
    point_list = [(-250, -125), (0, 250), (250, -125)]
    # draw_triangle(point_list, "green", turtle)
    # 度为5
    sierpinski(point_list, 3, turtle)
    turtle.exitonclick()