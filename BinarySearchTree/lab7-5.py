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

    def build_tree(self, postfix):
        stack = []
        for char in postfix:
            if char in '+-*/':
                node = Node(char)
                node.right = stack.pop() 
                node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(Node(char))
        self.root = stack.pop()

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def infix(self, node):
        if node is None:
            return ""
        if node.left is None and node.right is None:
            return node.data
        return f"({self.infix(node.left)}{node.data}{self.infix(node.right)})"

    def prefix(self, node):
        if node is None:
            return ""
        return f"{node.data}{self.prefix(node.left)}{self.prefix(node.right)}"

T = BST()
postfix = input('Enter Postfix : ')
T.build_tree(postfix)

print("Tree :")
T.print_tree(T.root)
print("--------------------------------------------------")

infix_expression = T.infix(T.root)
prefix_expression = T.prefix(T.root)

print(f"Infix : {infix_expression}")
print(f"Prefix : {prefix_expression}")
