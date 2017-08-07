#! /opt/local/bin/python3


def isBalancedPar(s):

    """ Check if paranthesis in s are balanced """

    from pythonds.basic.stack import Stack

    myStack = Stack()

    for c in s:
        if c == '(':
            myStack.push('(')
        elif c == ')':
            try:
                myStack.pop()
            except IndexError:
                return False


    return myStack.isEmpty()

def isBalancedGen(s):

    """ Check is parantesis, brackets or braces in s are balanced """

    from pythonds.basic.stack import Stack

    myStack = Stack()
    openers = '([{<'
    closers = ')]}>'

    def matches(o,c,openers,closers):
        return openers.index(o) == closers.index(c)

    for c in s:
        if c in openers:
            myStack.push(c)
        elif c in closers:
            try:
                t = myStack.pop()
                if not matches(t,c,openers,closers):
                    print("Error: The current closer %s does not match the last opener %s" % (c,t))
                    return False
            except IndexError:
                print ("Error: Too many %s" % c)
                return False

    
    if myStack.isEmpty():
        return True
    else:
        print("Error: Too many %s" % myStack.pop())
        return False



def main():

    s1 = '())'
    print(isBalancedPar(s1))

    s2 = '{([})><'
    print(isBalancedGen(s2))


if __name__ == "__main__":
    main()
