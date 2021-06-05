# Here we're using the stack data structure with linked list node

class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class stackLinked:
    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def push(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.isEmpty():
            print('the stack is empty')
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isEmpty():
            print('the stack is empty')
            return -1
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


s = stackLinked()
s.push(2)
s.push(34)
s.push(90)
s.display()
e = s.pop()
print(e)
s.display()
