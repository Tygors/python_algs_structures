# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 一个简单的模式匹配器
def simple_matcher(pattern, text):
    # 记录每次尝试的起点
    start = 0
    i, j = 0, 0 # i文本的下标， j模式的下标
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            start = start + 1 # 起点向右移动
            i = start
            j = 0

        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True
    if match:
        return i - j
    else:
        return -1


def simple_matcher(pattern, text):
    log_point = 0
    i = j = 0

    while True:
        if text[i] == pattern[j]:
            j = j + 1
        else:
            j = 0
            log_point += 1
        if j == 0:
            i = log_point
        else:
            i = i + 1

        if j == len(pattern):
            return i - j
        if i == len(text):
            return -1

def mismatched_links(pattern):
    aug_pattern = "0" + pattern
    links = {1: 0}
    for k in range(2, len(aug_pattern)):
        s = links[k - 1]
        while s >= 1:
            if aug_pattern[s] == aug_pattern[k - 1]:
                break
            else:
                s = links[s]
        links[k] = s + 1
    return links

if __name__ == "__main__":
    p = "ACGACACATAGTCACTTGGCA"
    for i in range(len(p)-5+1):
        print(p[i:i+5], simple_matcher(p[i:i+5], p))
    print(simple_matcher("ab", "ccabababcab"))
    print(simple_matcher("TGGCA", p))
    assert mismatched_links("ACATA") == {
        1: 0,
        2: 1,
        3: 1,
        4: 2,
        5: 1,
    }
    print("Done")