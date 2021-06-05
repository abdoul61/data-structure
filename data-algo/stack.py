# This is the implementation of the stack data structure using python language
# Stack using a particular method of saving data which is LAST IN FIRST OUT or (LIFO)


class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isEmpty():
            print('Thes stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            print('The stack is empty')
            return
        return self._data[-1]


myStack = StackArray()
myStack.push(5)
myStack.push(3)
print(myStack._data)
print('the length is:', len(myStack))
print(myStack.pop())
print(myStack.isEmpty())
myStack.pop()
print(myStack.isEmpty())
print(myStack)
