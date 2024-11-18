# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Graph import Graph
from Vertex import Vertex
from typing import List



def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = row * board_size + col
            new_positions = gen_legal_moves(row, col, board_size)
            for row_2, col_2 in new_positions:
                other_node_id = row_2 * board_size + col_2
                kt_graph.add_edge(node_id, other_node_id)

    return kt_graph


def gen_legal_moves(row, col, board_size):
    """
    接受骑士在棋盘上的位置，生成8种可能的走法
    :param row: 是水平轴+1右
    :param col: 是竖直轴+1上
    :param board_size:
    :return:
    """
    new_moves = []
    move_offsets = [
        (-1, -2), # 左下下
        (-1, 2), # 左上上
        (-2, -1), # 左左下
        (-2, 1), # 左左上
        (1, -2), # 右下下
        (1, 2), # 右上上
        (2, -1), # 右右下
        (2, 1), # 右右上
    ]
    for r_offset, c_offset in move_offsets:
        if (0 <= row + r_offset < board_size and 0 <= col + c_offset < board_size):
            new_moves.append((row+r_offset,col+c_offset))
    return new_moves

def knight_tour(n, path: List, u: Vertex, limit) -> bool:
    u.color = "gray"
    path.append(u)
    if n < limit:
        neighbors: List[Vertex] = sorted(list(u.get_neighbors()))
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].color == "white":
                done = knight_tour(n+1, path, neighbors[i], limit)
            i = i + 1
        if not done:
            # 准备回溯
            path.pop()
            u.color = "white"
    else:
        done = True
    return done


def order_by_avail(n: Vertex):
    res_list = []
    for v in n.get_neighbors(): #type: Vertex
        if v.color == "white":
            c = 0
            for w in v.get_neighbors(): #type: Vertex
                if w.color == "white":
                    c = c + 1
            res_list.append((c ,v))
    res_list.sort(key = lambda x: x[0])
    return [y[1] for y in res_list]