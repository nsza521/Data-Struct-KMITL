
class Queue:
    def __init__(self):
        self._items = []

    def enQueue(self, i):
        self._items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self._items.pop(0)
        return None

    def isEmpty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def items(self):
        return self._items

Input = input("Enter Input : ").split(",")
q = Queue()
dq = Queue()

for data in Input:
    if data[0] == "E":
        method, number = data.split()
        q.enQueue(number)
        print(", ".join(q.items()))
    elif data[0] == "D":
        if not q.isEmpty():
            x = q.deQueue()
            dq.enQueue(x)
            print(x + " <- ",end='')
            if not q.isEmpty():
                print(", ".join(q.items()))
            else:
                print("Empty")
        else:
            print("Empty")
if(dq.isEmpty()):
    print("Empty",end='')
else:
    print(", ".join(dq.items()),end="")
print(" : ",end="")
if(q.isEmpty()):
    print("Empty",end='')
else:
    print(", ".join(q.items()))

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา
# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue
# D  ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue
# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty

# Enter Input : E 1,E 2,E 3,D,D,E 4
# 1
# 1, 2
# 1, 2, 3
# 1 <- 2, 3
# 2 <- 3
# 3, 4
# 1, 2 : 3, 4

# Enter Input : E 1,E 2,D,D,D
# 1
# 1, 2
# 1 <- 2
# 2 <- Empty
# Empty
# 1, 2 : Empty

# Enter Input : D
# Empty
# Empty : Empty
