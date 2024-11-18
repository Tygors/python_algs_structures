# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


import sys
from data_structure.tree.priority_queues_with_binary_heaps.PriorityQueue import PriorityQueue
from Vertex import Vertex
from Graph import Graph


def prim(graph: Graph, start: Vertex):
    pq = PriorityQueue()
    for vertex in graph:  # type: Vertex
        vertex.distance = sys.maxsize
        vertex.previous = None

    start.distance = 0
    pq.heapify(
        [(vertex.distance, vertex) for vertex in graph]
    )
    while not pq.is_empty():
        distance, cur_v = pq.delete()  # type: int, Vertex
        for next_v in cur_v.get_neighbors():  # type: Vertex
            new_distance = cur_v.get_neighbor(next_v)
            if next_v in pq and new_distance < next_v.distance:
                next_v.previous = cur_v
                next_v.distance = new_distance
                pq.change_priority(next_v, new_distance)