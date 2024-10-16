class TreeNode:
    def __init__(self, value):
        self.value = str(value)
        self.left = None
        self.right = None
    def __str__(self):
        return self.value

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        new_node = TreeNode(value)
        queue = [self.root]
        
        while queue:
            current_node = queue.pop(0)
            if not current_node.left:
                current_node.left = new_node
                return
            elif not current_node.right:
                current_node.right = new_node
                return
            queue.append(current_node.left)
            queue.append(current_node.right)

    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    

        return result
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

bt = BinaryTree(1)
bt.insert(2)
bt.insert(5)
bt.insert(3)
bt.insert(4)


print("Level Order Traversal:", bt.level_order_traversal())
arr = bt.level_order_traversal()
bt.print_tree(bt.root)

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)