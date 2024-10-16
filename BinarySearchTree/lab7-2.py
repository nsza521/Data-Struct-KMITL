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

    def insert(self, data, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(data)
                return
            node = self.root
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def below(self, node, value):
        result = []
        if node is not None:
            if int(node.data) < int(value):
                result.append(node.data)
            result.extend(self.below(node.left, value))
            result.extend(self.below(node.right, value))
        return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

T = BST()
inp = input('Enter Input : ')
inp, value = inp.split("|")
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
    
T.printTree(T.root)
print("--------------------------------------------------")

values_below = T.below(T.root, value)
values_below = bubble_sort(values_below)
if(not values_below):
    print(f"Below {value} : Not have")
else :
    print(f"Below {value} : {' '.join(map(str, values_below))}")
