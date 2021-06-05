# This the quee abstack data structure with all implementation of all operation (dequee and enquee)
# The quee uses the fifo structure which means first in first out


class QueeArray:

    def __init__(self):
        self._Data = []

# This method return len of the array
    def __len__(self):
        return len(self._Data)

# This method check if the array is empty and return True or False
    def isEmpty(self):
        return len(self._Data) == 0

# This method add an element or append a new alement in the end of the array
    def enquee(self, e):
        self._Data.append(e)

# This method remove and element form the beginning of the array

    def dequee(self):
        if self.isEmpty():
            print('the quee is empty')
            return -1
        return self._Data.pop(0)


# This methos return the first element of the array


    def ReturnFist(self):
        if self.isEmpty:
            print('The quee is empty')
            return -1
        return self._Data[0]


Q = QueeArray()
print(Q.isEmpty())
Q.enquee(23)
Q.enquee(12)
Q.enquee(25)
Q.enquee(89)
Q.enquee(56)
print(Q._Data)
Q.dequee()
print(Q._Data)
