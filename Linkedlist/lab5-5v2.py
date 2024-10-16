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

    def radix_sort(self):
        # Separate negative and non-negative numbers
        negative = LinkedList()
        non_negative = LinkedList()
        current = self.head
        while current:
            if current.data < 0:
                negative.append(current.data)
            else:
                non_negative.append(current.data)
            current = current.next

        # Sort non-negative numbers
        self._radix_sort_list(non_negative)

        # Sort negative numbers and reverse the order
        self._radix_sort_list(negative)
        self._reverse_list(negative)

        # Merge sorted lists
        self.head = None
        self._merge(negative)
        self._merge(non_negative)

    def _radix_sort_list(self, lst):
        max_digits = lst.get_max_digits()
        for exp in range(max_digits):
            buckets = [LinkedList() for _ in range(10)]
            current = lst.head
            while current:
                digit = self.get_digit(current.data, exp)
                buckets[digit].append(current.data)
                current = current.next
            
            print(f"Round : {exp + 1}")
            for digit in range(10):
                bucket = buckets[digit]
                print(f"{digit} : ", end='')
                bucket_current = bucket.head
                while bucket_current:
                    print(f"{bucket_current.data} ", end='')
                    bucket_current = bucket_current.next
                print()
            print("------------------------------------------------------------")
            
            lst.head = None
            for bucket in buckets:
                lst._merge(bucket)

    def _reverse_list(self, lst):
        prev = None
        current = lst.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        lst.head = prev

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
print("Before Radix Sort :", before_l)
print("After  Radix Sort :", after_l)
