#! /opt/local/bin/python3

def dec2bin(d):
	from pythonds.basic.stack import Stack

	bStack = Stack()

	while d > 0:
		bStack.push(d%2)
		d = d // 2

	b = ''
	while not bStack.isEmpty():
		b = b + str(bStack.pop())

	return b

def dec2base(dec,base):
	from pythonds.basic.stack import Stack
	digits = '0123456789ABCDEF'

	bStack = Stack()

	while dec > 0:
		bStack.push(dec%base)
		dec = dec // base

	b = ''
	while not bStack.isEmpty():
		b = b + digits[bStack.pop()]

	return b

def main():

	print(dec2bin(233))

	print(dec2base(233,2))

	print(dec2base(233,16))


if __name__ == '__main__':
	main()