# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 简单的图片量化算法

from PIL import Image


def simple_quant(file_name):
    # 红色维度上有7个值，绿色和蓝色维度上有6个值
    im = Image.open(file_name)
    w, h = im.size
    for row in range(h):
        for col in range(w):
            r, g, b = im.getpixel((col, row))
            r = r // 36 * 36
            g = g // 42 * 42
            b = b // 42 * 42
            im.putpixel((col, row), (r, g, b))
    im.show()


if __name__ == "__main__":
    simple_quant("./图片量化对比效果/bubbles.jpg")