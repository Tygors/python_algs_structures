# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Stack import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        print("True")
        return True
    else:
        print("False")
        return False


if __name__ == "__main__":
    parChecker("(()()()())")
    parChecker("()))")
    parChecker("(()((())()))")
    parChecker("(()()(()")
