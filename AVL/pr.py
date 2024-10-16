class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class AVL:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,node,data):
        if node == None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)

        b = self.height(node.left) - self.height(node.right)
        if b > 1 and data < node.left.data:
            return self.rRotate(node)
        if b > 1 and data >= node.left.data:
            node.left = self.lRotate(node.left)
            return self.rRotate(node)
        if b < -1 and data < node.right.data:
            node.right = self.rRotate(node.right)
            return self.lRotate(node)
        if b < -1 and data >= node.right.data:
            return self.lRotate(node)
        return node
        
    def height(self,node):
        if node == None:
            return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)

        if height_left > height_right:
            return height_left+1
        else:
            return height_right+1
        
    def rRotate(self,node):
        x = node.left
        y = x.right
        x.right = node
        node.left = y
        return x
    
    def lRotate(self,node):
        x = node.right
        y = x.left
        x.left = node
        node.right = y
        return x
    

    def postorder(self,node):
        if node != None:
            self.postorder(node.left)
            print(node.data,' ',end='')

            self.postorder(node.right)

    
def printtree90(node,level=0):
    if node != None:
        printtree90(node.right,level+1)
        print('      '*level,node.data)
        printtree90(node.left,level+1)

input_string = input("Enter some numbers : ")

bst = AVL()

for n in input_string.split():
	bst.root = bst.insert(bst.root,int(n))


printtree90(bst.root)
print("post = ",end='')
bst.postorder(bst.root)
print()
printtree90(bst.root)
