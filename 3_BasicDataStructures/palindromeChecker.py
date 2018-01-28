#! /opt/local/bin/python3

from pythonds.basic.deque import Deque

def isPalindrome(s):

    strDeck = Deque()

    for c in s:
        strDeck.addRear(c)

    while strDeck.size() > 1:
        cF = strDeck.removeFront()
        cR = strDeck.removeRear()
        if cF != cR:
            return False

    return True

def main():
    sList = []
    sList.append('madam')
    sList.append('madan')
    sList.append('xyzzyx')
    sList.append('xyzxyz')

    for s in sList:
        print("Is %s a palindrome: %s" % (s, isPalindrome(s)))


if __name__ == '__main__':
    main()