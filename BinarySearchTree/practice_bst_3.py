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
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root

    def printTree(self,node, level=0):
            if node is not None:
                self.printTree(node.right, level + 1)
                print('     ' * level, node)
                self.printTree(node.left, level + 1)


def sumPath(root,value,result = 0):
        if root is None:
            return 0    
        print(root.data)
        result += root.data
        print("result = ",result)
        print("value = ",value)

        if result == value:
            return 1
        else:
            left_result = sumPath(root.left,value,result)
            right_result = sumPath(root.right,value,result)
            
        return left_result or right_result
    
            


T = BST()
lists,ans = input("Enter number / sum : ").split("/")
bstlists = lists.split()
for i in bstlists:
    root = T.insert(int(i))
x = sumPath(root,int(ans),0)
if x == 0:
    print("ANS: NO PATH")
else:
    print("ANS:",x)

T.printTree(T.root)