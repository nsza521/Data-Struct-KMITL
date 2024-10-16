class TreeNode(object): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 0 # why it is 1 im debug for an hour asdasdasdsadsadsa

    def __str__(self):
        return str(self.data)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height
    
    def getHeight(self, node):
        return -1 if node is None else node.height

    def balanceValue(self):
        return self.getHeight(self.right) - self.getHeight(self.left)

class AVL_Tree(object): 
    def __init__(self):
        self.root = None

    def add(self, root, data):
        self.root, is_balanced = AVL_Tree._add(self.root, int(data))
        return self.root

    def _add(root, data):
        if root is None:
            return TreeNode(data), True

        if data < root.data:
            root.left, is_balanced = AVL_Tree._add(root.left, data)
        else:
            root.right, is_balanced = AVL_Tree._add(root.right, data)

        x = root.setHeight()
        balance = root.balanceValue()

        if balance > 1:
            print("Left Left Rotation") 
            right_balance = root.right.balanceValue()  
            if right_balance >= 0:  
                return AVL_Tree.rotateLeftChild(root), False  
            else:  
                root.right = AVL_Tree.rotateRightChild(root.right)
                return AVL_Tree.rotateLeftChild(root), False

        if balance < -1:
            print("Right Right Rotation") 
            left_balance = root.left.balanceValue()  
            if left_balance <= 0:  
                return AVL_Tree.rotateRightChild(root), False 
            else:
                root.left = AVL_Tree.rotateLeftChild(root.left)
                return AVL_Tree.rotateRightChild(root), False

        return root, True

    @staticmethod
    def rotateLeftChild(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    @staticmethod
    def rotateRightChild(root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setHeight()
        new_root.setHeight()
        return new_root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None
print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.add(root, e)
    printTree90(root)
    print("====================")
