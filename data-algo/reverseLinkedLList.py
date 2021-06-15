

class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


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

    def reverLink(self):
        prev = None
        while self._head:
            nextNode = self._head._next
            self._head._next = prev
            prev = self._head
            self._head = nextNode
        self._head = prev


# This method traverse the linkedlist and display all the element


    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


l = LinkedList()
l.addNode(21)
l.addNode(43)
l.addNode(90)
l.addNode(34)
l.display()
l.reverLink()
l.display()
