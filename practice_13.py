class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedListQueue:
    def __init__(self):
        self.front = None  # Points to the front (head) of the queue
        self.rear = None   # Points to the rear (tail) of the queue

    def enqueue(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node  # Both front and rear point to the new node
            return
        self.rear.next = new_node  # Link the old rear to the new node
        self.rear = new_node       # Update the rear to the new node

    def dequeue(self):
        if self.is_empty():
            return None  # Return None if the queue is empty
        dequeued_node = self.front  # Get the front node
        self.front = self.front.next  # Move the front to the next node
        if self.front is None:  # If the queue is now empty, update rear to None
            self.rear = None
        return dequeued_node.data  # Return the data of the dequeued node

    def is_empty(self):
        return self.front is None  # The queue is empty if front is None

    def peek(self):
        if self.is_empty():
            return None  # Return None if the queue is empty
        return self.front.data  # Return the data at the front of the queue

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))  # Collect all elements in the queue
            current = current.next
        return " -> ".join(elements)  # Join elements with arrows to show the queue order

# Example usage:
queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue)  # Output: 1 -> 2 -> 3

queue.dequeue()
print(queue)  # Output: 2 -> 3

queue.enqueue(4)
print(queue)  # Output: 2 -> 3 -> 4

queue.dequeue()
queue.dequeue()
print(queue)  # Output: 4

queue.dequeue()
print(queue)  # Output: Queue is empty
