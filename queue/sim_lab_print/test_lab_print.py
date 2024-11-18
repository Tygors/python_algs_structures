# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


from data_structure.queue.Queue import Queue
from Printer import Printer
from Task import Task

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))



def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(10):
        print("高质量5张，round",i)
        simulation(3600, 5)
    for i in range(10):
        print("低质量10张，round",i)
        simulation(3600, 10)