class Queue:
    def __init__(self):
        self.items = []
        self.special_items = []
        self.special_count = 0

    def enQueueNormal(self, value):
        self.items.append(value)

    def enQueueSpecial(self, value):
        self.special_items.insert(self.special_count,value)
        self.special_count += 1

    def deQueue(self):
        if not self.isEmptySpecial():
            return self.special_items.pop(0)
        elif not self.isEmpty():
            return self.items.pop(0)
        return "Empty"

    def isEmpty(self):
        return len(self.items) == 0

    def isEmptySpecial(self):
        return len(self.special_items) == 0

    def size(self):
        return len(self.items) + len(self.special_items)

Input = input("Enter Input : ").split(",")
q = Queue()

for data in Input:
    if data.startswith("EN"):
        method, number = data.split()
        q.enQueueNormal(number)
    elif data.startswith("ES"):
        method, number = data.split()
        q.enQueueSpecial(number)
    elif data == "D":
        print(q.deQueue())

# PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ
# เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

# Input :
# EN <value>  เป็นโอตะธรรมดา  id = value
# ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
# D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty

# Enter Input : EN 1,EN 2,D,D,D,EN 3,D
# 1
# 2
# Empty
# 3

# Enter Input : EN 1,ES 2,D,D,D,EN 3,D
# 2
# 1
# Empty
# 3

# Enter Input : EN 1,ES 2,ES 99,D,D,D,EN 3,D
# 2
# 99
# 1
# 3
