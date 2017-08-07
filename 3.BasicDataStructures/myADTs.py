class Stack:

	""" My own stack implemetation. """

	def __init__(self):
		self.items = []

	def pop(self):
		return self.items.pop()

	def push(self, item):
		self.items.append(item)

	def isEmpty(self):
		return self.items == []

	def peek(self):
		return self.items[:]

	def size(self):
		return len(self.items)


