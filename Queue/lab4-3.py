class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return "Empty"

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def check_duplicate(input_str):
    left, right = input_str.split('/')
    queue = Queue()
    
    for book in left.split():
        queue.enQueue(book)
    
    for method in right.split(','):
        if method.startswith('E'):
            book = method.split()[1]
            queue.enQueue(book)
        elif method == 'D':
            queue.deQueue()
    
    book_set = set()
    while not queue.isEmpty():
        book = queue.deQueue()
        if book in book_set:
            return "Duplicate"
        book_set.add(book)
    
    return "NO Duplicate"

x = input("Enter Input : ")
print(check_duplicate(x)) 

# กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# D                -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
# E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง

# Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
# NO Duplicate

# ALL CASE IS HIDDEN CASE