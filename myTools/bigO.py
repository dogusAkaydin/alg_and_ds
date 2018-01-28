"""Carry-out a Big-O analysis by feeding a growing input."""

def analyse(func):
    from timeit import default_timer as timer
    import math
    timeConsumedBefore = 1
    Nbefore = 2 
    for n in range(0,100):
        N=2*Nbefore
        testList = [i for i in range(N,0,-1)]
        start=timer()
        func(testList)
        end=timer()
        timeConsumed = end-start
        timeRatio = timeConsumed/timeConsumedBefore
        workRatio  = N/Nbefore
        theoreticalTime       = N*math.log(N)
        theoreticalTimeBefore = Nbefore*math.log(Nbefore)
        theoreticalTimeRatio  = theoreticalTime/theoreticalTimeBefore
        print("Work N={0:>10d},timeConsumed={1:>10f},workRatio={2:10f},timeRatio={3:10f},theoreticalTimeRatio = {4:>10f}.".format(N,timeConsumed,workRatio,timeRatio,theoreticalTimeRatio))
        timeConsumedBefore = timeConsumed 
        Nbefore = N

