class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(data)
                return
            node = self.root
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.append(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.append(data, node.right)

    def find(self, data, node):
        if node is None:
            return None
        if node.data == data:
            return node
        left_result = self.find(data, node.left)
        if left_result:
            return left_result
        return self.find(data, node.right)
    
    def cut(self, data):
        parent, node_to_cut = self._find_parent(data, self.root, None)
        if node_to_cut:
            if node_to_cut.right:
                if parent:
                    if parent.left == node_to_cut:
                        parent.left.right = None
                    else:
                        parent.right.right = None
                else:
                    self.root.right = None
            elif node_to_cut.left:
                if parent:
                    if parent.left == node_to_cut:
                        parent.left.left = None
                    else:
                        parent.right.left = None
                else:
                    self.root.left = None
            else:
                print("Not thing change")
        else:
            print("Node not found")

    def _find_parent(self, data, node, parent):
        if node is None:
            return (None, None)
        if node.data == data:
            return (parent, node)
        left_result = self._find_parent(data, node.left, node)
        if left_result[1]:
            return left_result
        return self._find_parent(data, node.right, node)

    def preorder(self, node, stop):
        if node:
            if node.data > stop:
                    print(node.data + ' ', end='')
            else:
                    ascii_value = [ord(char) for char in node.data]
                    print(''.join(map(str, ascii_value)) + ' ', end='')
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node, stop):
        if node:
            self.inorder(node.left, stop)
            if node.data > stop:
                print(node.data + ' ', end='')
            else:
                ascii_value = [ord(char) for char in node.data]
                print(''.join(map(str, ascii_value)) + ' ', end='')
            self.inorder(node.right, stop)

    def postorder(self, node, stop):
        if node:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            if node.data > stop:
                print(node.data + ' ', end='')
            else:
                ascii_value = [ord(char) for char in node.data]
                print(''.join(map(str, ascii_value)) + ' ', end='')

    
    def printMirrorTree(self,node, level=0):
        if node:
            self.printMirrorTree(node.left, level + 1)
            print('     ' * level, node)
            self.printMirrorTree(node.right, level + 1)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def is_string(self, data):
        return isinstance(data, str) and len(data) > 1
    
    def is_some_ascii_lower(self, data, stop):
        return any(char > stop for char in data)


T = BST() 
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
print("FIrst look of this plum tree")
first = first.split()
for i in first:
    T.append(i)
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)
