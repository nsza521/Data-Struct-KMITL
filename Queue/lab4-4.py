class Cafe:
    def __init__(self, input_data):
        self.events = sorted(input_data, key=lambda x: int(x.split(",")[0])) 
        self.balista_end_time = [0, 0]  #\
        self.queue = []  
        self.longest_wait_time = 0
        self.waiting_customer_id = 0
        self.output = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def calculate(self):

        for entry in self.events:
            arrival, prep_time = map(int, entry.split(","))
            self.enqueue((arrival, prep_time))

        index = 1  

        while not self.is_empty():
            arrival, prep_time = self.dequeue()

            available_barista = self.balista_end_time.index(min(self.balista_end_time))
            start_time = max(self.balista_end_time[available_barista], arrival)
            wait_time = start_time - arrival

            if wait_time > self.longest_wait_time:
                self.longest_wait_time = wait_time
                self.waiting_customer_id = index

            self.balista_end_time[available_barista] = start_time + prep_time

            self.output.append((self.balista_end_time[available_barista], index))

            index += 1

        self.output.sort()

        for time, customer_id in self.output:
            print(f"Time {time} customer {customer_id} get coffee")

        if self.longest_wait_time > 0:
            print(f"The customer who waited the longest is : {self.waiting_customer_id}")
            print(f"The customer waited for {self.longest_wait_time} minutes")
        else:
            print("No waiting")

# Input
print(" ***Cafe***")
data = input("Log : ").split("/")
cafe = Cafe(data)
cafe.calculate()

# ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) 
# ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting

# ตัวอย่างข้อมูลเข้า
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# คำอธิบาย
# ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 
# ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 

# ไทม์ไลน์
# เวลา(t)    เหตุการณ์
# 0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ
# 2    ลูกค้าคนที่ 3 เข้ามาในร้าน
# 3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที
# 6    ลูกค้าคนที่ 3 ได้กาแฟ
# 7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ
# 10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ
# 14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที
# 15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ

# ผลลัพธ์ 
# Time 3 customer 1 get coffee  
# Time 6 customer 3 get coffee  
# Time 7 customer 2 get coffee  
# Time 14 customer 4 get coffee  
# Time 15 customer 5 get coffee  
# Time 15 customer 6 get coffee  
# The customer who waited the longest is : 6
# The customer waited for 4 minutes


# test case 
#  ***Cafe***
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# Time 3 customer 1 get coffee  
# Time 6 customer 3 get coffee  
# Time 7 customer 2 get coffee  
# Time 14 customer 4 get coffee  
# Time 15 customer 5 get coffee  
# Time 15 customer 6 get coffee  
# The customer who waited the longest is : 6
# The customer waited for 4 minutes

#  ***Cafe***
# Log : 0,1/1,1/2,1/3,1/4,1/5,1
# Time 1 customer 1 get coffee  
# Time 2 customer 2 get coffee  
# Time 3 customer 3 get coffee  
# Time 4 customer 4 get coffee  
# Time 5 customer 5 get coffee  
# Time 6 customer 6 get coffee  
# No waiting

#  ***Cafe***
# Log : 0,1/0,1/1,1/1,1/2,1/2,1
# Time 1 customer 1 get coffee  
# Time 1 customer 2 get coffee  
# Time 2 customer 3 get coffee  
# Time 2 customer 4 get coffee  
# Time 3 customer 5 get coffee  
# Time 3 customer 6 get coffee  
# No waiting