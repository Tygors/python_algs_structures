# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

if __name__ == "__main__":
    print(divideBy2(15))
    print(divideBy2(256))
    print(divideBy2(255))
    print(divideBy2(65535))
    print(divideBy2(65536))