class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class circularLinkedLIst:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addLast(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._head = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def displayList(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()

    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head

        self._head = newest
        self._size += 1

    def addELement(self, e, pos):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def remvFirst(self):
        if self.isEmpty():
            print('The circular linkedLIst is empty')
            return -1
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
            self._head = None
        return e

    def removLast(self):
        if self.isEmpty():
            print('The circular linked list is empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._tail = p
        p = p._next
        self._tail._next = self._head
        e = p._element
        self._size -= 1
        return e

    def remvNode(self, pos):
        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i = i + 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e


circularBlock = circularLinkedLIst()
circularBlock.addLast(54)
circularBlock.addLast(345)
circularBlock.addLast(21)
circularBlock.addLast(87)
circularBlock.addLast(14)
circularBlock.displayList()


v = circularBlock.removLast()
c = circularBlock.remvNode(3)
print('size', len(circularBlock))

print(v, c)
circularBlock.displayList()
