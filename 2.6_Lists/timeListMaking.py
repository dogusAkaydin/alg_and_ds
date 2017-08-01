#! /opt/local/bin/python3

def concat(n):
    """Take a count, make a list by concatenating [i]."""
    myList = []
    for i in range(n):
        myList = myList + [i]

def append(n):
    """Take a count, make a list by using append method."""
    myList = []
    for i in range(n):
        myList.append(i)

def comprehend(n):
    """Take a count, make a list by using list comprehension."""
    myList  = [i for i in range(n)]

def convertRange(n):
    """Take a count, make a range obkect and convert it to a list."""
    myList = list(range(n))

def main():
    """Times various ways of forming a list.

    Lists are formed either by concatenating, appending, list comprehension 
    or by converting a range() object to a list. 
    """
    import timeit

    concat1000   = timeit.Timer("concat(1000)"  , "from __main__ import concat")
    concat10000  = timeit.Timer("concat(10000)" , "from __main__ import concat")
    concat100000 = timeit.Timer("concat(100000)", "from __main__ import concat")

    print("Using concatenation:")
    print (concat1000.timeit(number=1000))   #Returned 1.138596503995359
    print (concat10000.timeit(number=1000))  #Returned 114.18594056800066
#    print (concat100000.timeit(number=1000)) #Will probably return O(10,000)

    append1000   = timeit.Timer("append(1000)"  , "from __main__ import append")
    append10000  = timeit.Timer("append(10000)" , "from __main__ import append")
    append100000 = timeit.Timer("append(100000)", "from __main__ import append")

    print("Using append method:")
    print (append1000.timeit(number=1000))   #Returned 0.11153060299693607
    print (append10000.timeit(number=1000))  #Returned 0.9811982550018001
    print (append100000.timeit(number=1000)) #Returned 10.622478520002915

    comprehend1000   = timeit.Timer("comprehend(1000)"  , "from __main__ import comprehend")
    comprehend10000  = timeit.Timer("comprehend(10000)" , "from __main__ import comprehend")
    comprehend100000 = timeit.Timer("comprehend(100000)", "from __main__ import comprehend")

    print("Using list comprehension:")
    print (comprehend1000.timeit(number=1000))   #Returned 0.03252470400184393
    print (comprehend10000.timeit(number=1000))  #Returned 0.3963708600058453
    print (comprehend100000.timeit(number=1000)) #Returned 5.129970270994818

    convertRange1000   = timeit.Timer("convertRange(1000)"  , "from __main__ import convertRange")
    convertRange10000  = timeit.Timer("convertRange(10000)" , "from __main__ import convertRange")
    convertRange100000 = timeit.Timer("convertRange(100000)", "from __main__ import convertRange")

    print("Using range conversion:")
    print (convertRange1000.timeit(number=1000))   #Returned 0.017309853996266613
    print (convertRange10000.timeit(number=1000))  #Returned 0.20817322000220884
    print (convertRange100000.timeit(number=1000)) #Returned 3.231948986998759

    print("Is range coversion the fastest method? It seems so.")

if __name__ == '__main__' :
    '''This will be executed only if the module is executed directly.'''
    main()