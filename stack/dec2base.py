# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

if __name__ == "__main__":
    print(baseConverter(15,16))
    print(baseConverter(15, 8))
    print(baseConverter(256,16))
    print(baseConverter(255,16))
    print(baseConverter(65535,16))
    print(baseConverter(65536,16))