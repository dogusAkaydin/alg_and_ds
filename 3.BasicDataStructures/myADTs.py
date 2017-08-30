
#! /opt/local/bin/python3

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

class Node:

    def __init__(self, initData):

        self.data = initData
        self.next = None

    def setNext(self, nextNode):
        self.next = nextNode

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

        if self.head.getNext() is None:
            self.tail = self.head

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def index(self,data):
        '''
        Note how similar this is to find().
        Could the code be reused someway?
        Decorators?
        '''
        current = self.head
        count = 0

        while current is not None:
            if current.getData() == data and type(current.getData()) is type(data): 
                return count
            else:
                current = current.getNext()
            count += 1

        return -1

    def find(self,data):
        current = self.head
        count = 0
        while current is not None:
            #If data is True or False, it will be == to 1 or 0 in current.getData()
            #This is not we want, so I am adding this type checking
            if current.getData() == data and type(current.getData()) is type(data): 
                return True #Could have returned count to index.
            else:
                current = current.getNext()
            count += 1

        return False

    def remove(self,data):
        '''
        Note how similar this is to find().
        Could the code be reused someway?
        Decorators?
        '''
        current = self.head
        previous = None

        while current is not None:
            if current.getData() == data and type(current.getData()) is type(data): 
                if previous is not None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                return
            else:
                previous = current
                current = current.getNext()



#    def append(self,data):


def main():

    myLinkedList = UnorderedList()

    myLinkedList.add(False)
    myLinkedList.add('dog')
    myLinkedList.add('cat')
    #myLinkedList.add(1)
    myLinkedList.add(True)
    myLinkedList.add(5)

    #print(myLinkedList.find('cat'))
    #myLinkedList.remove('cat')
    #print(myLinkedList.find('cat'))

    print(myLinkedList.find(1))
    #myLinkedList.remove(1)
    #print(myLinkedList.find(1))
  



if __name__ == '__main__':
    main()
















