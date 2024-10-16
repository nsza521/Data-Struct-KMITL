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
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s.strip()

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

    def merge(self,l2):
        p = l2.tail 
        while p != None:
            self.append(p.value)
            p = p.previous
    

l1_d = LinkedList()
l2_d = LinkedList()

l1 ,l2 = input("Enter Input (L1,L2) : ").split()
l1 = l1.split("->")
l2 = l2.split("->")

for item in l1:
    l1_d.append(item)
for item in l2:
    l2_d.append(item)

print(f"L1    : {l1_d}")
print(f"L2    : {l2_d}")

l1_d.merge(l2_d)

print(f"Merge : {l1_d}")

