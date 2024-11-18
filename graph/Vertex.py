# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.distance = sys.maxsize
        self.previous = None
        self.color = "white"
        self.discovery_time = 0
        self.closing_time = 0

    def get_neighbor(self, other: "Vertex"):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other: "Vertex", weight=0):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return f"{self.key} connected to : {[x.key for x in self.neighbors]}"

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]