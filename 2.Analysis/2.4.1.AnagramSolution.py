#! /opt/local/bin/python3


def isAnagramV1(s1,s2):

    """ Return True if s1 and s2 are anagrams 

    s1, s2: Strings of equal length.
    Book solution with O(n2) run time
    """
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def isAnagramV2(s1,s2):
    """ Return False if s2 is not an anagram of s1 

    s1, s2: Strings of equal length.

    Form a dictionary {character: count} for both strings
    If the two dictionary=ries are equal, then the two strings are anagrams.

    """
    
    d1 = {}
    for c in s1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1

    d2 = {}
    for c in s2:
        if c in d2:
            d2[c] += 1
        else:
            d2[c] = 1

    return d1 == d2


def main():

    import timeit

    s1 = "p"
    s2 = "p"


    #print(isAnagramV1(s1,s2))
    #print(isAnagramV2(s1,s2))

    for n in range(15):
        s1 = s1 + s1
        s2 = s2 + s2
        t1 = timeit.Timer(("isAnagramV1('p'+'%s'+'p','p'+'%s'+'q')" % (s1,s2)),"from __main__ import isAnagramV1")
        t2 = timeit.Timer(("isAnagramV2('p'+'%s'+'p','p'+'%s'+'q')" % (s1,s2)),"from __main__ import isAnagramV2")
        print(("Number of characters: %10d, time it took with v1: %10e, time it took with v2: %10e") % (len(s1),t1.timeit(1), t2.timeit(1)))


if __name__ == "__main__":
    main()
