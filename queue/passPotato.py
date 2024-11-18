# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from Queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    print("---start---")
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        print(simqueue.dequeue(),"out")
    print("---end---")
    return simqueue.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], \
              7))
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 17))
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 1))