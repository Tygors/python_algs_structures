# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 回文Palindromic_String问题即一个字符串从前往后读和前后往前读都一样
# 例如 madam noon radar level
from Deque import Deque

# 用双端队列存入一个字符串，然后分别从前端和后端取出每个字符对比，直到只剩一个字符（奇）或没有字符（偶）

def pal_checker(chars: str) -> str:
    char_deque = Deque()

    for ch in chars:
        # 从双端队列尾部，即0处插入元素
        char_deque.addRear(ch)

    # 设置一个标记
    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.removeRear()
        last = char_deque.removeFront()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == "__main__":
    test_strings = ["madam","noon","tigers","radar","level"]
    for a_string in test_strings:
        print(f"{a_string} is a Palindromic_String:",pal_checker(a_string))