#! /opt/local/bin/python3

def revstring(sIn):
    from pythonds.basic.stack import Stack

    sIn_stack  = Stack()
    sOut = ''

    for c in sIn:
        sIn_stack.push(c)

    #for c in range(sIn_stack.size()):
    while not sIn_stack.isEmpty():
        sOut = sOut + sIn_stack.pop()

    return ''.join(sOut)

def main():
    import sys
    s = sys.argv[1]
    print(revstring(s))

if __name__ == "__main__":
    main()
