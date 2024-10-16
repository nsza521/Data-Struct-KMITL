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
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

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

    def addHead(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        self.size += 1
        # code here

    def insert(self, pos, item):
        # 999 case
        if pos > self.size:
            self.append(item)
            return
        elif pos < -self.size:
            self.addHead(item)
            return
        

        if pos < -self.size or pos > self.size:
            return
        if pos < 0:
            pos = self.size + pos
        if pos == 0:
            self.addHead(item)
            return
        if pos == self.size:
            self.append(item)
            return
        
 
        p = Node(item)
        q = self.head
        for _ in range(pos - 1):
            q = q.next
        p.next = q.next
        p.previous = q
        q.next.previous = p
        q.next = p
        self.size += 1
            
    def size(self):
        return self.size
    
    def pop(self, pos=None):
        if self.size == 0:
            return "Out of Range"
        
        if pos is None:
            pos = self.size - 1

        if pos < 0 or pos >= self.size:
            return "Out of Range"

        if pos == 0:  # Remove head
            pop_item = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
        elif pos == self.size - 1:  # Remove tail
            pop_item = self.tail.value
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:  # Remove middle
            current = self.head
            for _ in range(pos):
                current = current.next
            pop_item = current.value
            current.previous.next = current.next
            current.next.previous = current.previous

        self.size -= 1
        return "Success"
        
    def search(self, item):
        t = self.head
        while t is not None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"
    
    def index(self, item):
        t = self.head
        count = 0
        while t is not None:
            if (t.value == item):
                return count
            t = t.next
            count += 1
        return -1

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
