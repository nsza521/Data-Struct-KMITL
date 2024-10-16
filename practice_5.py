class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
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
        if self.head is None:
            self.head =  Node(item)
        else:
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = Node(item)
            
    def rearrangeEvenOdd(self):
        p = self.head
        p2 = self.head
        self.head = None
        while p:
            if(int(p.value)%2 == 0):
                if self.head is None:
                    self.head = Node(p.value)
                else:
                    h = self.head
                    while h.next is not None:
                        h = h.next
                    h.next =  Node(p.value)
            p = p.next
        # This is bad code 2 loop Big(O) 2*O(n^2)
        while p2:
            if(int(p2.value)%2 == 1):
                if self.head is None:
                    self.head = Node(p2.value)
                else:
                    h = self.head
                    while h.next is not None:
                        h = h.next
                    h.next =  Node(p2.value)
            p2 = p2.next

dl = LinkedList()
input_list = input("Enter the numbers list: ").split()
for item in input_list:
    dl.append(item)

dl.rearrangeEvenOdd()
print(f"Rearranged list: [{dl}]")