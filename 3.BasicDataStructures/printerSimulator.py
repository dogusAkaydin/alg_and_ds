#! /opt/local/bin/python3

from pythonds.basic.queue import Queue
from random import randint

class Printer:

    def __init__(self, ppm):
        self.ppm = ppm
        self.task = None
        self.timeRemaining = 0

    def isBusy(self):
        if self.task == None:
            return False
        else:
            return True

    def processTask(self,task):
        if self.task == None:
            self.task = task
            self.timeRemaining = 60*(self.task.pageCount/self.ppm)

    def tick(self):
        self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.task = None


class Task:

    def __init__(self,initTime):
        self.initTime = initTime
        self.pageCount = randint(1,20)

    def pageCount(self):
        return self.pageCount
        
def simulate(T,ppm):

    printQueue = Queue()
    labPrinter = Printer(ppm)
    waitTimes  = []

    for t in range(T):

        if isNewTask():
            printQueue.enqueue(Task(t))

        if (not labPrinter.isBusy()) and (not printQueue.isEmpty()):
            currentTask = printQueue.dequeue()
            labPrinter.processTask(currentTask)
            waitTimes.append(t-currentTask.initTime)

        labPrinter.tick()


    print("Average wait time = %d, jobs not done = %d" % (sum(waitTimes)/len(waitTimes), printQueue.size()))


def isNewTask():

    r = randint(1,180)
    if r == 180:
        return True
    else:
        return False

def main():

    T = 3600
    ppm = 1
    print("Now at %d ppm" % ppm)
    for i in range(10):
        simulate(T,ppm)

    ppm = 20
    print("Now at %d ppm" % ppm)
    for i in range(10):
        simulate(T,ppm)

if __name__ == '__main__':
    main()