# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Graph import Graph
from data_structure.queue.Queue import Queue
from Vertex import Vertex


# 为词梯问题构建单词关系图
def build_graph(file_name):
    buckets = {}
    a_graph = Graph()
    with open(file_name, "r", encoding="utf8") as fn:
        all_words = fn.readlines()
    # 创建词桶
    for line in all_words:
        word = line.strip()
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i+1:]}"
            buckets.setdefault(bucket, set()).add(word)

    # 连接同一个桶内的不同单词
    for similar_words in buckets.values():
        for w1 in similar_words:
            # 去掉w1本身的集合
            for w2 in similar_words - {w1}:
                a_graph.add_edge(w1, w2)
    return a_graph


# 实现广度优先搜索
def dfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        cur: Vertex = vert_queue.dequeue()
        for neighbor in cur.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = cur.distance + 1
                neighbor.previous = cur
                vert_queue.enqueue(neighbor)
        cur.color = "black"


# 回溯广度优先搜索树
def traverse(starting_vertex):
    # 通过回溯previous链来打印整个词梯
    cur: Vertex = starting_vertex
    while cur:
        print(cur.key)
        cur = cur.previous

# traverse(g.get_vertex("sage"))