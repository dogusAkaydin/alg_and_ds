#! /opt/local/bin/python3

def main():
	#from myADTs import Stack
	from pythonds.basic.stack import Stack

	myStack = Stack()

	myStack.push("dog")

	myStack.push(0)

	myStack.push(True)

	print(myStack.peek())

	s=Stack()

	print(s.isEmpty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.isEmpty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())

if __name__ == "__main__" :
	main()