class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None  # Initially, the stack is empty

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # New node points to the current top
        self.top = new_node       # New node becomes the new top

    def pop(self):
        if self.is_empty():
            return None  # Return None if the stack is empty
        popped_node = self.top    # Get the top node
        self.top = self.top.next  # Update the top to the next node
        return popped_node.data   # Return the popped node's data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: 3 -> 2 -> 1 -> None

stack.pop()
stack.display()  # Output: 2 -> 1 -> None

stack.push(3)
stack.display()  # Output: 3 -> 2 -> 1 -> None
