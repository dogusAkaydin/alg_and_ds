#! /opt/local/bin/python3

def isAnagramV1(s1,s2):

    """ Return False if s2 is not an anagram of s1 

    s1, s2: Strings of equal length.

    Start by assuming s2 is an anagram of s1.
    Select one character in s1, check each character of s2
    If there is a match found, proceed with another character in s1

    If this test fails at any character, then s2 is not and anagram of s1. Return False

    If this test never fails, then s2 really is anagram of s1. Return True


    """ 

    for c1 in s1:
        checkNextInS1 = False
        for c2 in s2:
            if c2 == c1:
                checkNextInS1 = True
                break
        if not checkNextInS1:
            return False
            break

    return True






def main():

    import timeit

    s1 = "python"

    s2 = "pyhton"

    print(isAnagramV1(s1,s2))

    # for n in range(10):
    #     s1 = s1 + s1
    #     s2 = s1
    #     t1 = timeit.Timer(("isAnagramV1('%s','%s')" % (s1,s2)),"from __main__ import isAnagramV1")
    #     print(("Number of characters: %10d, time it took: %10e") % (len(s1),t1.timeit(1)))

 

if __name__ == "__main__":
    main()
