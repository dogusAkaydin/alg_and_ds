#! /opt/local/bin/python3
def infix2postfix(infStr):

    """ Convert the postfix equivalent of an infix expresion. """

    from pythonds.basic.stack import Stack

    infExpr = infStr.split()

    operands   = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    oPar       = "("
    cPar       = ")"
    operators  = "*/+-" 
    precedence = {"*":3,"/":3,"+":2,"-":2,oPar:1} #{operator:precedence} 

    opStack = Stack()

    psfExpr = []

    for c in infExpr:

        if c in operands: # If you see a closing parenthesis ...
            psfExpr.append(c) #append it to the psf expression.
        elif c == oPar: # If you see an opening parenthesis ...
            opStack.push(c) #push it onto the the stack.
        elif c == cPar: # If you see a closing parenthesis ...
            p = opStack.pop() # ... pop the stack & append until ... 
            while p != oPar: # the corresponding opening parenthesis is popped.              
                psfExpr.append(p)
                p = opStack.pop()
        elif c in operators:
                while not opStack.isEmpty() and (precedence[opStack.peek()] >= precedence[c]):
                    p = opStack.pop()
                    psfExpr.append(p)
                opStack.push(c)
        else:
            print("error")

    while not opStack.isEmpty():
        p = opStack.pop()
        if p in operators:
            psfExpr.append(p)

    return ''.join(psfExpr)

def postfixEval(psfStr):
    """ Evaluate a postfix expression involving single-digit integers. """

    from pythonds.basic.stack import Stack

    def doMath(opnd1,opnd2,oprt):
        if oprt == '*':
            return opnd1 * opnd2
        elif oprt == '/':
            return opnd1 / opnd2
        elif oprt == '+':
            return opnd1 + opnd2
        elif oprt == '-':
            return opnd1 - opnd2
    
    operands   = "0123456789"
    operators  = "*/+-"

    opStack = Stack()

    for c in psfStr:
        if c in operands:
            opStack.push(int(c))
        if c in operators:
            opnd2 = opStack.pop()
            opnd1 = opStack.pop()
            result = doMath(opnd1,opnd2,c) 
            opStack.push(result)

    return opStack.pop()

def evalInfix(infStr):
    pass

def main():

    print(infix2postfix("A * B + C * D"))
    print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    psfExpr = infix2postfix("1 * 2 + 3 * 4")

    print(postfixEval(psfExpr))

    print(postfixEval('7 8 + 3 2 + /'))
    

if __name__ == '__main__':
    main()



