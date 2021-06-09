# This is a double end quee where an elemnt can be remove from the back or remove from the front
# an  element can also be added from the back or added from the front


class dequee:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def EnqueeBack(self, e):
        self._data.append(e)

    def EnqueeFront(self, e):
        self._data.insert(0, e)

    def remvFront(self):
        if self.isEmpty():
            print('The double END quee is empty')
            return -1
        return self._data.pop(0)

    def removLast(self):
        if self.isEmpty():
            print('The double END  que is empty')
            return -1
        return self._data.pop()

    def first(self):
        if self.isEmpty():
            print('The double end quee is empty')
            return -1
        return self._data[0]

    def last(self):
        if self.isEmpty():
            print('The double end quee is empty')
            return -1
        return self._data[-1]


d = dequee()
d.EnqueeFront(3)
d.EnqueeFront(7)
d.EnqueeBack(8)
d.EnqueeBack(9)
print(d._data)
print('length', len(d))
