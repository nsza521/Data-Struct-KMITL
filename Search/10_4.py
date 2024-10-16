class hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * table_size
        self.data_count = 0

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(self, n):
        while True:
            n += 1
            if self.is_prime(n):
                return n

    def hash_function(self, key):
        return key % self.table_size

    def rehash(self, reason):
        print(f"{reason}")
        old_table = self.table
        self.table_size = self.next_prime(self.table_size * 2)
        self.table = [None] * self.table_size
        self.data_count = 0
        
        items_to_insert = [item for item in old_table if item is not None]
        
        items_to_insert.reverse()
        
        for item in items_to_insert:
            self.insert(item, rehashing=True)

    def insert(self, key, rehashing=False):
        if not rehashing and (self.data_count + 1) / self.table_size * 100 > self.threshold:
            self.rehash('****** Data over threshold - Rehash !!! ******')
            return self.insert(key)

        index = self.hash_function(key)
        collision = 0

        while self.table[index] is not None:
            collision += 1
            print(f"collision number {collision} at {index}")
            if collision == self.max_collision:
                if not rehashing:
                    self.rehash('****** Max collision - Rehash !!! ******')
                    return self.insert(key)
                else:
                    return
            index = (self.hash_function(key) + collision ** 2) % self.table_size

        self.table[index] = key
        self.data_count += 1

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i+1}\t{item}")
        print("----------------------------------------")

print(" ***** Rehashing *****")
input_str = input("Enter Input : ")
table_size, max_collision, threshold = map(int, input_str.split('/')[0].split())
data_input = list(map(int, input_str.split('/')[1].split()))

h = hash(table_size, max_collision, threshold)

print("Initial Table :")
h.print_table()

for item in data_input:
    print(f"Add : {item}")
    h.insert(item)
    h.print_table()