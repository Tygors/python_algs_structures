# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# from turtle import *

import turtle
# turtle_ins = Turtle()
# turtle_window = turtle_ins.getscreen()


def draw_spiral(turtle_ins, line_len):
    if line_len > 0:
        turtle_ins.forward(line_len)
        turtle_ins.right(90)
        draw_spiral(turtle_ins, line_len-5)

if __name__ == "__main__":
    line_length = 100
    draw_spiral(turtle, line_length)
    turtle.exitonclick()