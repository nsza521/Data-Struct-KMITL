class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    def push(self, data):
        self.stack.append(data)  # Add an element to the end (top) of the stack

    def pop(self):
        if self.is_empty():
            return None  # Return None if the stack is empty
        return self.stack.pop()  # Remove and return the top element of the stack

    def peek(self):
        if self.is_empty():
            return None  # Return None if the stack is empty
        return self.stack[-1]  # Return the top element without removing it

    def is_empty(self):
        return len(self.stack) == 0  # The stack is empty if its length is 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.stack)
stack.push(3)
print(stack.stack)

print(stack.peek())  # Output: 3 (top element)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None (since the stack is now empty)
