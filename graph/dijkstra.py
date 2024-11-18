# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from ..tree.priority_queues_with_binary_heaps.PriorityQueue import PriorityQueue
from Vertex import Vertex
from Graph import Graph


def dijkstra(graph: Graph, start: Vertex):
    pq = PriorityQueue()
    start.distance = 0
    pq.heapify([(v.distance, v) for v in graph])
    while pq:
        distance, cur_v = pq.delete()  # type: int, Vertex
        for next_v in cur_v.get_neighbors():  # type: Vertex
            new_distance = cur_v.distance + cur_v.get_neighbor(next_v)
            if new_distance < next_v.distance:
                next_v.distance = new_distance
                next_v.previous = cur_v
                pq.change_priority(next_v, new_distance)
