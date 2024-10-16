class AVLTree:
    def __init__(self, data):
        self.root = None
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height starts at 1 for a new node

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        # Step 1 - Perform normal BST insert
        if root is None:
            return AVLTree(data)

        if data < root.data:
            root.left = self._add(root.left, data)
        elif data > root.data:
            root.right = self._add(root.right, data)
        else:
            # Duplicate data is not allowed
            return root

        # Step 2 - Update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor of this node to check if it became unbalanced
        balance = self.get_balance(root)

        # Step 4 - If unbalanced, there are 4 cases:

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Function to print the tree in order (useful for debugging)
    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)

# Example usage
avl_tree = AVLTree(10)
avl_tree.add(20)
avl_tree.add(30)
avl_tree.add(40)
avl_tree.add(50)
avl_tree.add(25)

avl_tree.in_order_traversal(avl_tree.root)
