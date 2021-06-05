# This is double linked list


class _Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev


class doubleLInkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addLast(self, e):
        newest = _Node(e, None, None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._prev = self._tail
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def displayRev(self):
        p = self._tail
        while p:
            print(p._element, end='-->')
            p = p._prev
        print(),

    def addFirst(self, e):
        newest = _Node(e, None, None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size

    def addAny(self, e, pos):
        newest = _Node(e, None, None)
        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1

    def rmFirst(self):
        if self.isEmpty():
            print('The linked list is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e

    def rmLast(self):
        if self.isEmpty():
            print('The list is empty')
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        return e

    def remove(self, pos):
        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i = i + 1
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        return e


doubleBlock = doubleLInkedList()
doubleBlock.addLast(3)
doubleBlock.addLast(34)
doubleBlock.addLast(123)
doubleBlock.addLast(90)
doubleBlock.display()
doubleBlock.displayRev()
doubleBlock.addFirst(21)
doubleBlock.display()
doubleBlock.addAny(12, 4)
doubleBlock.display()
v = doubleBlock.rmFirst()
doubleBlock.display()
print(v)
