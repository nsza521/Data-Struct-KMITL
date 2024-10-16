class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node


    def preOrder(self,node): 
        if not node: 
            return      
        print(node.data)
        self.preOrder(node.left) 
        self.preOrder(node.right)   



    def printBST(self,node,level = 0):
        if node != None:
            self.printBST(node.right, level + 1)
            print('     ' * level, node.data)
            self.printBST(node.left, level + 1)


tree = BST()

list_nums = ([int(item) for item in input("Enter list : ").split()])

for i in list_nums:
    tree.insert(i)

print("\nList to a height balanced BST : ")

print(tree.preOrder(tree.root))

print("\nBST model : ")

tree.printBST(tree.root)