# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from typing import Any
from binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):
    def change_priority(self, search_key: Any, new_priority: Any) -> None:
        key_to_move = -1
        for i, (_, key) in enumerate(self._heap):
            if key == search_key:
                key_to_move = i
                break
        if key_to_move > -1:
            self._heap[key_to_move] = (new_priority, search_key)
            self._perc_up(key_to_move)

    def __contains__(self, search_key: Any) -> bool:
        for _, key in self._heap:
            if key == search_key:
                return True

        return False