class Stack:
    def __init__(self,max,car_list = None):
        if car_list == None:
            self.items = []
        else:
            if not ('0' in car_list):
                self.items = car_list
            else:
                self.items = []
        self.max = max

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def arrive(self,i):
        if (len(self.items)+1 > int(self.max)):    
            print(f"car {i} cannot arrive : Soi Full")
        elif(i in car_list):
            print(f"car {i} already in soi")
        else:
            self.push(i)
            print(f"car {i} arrive! : Add Car {i}")

    def depart(self , i):
        if(len(self.items)==0):
            print(f"car {i} cannot depart : Soi Empty")
        elif(i in self.items):
            print(f"car {i} depart ! : Car {i} was remove")
            self.items.remove(i)
        else:
            print(f"car {i} cannot depart : Dont Have Car {i}")
            
    
print("******** Parking Lot ********")
max , car_list , method , car = input("Enter max of car,car in soi,operation : ").split()
car_list = car_list.split(',')
car_parking = Stack(max ,car_list)

if(method == "arrive"):
    car_parking.arrive(car)
if(method == "depart"):
    car_parking.depart(car)

result = [eval(i) for i in car_parking.items]
print(result)

# ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output
# การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4
# ***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
# car 5 arrive! : Add Car 5
# [1, 2, 3, 4, 5]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
# car 5 cannot arrive : Soi Full
# [1, 2, 3, 4]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 1
# car 1 already in soi
# [1, 2, 3, 4]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 8 1,4,6,2,3,5,8 arrive 7
# car 7 arrive! : Add Car 7
# [1, 4, 6, 2, 3, 5, 8, 7]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 0 depart 3
# car 3 cannot depart : Soi Empty
# []

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 4 1,3,2 depart 1
# car 1 depart ! : Car 1 was remove
# [3, 2]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
# car 1 cannot depart : Dont Have Car 1
# [2, 3, 5, 7, 8]
