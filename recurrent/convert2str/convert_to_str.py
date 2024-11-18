# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


"""
整个算法包含三个组成部分：
(1) 将原来的整数分成一系列仅有单数位的数；（小于基数即为单数位）
(2) 通过查表将单数位的数转换成字符串；
(3) 连接得到的字符串，从而形成结果。
"""

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    # 基本情况是 剩下的数字比基数要 小（即n小于进制基数）
    if n < base:
        # 如果已经满足基本情况，则停止递归，并查表返回字符
        return convert_string[n]

    else:
        # 通过递归调用以及除法来分解问题
        return to_str(n//base, base) + convert_string[n%base]


if __name__ == "__main__":
    print(to_str(765, 10))
    print(to_str(10,2))
    print(to_str(256, 16))
    print(to_str(255, 16))
