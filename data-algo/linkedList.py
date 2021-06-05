# This  is linked list data structure  a different form of an array

# First you create a class node where you initiat what should every node have
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# Here is the class name blockchain or linkedlist for some
# this class have all the methods or function that allows you to perform different operation in the linkedlist


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

#  This method check the sizeof the linkedlist
    def __len__(self):
        return self._size

# This metho check if the linkedlist is empty
    def isEmpty(self):
        return self._size == 0

# Thid method add a new node to the linkedlist
    def addNode(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

# This method traverse the linkedlist and display all the element
    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()
# This method traverse the linkdlist and compare each element with the value e entered when call the function
# if the alue is found within the linkedlist the value of index is return whic represent the index position of the node

    def searchlink(self, e):
        p = self._head
        index = 0
        while p:
            if p._element == e:
                return index
            p = p._next
            index += 1
        return -1


# This method add a new node on the beginine of the linkedlist


    def insertNode(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        newest._next = self._head
        self._head = newest
        self._size += 1

# This method add a node in between at any particular position of the linkedlist
    def addAny(self, e, pos):
        newest = _Node(e, None)
        p = self._head
        index = 1
        while index < pos - 1:
            p = p._next
            index += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

# Tis method remove an element from the begining of the linked list
    def remFirstNode(self):
        if self.isEmpty():
            print('The linkedlist is empty')
            return -1
        e = self._head._element
        p = self._head
        self._head = p._next
        p._next = None
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e

# This method remove an element from the end of the linked list
    def remvLast(self):
        if self.isEmpty():
            print('The list is empty')
            return -1
        p = self._head
        i = 1
        while i < len(self)-1:
            p = p._next
            i = i + 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        return e

# This method remove an element from anywhere in between the linkedlist
    def remNode(self, pos):
        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i = i+1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e


blockchain = LinkedList()
blockchain.addNode(7)
blockchain.addNode(4)
blockchain.addNode(8)
blockchain.display()
blockchain.insertNode(10)
blockchain.display()
blockchain.insertNode(24)
blockchain.addNode(26)
blockchain.addAny(40, 4)
blockchain.display()
e = blockchain.remFirstNode()
blockchain.display()
L = blockchain.remvLast()
blockchain.display()
v = len(blockchain)
print(v)
print(e, L)
