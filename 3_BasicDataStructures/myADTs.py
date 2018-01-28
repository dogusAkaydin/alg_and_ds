class Stack:
    """ My own stack implementation. """
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

        self.item = initData
        self.next = None

    def setNext(self, nextNode):
        self.next = nextNode

    def setData(self,item):
        self.item = item

    def getData(self):
        return self.item

    def getNext(self):
        return self.next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
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

    def index(self,item):
        """
        Return the index of the item starting from head.
        If not found, return -1
        """
        current = self.head
        count = 0
        while current is not None:
            #If item is True or False, it will be == to 1 or 0 in current.getData()
            #This is not we want, so I am adding this type checking
            if current.getData() == item and type(current.getData()) is type(item): 
                return count
            else:
                current = current.getNext()
            count += 1
        return -1

    def find(self,item):
        index = self.index(item)
        if index == -1:
            return False
        else:
            return True

    def remove(self,item):
        current = self.head
        previous = None
        while current is not None:
            if current.getData() == item and type(current.getData()) is type(item): 
                if previous is not None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                return
            else:
                previous = current
                current = current.getNext()

    def append_O_n(self,item):
        """Append item to the tail using no direct reference to the tail. O(n)"""
        current = self.head
        count = 0
        while current.getNext() is not None:
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)
        self.tail = temp

    def append_O_1(self,item):
        """Append item to the tail a direct reference to the tail. O(1)"""
        temp = Node(item)
        current = self.tail
        current.setNext(temp)
        self.tail = temp

    def append(self,item):
        """Append item using self.append_O_1"""
        self.append_O_1(item)

    def insert(self,pos,item):
        """insert item at position pos counting from the head"""
        current = self.head #head is the 0th item.
        if pos > self.size():
            print("Requested position (%d) is larger than the list size (%d)." % (pos, self.size()))
        elif pos == 0:
            self.add(item)
        else:
            #Proceeed to item at i=pos-1:
            for i in range(pos-1):
                current = current.getNext()
            #Insert the item between the items at pos-1 and pos.
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)

    def pop(self,pos=None):
        """pop the last item or the item at position pos counting from the head"""
        if pos == None:
            current = self.head
            #Proceeed to item just before the tail
            while current.getNext().getNext() is not None:
                current = current.getNext()
            current.setNext(None)
            self.tail = current
        elif pos == 0:
            removed = self.head
            self.head = removed.getNext()
        elif pos > self.size():
            print("Requested position (%d) is larger than the list size (%d)." % (pos, self.size()))
        else:
            current = self.head #head is the 0th item.
            #Proceeed to item at i=pos-1:
            for i in range(pos-1):
                current = current.getNext()
            #Insert the item between the items at pos-1 and pos.
            removed = current.getNext()
            current.setNext(removed.getNext())

    def show(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

def main():

    import timeit

    myLinkedList = LinkedList()

    myLinkedList.add(False)
    myLinkedList.add('cat')
    myLinkedList.add(1)
    myLinkedList.add(1.0)
    myLinkedList.add(True)

    # print("Find 'cat', remove 'cat', find 'cat' again." )
    # print(myLinkedList.find('cat'))
    # myLinkedList.remove('cat')
    # print(myLinkedList.find('cat'))

    # print("Find 1, remove 1, find 1 again.")
    # print(myLinkedList.find(1))
    # myLinkedList.remove(1)
    # print(myLinkedList.find(1))

    # print("Find 2, add 2, find 2 again.")
    # print(myLinkedList.find(2))
    # myLinkedList.add(2)
    # print(myLinkedList.find(2))

    # print("---")
    # myLinkedList.show()
    # print("---")

    # print("Find 3, append_O_n 3, find 3 again.")
    # print(myLinkedList.find(3))
    # myLinkedList.append_O_n(3)
    # print(myLinkedList.find(3), myLinkedList.index(3))


    # print("---")
    # myLinkedList.show()
    # print("---")  

    # print("Find 4, append_O_1 4, find 4 again.")
    # print(myLinkedList.find(4))
    # myLinkedList.append_O_1(4)
    # print(myLinkedList.find(4), myLinkedList.index(4))

    # #Testing runtime of append O(n) and O(1) methods:
    
    # nList = [2**p for p in range(21)]

    # for n in nList:
    #     setupS ='''from __main__ import LinkedList\nmyLargeLinkedList = LinkedList()\nfor i in range(%s): myLargeLinkedList.add(i)'''
    #     initS = setupS % n
    #     t_append_O_n = timeit.Timer(("myLargeLinkedList.append_O_n(1)"),(initS))
    #     print("Time it takes to append to a linked list of %10d elements using append_O_n is: %20f" % (n, t_append_O_n.timeit(number=1)))

    # for n in nList:
    #     setupS ='''from __main__ import LinkedList\nmyLargeLinkedList = LinkedList()\nfor i in range(%s): myLargeLinkedList.add(i)'''
    #     initS = setupS % n    
    #     t_append_O_1 = timeit.Timer(("myLargeLinkedList.append(1)"),(initS))
    #     print("Time it takes to append to a linked list of %10d elements using append_O_1 is: %20f" % (n, t_append_O_1.timeit(number=1)))

    # print("Show the linked list")
    # print("---")
    # myLinkedList.show()
    # print("---")

    # print("Find 5, insert it at pos=3, find it again.")
    # print(myLinkedList.find(5))
    # myLinkedList.insert(3,5)
    # print(myLinkedList.find(5), myLinkedList.index(5))

    # print("Show the linked list")
    # print("---")
    # myLinkedList.show()
    # print("---")

    # print("Find 6, insert it at pos=0, find it again.")
    # print(myLinkedList.find(6))
    # myLinkedList.insert(0,6)
    # print(myLinkedList.find(6), myLinkedList.index(6))

    print("Show the linked list")
    print("---")
    myLinkedList.show()
    print("---")

    print("pop()")
    myLinkedList.pop()

    print("Show the linked list")
    print("---")
    myLinkedList.show()
    print("---")

    print("pop(0)")
    myLinkedList.pop(0)

    print("Show the linked list")
    print("---")
    myLinkedList.show()
    print("---")

    print("pop(1)")
    myLinkedList.pop(1)

    print("Show the linked list")
    print("---")
    myLinkedList.show()
    print("---")



    return





if __name__ == '__main__':
    main()
















