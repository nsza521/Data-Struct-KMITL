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

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_descendants(self, root, value):
        result = []
        target_node = self._find(root, value)
        if target_node:
            self._collect_descendants(target_node, result)
        return result

    def _find(self, node, value):
        if node is None:
            return None
        if node.data == value:
            return node
        elif value < node.data:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def _collect_descendants(self, node, result):
        if node:
            result.append(node.data)
            self._collect_descendants(node.left, result)
            self._collect_descendants(node.right, result)

T = BST()   
inp = input('Enter the BST values and search value: ')
inp, value = inp.split(",")
inp = [int(i) for i in inp.split()]
value = int(value)
for i in inp:
    T.insert(i)

descendants = T.find_descendants(T.root, value)
print("Input: root = " ,end='')
print(inp,end='')
print(f", val = {value}")
print("Output: ",end='')
print(descendants,end='')

def printTree(node, level=0):
        if node is not None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)
printTree(T.root)
