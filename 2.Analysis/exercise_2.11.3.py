#! /opt/local/bin/python3

def delList(theList,theIndex):
    #print(len(theList))
    #print(theIndex)
    del theList[theIndex]

def delDict(theDict,theKey):
    del theDict[theKey]

def main():
    import timeit

    initStatement1L = "from __main__ import delList;"
    initStatement1D = "from __main__ import delDict;"

    initStatement3  = "L = list(range(n));"
    initStatement4  = "D = {key:None for key in L};"

    testStatement2L = "delList(L,k);"
    testStatement2D = "delDict(D,k);"


    for n in [1e3,1e6,2e6,4e6]:
        for k in [0,n//2,n-3]:

            tL = timeit.Timer(("delList(L,%d)" % k), initStatement1L+
                                                     ("n = %d;" % n)+
                                                     initStatement3)

            print("Time it takes to del element %d from a list of %d: %20f" % (k,n,tL.timeit(number=1)) )


            tD = timeit.Timer("delDict(D,%d)" % k, initStatement1D+
                                                   ("n = %d;" % n)+
                                                   initStatement3 +
                                                   initStatement4)

            print("Time it takes to del element %d from a dict of %d: %20f" % (k,n,tD.timeit(number=1)) )

            print("\n")

if __name__ == "__main__":
    main()