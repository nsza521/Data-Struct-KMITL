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

    def insert(self, list):
        self.root = self._insert(list)
        
    
    def _insert(self,list):
        index = int(len(list) / 2)
        if len(list)==0:
            return None
        node = Node(list[index])
        temp = list.copy()
        node.left = self._insert(temp[0:index])
        node.right = self._insert(temp[index+1:])
        return node
        

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
inp = sorted(inp)
T.insert(inp)
    
T.printTree(T.root)
