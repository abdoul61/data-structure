# This is the double end quee while using the linkedList as structure
# we can remov an element from the  front in constant time an the from the back in linear time or O(n)
# we can add an element from the front in constant time and add an element from the back in linear time or O(n)


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class doubleEndQueeLinkedList:
    def __init__(self):
        self._front = None
        self._end = None
        self._size = 0

    def __len__(self):
        return self(self._size)

    def isEmpty(self):
        return self._size == 0

    def addFront(self, e):
        newest = _Node(e)
        if self.isEmpty():
            self._front = newest
            self._end = newest

        newest._next = self._front
        self._front = newest
        self._size += 1

    def addback(self, e):
        newest = _Node(e)
        if self.isEmpty():
            self._end = newest
            self._front = newest
        self._end._next = newest
        self._end = newest
        self._size += 1

    def removFront(self):
        if self.isEmpty():
            print('The double end que linked list is empty')
            return -1
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._end = None
        return e

    def removLast(self):
        if self.isEmpty():
            print('The double end QueeLinkedList is empty')
            return -1
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._end = p
        p = p._next
        e = p._element
        self._end._next = None
        self._size -= 1
        return e
