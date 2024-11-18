# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 整数列表是以升序排列的有序列表
# 那么它会被写作 17, 26, 31, 54, 77, 93

"""
在有序列表中，元素的相对位置取决于它们的基本特征。它们通常
以升序或者降序排列
"""
from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        假设 item 之前不在列表中，并向其中添加 item ，
        同时保持整个列表的顺序。它接受一个元素作为参数，
        无返回值。
        """
        # 需要在已有链表中为新节点找到正确的插入位置
        current_node = self.head
        previous_node = None
        stop: bool = False

        # 先找到需要插入的位置
        while current_node != None and not stop:
            if current_node.get_data() > item:
                stop = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        # 找到插入的位置
        tmp_node = Node(item)
        # 如果需要添加的位置是第一个位置，即privious没有移动过
        # 则添加的方式与无需链表添加到链表第一个位置的方式一样
        if previous_node == None:
            tmp_node.set_next(self.head)# tmp_node.set_next(self.head)这句去掉好像也可以，next本来就是None,这里self.head一开始也是None
            # 如果previous_node为None,则为首次添加，将head 指向第一个要添加的节点
            self.head = tmp_node
        # 如果并不是第一个位置，则需要插入的位置为previous和current的中间，分为两步
        # 1. 先将新节点的next指向current
        # 2. previous的next指向新的节点
        # 有序列表中，这里的两个顺序也可以反过来，因为有辅助的两个指针，不涉及反过来后导致已有节点的丢失情况
        else:
            # tmp_node.set_next(current_node) # 注掉这条尝试反过来1.2.的顺序
            previous_node.set_next(tmp_node) # 2.
            tmp_node.set_next(current_node) #1.

    def remove(self, item):
        """
        假设 item 已经在列表中，并从其中移除 item 。
        它接受一个元素作为参数，并且修改列表
        """
        current_node = self.head
        previous_node = None
        found: bool = False

        while not found:
            if current_node.get_data() == item:
                found = True
            else:
                """必须先将 previous移动到 current 的位置，然后再移动 current"""
                # 当前节点已经判断过后，往后遍历之前
                # 用previous_node来指向当前节点
                previous_node = current_node
                # 移动当前节点为指向下一节点
                current_node = current_node.get_next()

        # 找到后，如果previous仍未空，则代表要删除是第一个元素
        if previous_node == None:
            # 直接将头节点指向第二个元素即可
            self.head = current_node.get_next()
        else:
            # 将前一个节点的next指向当前节点的下一节点，即跳过了当前节点
            previous_node.set_next(current_node.get_next())

    def search(self, item):
        """
        在列表中搜索 item 。它接受一个元素作为参数，
        并且返回布尔值。
        """
        # 如果目标元素不在列表中，可以利用元素有序排列这一特性尽早终止搜索。
        stop: bool = False
        current_node = self.head
        found = False
        while current_node != None and not found and not stop:
            if current_node.get_data() == item:
                found = True
            else:
                if current_node.get_data() > item:
                    stop = True
                else:
                    current_node = current_node.get_next()

        return found

    def is_empty(self):
        """
        检查列表是否为空。它不需要参数，
        并且返回布尔值。
        """
        return self.head == None

    def length(self):
        """
        返回列表中元素的个数。它不需要参数，
        并且返回一个整数。
        """
        current_node = self.head
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def index(self, item):
        """
        假设 item 已经在列表中，
        并返回该元素在列表中的位置。
        它接受一个元素作为参数，
        并且返回该元素的下标。
        """
        pass

    def pop(self):
        """
        假设列表不为空，并移除列表中的最后一个元素。
        它不需要参数，且会返回一个元素。
        """
        pass

    def pop(self, pos):
        """
        假设在指定位置 pos 存在元素，并移除该位置上的元素。
        它接受位置参数，且会返回一个元素。
        """
        pass

if __name__ == "__main__":
    n = OrderedList()
    n.add(2)
    print(n.length())
    n.add(3)
    n.add(5)
    n.add(4)
    print(n.length())
    pass