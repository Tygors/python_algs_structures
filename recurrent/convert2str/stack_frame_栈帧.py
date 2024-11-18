# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# convert_to_str.py中如果不拼接递归调用to_str的结果和convert_string的查找结果
# 则可以再进行递归调用之前把字符串压入栈中

from data_structure.stack import Stack

r_stack = Stack()

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        r_stack.push(convert_string[n])

    else:
        r_stack.push(convert_string[n % base])
        to_str(n // base, base)

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


if __name__ == "__main__":
    # print(r_stack.items)
    # to_str(765, 10)
    # print(r_stack.items)
    # res = []
    # for i in range(r_stack.size()):
    #     res.append(r_stack.pop())
    # print("".join(res))

    print(toStr(1453, 16))