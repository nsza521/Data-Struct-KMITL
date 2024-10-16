class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right= None
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            p=self.root
            while(p!=None):
                if(data < p.data):
                    if(p.left==None):
                        p.left = Node(data)
                        break
                    p=p.left
                else:
                    if(p.right == None):
                        p.right = Node(data)
                        break
                    p=p.right
    def preOrder(self,node):
        if node == None:
            return
        print(node,end = ' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self,node):
        if node == None:
            return
        self.inOrder(node.left)
        print(node,end = ' ')
        self.inOrder(node.right)

    def postOrder(self,node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node,end = ' ')

    def bfs(self):
        p=self.root
        list_queue = [p]
        while list_queue is not None:
            if len(list_queue) == 0:
                break
            node = list_queue.pop(0)
            print(node.data)

            if node.left is not None:
                list_queue.append(node.left)

            if node.right is not None:
                list_queue.append(node.right)

            
        

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


print(' *** Binary Search Tree ***')
inp=[int(e) for e in input('Enter Input : ').split()]
t=BST()
for i in inp:
    root=t.insert(i)
print('')
print(' --- Tree traversal ---')
print('Level order : ',end='')
t.bfs()
print('')
print('Preorder : ',end='')
t.preOrder(t.root)
print('')
print('Inorder : ',end='')
t.inOrder(t.root)
print('')
print('Postorder : ',end='')
t.postOrder(t.root)
print('')

t.printTree(t.root)