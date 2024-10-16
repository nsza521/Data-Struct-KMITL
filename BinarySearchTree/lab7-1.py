class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)
        return node
    # def insert(self, data):
    #     if self.root is None:
    #         self.root = Node(data)
    #     else:
    #         self.root = self._insert(self.root, data)

    # def _insert(self, node, data):
    #     if node is None:
    #         return Node(data)
    #     if data < node.data:
    #         node.left = self._insert(node.left, data)
    #     else:
    #         node.right = self._insert(node.right, data)
    #     return node

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.root = T.insert(T.root,i)
    
T.printTree(T.root)
