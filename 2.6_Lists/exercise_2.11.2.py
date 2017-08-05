#! /opt/local/bin/python3

def picker(d,k):
    return d[k]


def main():

    import timeit

    importStatement = "from __main__ import picker;"
    
    init2           = "myKeys = list(range(nItem));"
    init3           = "myDict = {key: None for key in myKeys}"

    for nItem in [1000,10000,100000]:
        init1           = ("nItem  = %s;" % nItem)

        timePick = timeit.Timer("picker(myDict,1)", importStatement+init1+init2+init3)
        print("time to pick first out of %10d elements: %20.10f" % (nItem, timePick.timeit(number=1000)))

        timePick = timeit.Timer("picker(myDict,nItem//2)", importStatement+init1+init2+init3)
        print("time to pick mid   out of %10d elements: %20.10f" % (nItem, timePick.timeit(number=1000)))

        timePick = timeit.Timer("picker(myDict,nItem-1)", importStatement+init1+init2+init3)   
        print("time to pick last  out of %10d elements: %20.10f" % (nItem, timePick.timeit(number=1000)))



if __name__ == "__main__":
    main()

