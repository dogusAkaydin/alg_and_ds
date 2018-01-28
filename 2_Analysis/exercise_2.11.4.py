#! /opt/local/bin/python3

def kthMinNlogN(theList,theIndex):
    return sorted(theList)[theIndex-1] #Sorting is O(NlogN)

def main():
    import random
    #import numpy.random as nprnd
    #nprnd.randint(1000, size=10000)

    N = 10000
    k = 10

    #L = [random.randrange(-1e6,1e6+1) for i in range(N)] 
    #right end is not included in randrange, so the selection 
    #is from [-1e6 to 1e6+1) = [-1e6 to 1e6].  Not [-1e6 to 1e6+1]

    L = [random.randint(-1e6,1e6) for i in range(N)] # endpoints are included in randint.

    print(sorted(L)[0:k]) #Indexing a list is O(1)
    #Resultant runtime is O(1)*O(NlogN)

    value = kthMinNlogN(L,k)

    print(value)

if __name__ == "__main__":
    """Gets executed when executed"""
    main()