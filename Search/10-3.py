class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class HashTable:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.table = [None] * table_size
        self.max_collision = max_collision
        self.full = False
        self.count = 0

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.table_size

    def insert(self, key, value):
        if self.full:
            return

        if self.count == self.table_size:
            print('This table is full !!!!!!')
            return

        index = self.hash_function(key)
        collision_count = 0
        
        while self.table[index] is not None:
            collision_count += 1
            print(f'collision number {collision_count} at {index}')
            if collision_count == self.max_collision:
                print('Max of collisionChain')
                self.print_hash()
                return
            index = (self.hash_function(key) + collision_count ** 2) % self.table_size

        self.table[index] = Data(key, value)
        self.count += 1

        if self.count == self.table_size:
            self.print_hash()
            print('This table is full !!!!!!')
            self.full = True
        else:
            self.print_hash()

    def print_hash(self):
        for i, item in enumerate(self.table):
            print(f'#{i+1}\t{str(item) if item is not None else "None"}')
        print('---------------------------')


print(' ***** Fun with hashing *****')
inp = input("Enter Input : ").split('/')

table_size, max_collision = map(int, inp[0].split())

hass = HashTable(table_size, max_collision)

for entry in inp[1].split(','):
    key, value = entry.split()
    hass.insert(key, value)
