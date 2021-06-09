# This is the implementation of the quee abstract data structure using the Linked list  as node instead of using the list
# we can implement a quee data strucuture using a linked list and the to be more efficient we will opt for
# inserting a  new element from the head of he linkedList since the time complexitys is 0(1)
# deleting an element from the tail of the linkedList since the time complexity is 0(1)

# First we declare a simple class Node

class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


# Here we create the quee class with all the different method for different operations

class QueeLinkedList:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

# This method return the size of the quee
    def __len__(self):
        return self._size

# This method return true or false depending if the quee is empty or not

    def isEmpty(self):
        return self._size == 0

# This method allows you add a new elemnt to the quee ADT

    def enquee(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._front = newest
            self._rear = newest
        else:
            self._rear._next = newest
            self._rear = newest
        self._size += 1

# This method allows you remove or dequee in a quee ADT

    def dequee(self):
        if self.isEmpty():
            print('The quee is empty')
            return -1
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return e

# This method return the first element of the queelinkedist

    def first(self):
        if self.isEmpty():
            print('The list is empty')
            return -1
        return self._front._element

# This method display all the different node of the queelinkedlist
    def display(self):
        p = self._front
        while p:
            print(p._element, end='<--')
            p = p._next
        print()


# lets create an obeject and try all the different method
q = QueeLinkedList()
q.enquee(23)
q.enquee(45)
q.display()
print(q.isEmpty())
q.enquee(90)
q.display()
q.dequee()
q.display()
