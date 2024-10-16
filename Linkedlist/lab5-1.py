class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        s = str(cur.value)
        while cur.next is not None:
            cur = cur.next
            s += f", {cur.value}"
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
            self.tail = p
        else:
            t = self.tail
            t.next = p
            p.previous = t
            self.tail = p
        self.size += 1

    def rearrangeEvenOdd(self):
        if self.isEmpty():
            return

        even_head = even_tail = None
        odd_head = odd_tail = None

        current = self.head

        while current:
            next_node = current.next
            current.next = None  

            if int(current.value) % 2 == 0:
                if even_head is None:
                    even_head = even_tail = current
                else:
                    even_tail.next = current
                    current.previous = even_tail
                    even_tail = current
            else:
                if odd_head is None:
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current
                    current.previous = odd_tail
                    odd_tail = current

            current = next_node

        if even_tail:
            even_tail.next = odd_head
        if odd_head:
            odd_head.previous = even_tail

        self.head = even_head if even_head else odd_head
        self.tail = odd_tail if odd_tail else even_tail

dl = LinkedList()
input_list = input("Enter the numbers list: ").split()
for item in input_list:
    dl.append(item)

dl.rearrangeEvenOdd()
print(f"Rearranged list: [{dl}]")
