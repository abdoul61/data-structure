# This is an implementation of the binary trees using a node technic
# There is four methods how you can traverse a trees which are predorder- traversal , inorder-traversal , post-order-traversal then the levle order traversal


class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._left = left
        self._right = right
        self._element = element


class BinaryTree:
    def __init__(self):
        self._root = None

    def makeTree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)

    def inOrderT(self, troot):
        if troot:
            self.inOrderT(troot._left)
            print(troot._element, end=' ')
            self.inOrderT(troot._right)

    def preOrderT(self, troot):
        if troot:
            print(troot._element, end=' ')
            self.preOrderT(troot._left)
            self.preOrderT(troot._right)

    def postOrderT(self, troot):
        if troot:
            self.preOrderT(troot._left)
            self.preOrderT(troot._right)
            print(troot._element, end=' ')
        print()


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.makeTree(20, a, a)
y.makeTree(30, a, a)
z.makeTree(10, x, y)

print('This is in order traversal')
z.inOrderT(z._root)
print()
print('This is a pre order traversal')
z.preOrderT(z._root)
print()
print('This is a pos ordere traversal')
z.postOrderT(z._root)
