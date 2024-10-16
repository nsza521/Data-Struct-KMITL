class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def get_max_digits(self):
        max_num = 0
        current = self.head
        while current:
            max_num = max(max_num, abs(current.data))
            current = current.next
        return len(str(max_num))
    
    def get_digit(self, number, n):
        return abs(number) // 10**n % 10

    def is_all_zeros(self):
        current = self.head
        while current:
            if current.data != 0:
                return False
            current = current.next
        return True
        
    def radix_sort(self):
        if self.is_all_zeros():
            print(f"0 Time(s)")
            print(f"Before Radix Sort : {self}")
            print(f"After  Radix Sort : {self}")
            return
        max_digits = self.get_max_digits()
        round_count = 0
        for i in range(max_digits):
            round_count += 1
            pos_buckets = [LinkedList() for _ in range(10)]
            neg_buckets = [LinkedList() for _ in range(10)]
            
            current = self.head
            while current:
                digit = self.get_digit(current.data, i)
                if current.data >= 0:
                    pos_buckets[digit].append(current.data)
                else:
                    neg_buckets[digit].append(current.data)
                current = current.next

            # Print current round status
            print(f"Round : {i + 1}")
            for j in range(10):
                print(f"{j} : ", end='')
                current = neg_buckets[j].head
                while current:
                    print(current.data, end=' ')
                    current = current.next
                current = pos_buckets[j].head
                while current:
                    print(current.data, end=' ')
                    current = current.next
                print()
            print("------------------------------------------------------------")
            
            # Rebuild the main list from buckets, starting with negative numbers in reverse order
            self.head = None
            for j in range(9, -1, -1):
                self._merge(neg_buckets[j])
            for j in range(10):
                self._merge(pos_buckets[j])
        
        print(f"{round_count} Time(s)")
        print(f"Before Radix Sort : {before_l}")
        print(f"After  Radix Sort : {self}")

    def _merge(self, bucket):
        if not self.head:
            self.head = bucket.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = bucket.head

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)

nums = input("Enter Input : ").split()
before_l = LinkedList()
after_l = LinkedList()
for data in nums:
    before_l.append(int(data))
    after_l.append(int(data))

print("------------------------------------------------------------")
after_l.radix_sort()
