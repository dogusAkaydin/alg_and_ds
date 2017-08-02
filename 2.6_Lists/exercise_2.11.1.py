#! /opt/local/bin/python3


def picker(l,p):
    return l[p]


def main():

    import timeit

    timePick = timeit.Timer("picker(myList,0)", "from __main__ import picker ; nItem=1000; myList = list(range(nItem))")
    print("time to pick first out of %10d elements: %20.10f" % (1000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,0)", "from __main__ import picker ; nItem=10000; myList = list(range(nItem))")
    print("time to pick first out of %10d elements: %20.10f" % (10000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,0)", "from __main__ import picker ; nItem=100000; myList = list(range(nItem))")
    print("time to pick first out of %10d elements: %20.10f" % (100000, timePick.timeit(number=1000)))
    
    timePick = timeit.Timer("picker(myList,nItem//2)", "from __main__ import picker ; nItem=1000; myList = list(range(nItem))")
    print("time to pick mid   out of %10d elements: %20.10f" % (1000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,nItem//2)", "from __main__ import picker ; nItem=10000; myList = list(range(nItem))")
    print("time to pick mid   out of %10d elements: %20.10f" % (10000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,nItem//2)", "from __main__ import picker ; nItem=100000; myList = list(range(nItem))")
    print("time to pick mid   out of %10d elements: %20.10f" % (100000, timePick.timeit(number=1000)))


    timePick = timeit.Timer("picker(myList,nItem-1)", "from __main__ import picker ; nItem=1000; myList = list(range(nItem))")
    print("time to pick last  out of %10d elements: %20.10f" % (1000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,nItem-1)", "from __main__ import picker ; nItem=10000; myList = list(range(nItem))")
    print("time to pick last  out of %10d elements: %20.10f" % (10000, timePick.timeit(number=1000)))

    timePick = timeit.Timer("picker(myList,nItem-1)", "from __main__ import picker ; nItem=100000; myList = list(range(nItem))")
    print("time to pick last  out of %10d elements: %20.10f" % (100000, timePick.timeit(number=1000)))





if __name__ == "__main__":
    main()

