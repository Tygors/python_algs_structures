# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 为了实现无序列表，要构建链表

# 无序列表需要维持元素之间的相对位置，但并不需要在连续的内存空间中维护这些位置信息
# 必须指明列表中第一个元素的位置，指向链表第一个元素的引用称作 头
# 最后一个元素需要直到自己没有下一个元素

# 基于Node类节点集合来构建
from Node import Node

# UnorderedList类必须包含指向第一个节点的引用
# 每个列表对象都保存了指向列表头部的引用

class UnorderedList:
    def __init__(self):
        # 初始化头指向为空，即为一个空列表
        self.head = None

    def is_empty(self):
        # 检查列表的头部是否为指向None 的引用
        return self.head == None

    def add(self, item):
        """
        由于链表只提供一个入口（头部）
        因此其他所有节点都只能通过第一个节点以及 next 链接来访问
        这意味着添加新节点最简便的位置就是头部，或者说链表的起点
        """
        tmp_node = Node(item)
        """
        第 1 步，将新节点的next 引用指向当前列表中的第一个节点。
        这样一来，原来的列表就和新节点正确地链接在了一起。
        第 2 步，修改列表的头节点，使其指向新创建的节点
        """
        tmp_node.set_next(self.head)
        self.head = tmp_node

    # length 、search以及remove都基于链表遍历技术
    """
    用一个外部引用从列表的头节点开始访问。随着访问每一个节点
    将这个外部引用通过“遍历”下一个引用来指向下一个节点
    """
    def length(self):
        '''需要遍历链表并且记录访问过多少个节点。'''
        # current_node即为外部引用(只关注next，不关注数据本身)
        current_node = self.head
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def search(self, item):
        current_node = self.head
        found: bool = False

        while current_node != None and not found:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
        # try:
        #     a= current_node.get_data()
        # except Exception as e:
        #     a = -2
        # try:
        #     b=current_node.get_next().get_data()
        # except Exception as e:
        #     b = -2
        return found # ,a,b

    def remove(self, item):
        """先找到需要移除的元素，再进行移除该节点"""
        # 需要增加一个外部引用previous_node，用来标记当前节点的前一个节点
        # 由于头节点之前没有别的节点，因此 previous_node初始值是 None
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


    def append(self, item):
        new_node = Node(item)
        current_node = self.head
        previous_node = None

        while current_node.get_next() != None:
            current_node = current_node.get_next()

        if current_node.get_next() == None:
            current_node.set_next(new_node)


    def insert(self, pos, item):
        new_node = Node(item)
        current_node = self.head
        previous_node = None
        found: bool = False
        count: int = 0
        while count < pos:
            count += 1
            previous_node = current_node
            current_node = current_node.get_next()

        previous_node.set_next(new_node)
        new_node.set_next(current_node)

    def index(self, item):
        current_node = self.head
        previous_node = None
        found: bool = False
        count = -1
        if current_node == None:
            return count
        while not found:# and current_node.get_next() != None
            count += 1
            if current_node.get_next() == None:
                if current_node.get_data() != item:
                    count = -1
                else:
                    found = True
                break
            else:
                if current_node.get_data() == item:
                    found = True
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
        return count

    def pop(self, pos=-1):
        if pos == -1:
            current_node = self.head
            previous_node = None

            while current_node.get_next() != None:
                previous_node = current_node
                current_node = current_node.get_next()

            previous_node.set_next(current_node.get_next())
        else:
            current_node = self.head
            previous_node = None
            count = -1

            while current_node.get_next() != None and pos-1 > count:
                count += 1
                previous_node = current_node
                current_node = current_node.get_next()
            previous_node.set_next(current_node.get_next())
            current_node = current_node.get_next()




if __name__ == "__main__":
    # 列表类本身并不包含任何节点对象，只有指向整个链表结构中第一个节点的引用
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list.length())
    print(my_list.search(93))
    print(my_list.search(22))

    my_list.append(11)
    print(my_list.search(11))
    print(my_list.length())

    my_list.insert(3,12)
    print(my_list.search(12))
    for i in [31,77,17,93,26,54,11,12]:
        print("find:",i,my_list.index(i))
    print(my_list.length())
    my_list.pop(3)
    print(my_list.length())
    for i in [31,77,17,93,26,54,11,12,0]:
        print("i:",i)
        print("find:-",i,my_list.index(i))