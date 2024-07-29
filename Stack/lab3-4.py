class StackCalc:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def pop_discard(self):
        if not self.isEmpty():
            self.items.pop()
        if(self.isEmpty()):
            self.push(0)
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def plus(self):
        x = self.pop()
        y = self.pop()
        self.push(x+y)
        return x+y

    def minus(self):
        x = self.pop()
        y = self.pop()
        self.push(x-y)
        return x-y
    
    def multiply(self):
        x = self.pop()
        y = self.pop()
        self.push(x*y)
        return x*y
    
    def divide(self):
        x = self.pop()
        y = self.pop()
        self.push(x/y)
        return x/y
    
    def dub(self):
        x = self.pop()
        self.push(x)
        self.push(x)

    def run(self,arg):
        arg = arg.split()
        for vaule in arg:
            if(vaule.isnumeric()):
                self.push(int(vaule))
            elif(vaule == "+"):
                self.plus()
            elif(vaule == "-"):
                self.minus()
            elif(vaule == "*"):
                self.multiply()
            elif(vaule == "/"):
                self.divide()
            elif(vaule == "DUP"):
                self.dub()
            elif(vaule == "POP"):
                self.pop_discard()
            else:
                print(f"Invalid instruction: {vaule}")
                break

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
if not machine.isEmpty():
    print(int(machine.items[-1]))


# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ 1. คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# 2. การนำค่าออกจาก stack สำหรับ calculator นี้ให้ การนำค่าออกจาก stack ครั้งแรกเป็น operand ด้านซ้าย และ การนำค่าออกจาก stack ครั้งที่ 2 เป็น operand ด้านขวา
# *************************************************
# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())


# test case
# * Stack Calculator *
# Enter arguments : 5 6 +
# 11

# * Stack Calculator *
# Enter arguments : 3 DUP +
# 6

# * Stack Calculator *
# Enter arguments : 6 5 5 7 * - /
# 5

# * Stack Calculator *
# Enter arguments : a b c +
# Invalid instruction: a

# * Stack Calculator *
# Enter arguments : 12
# 12

# * Stack Calculator *
# Enter arguments : 9 14 DUP + - 3 POP
# 19

# * Stack Calculator *
# Enter arguments : 1 2 3 4 5 POP POP POP
# 2

# * Stack Calculator *
# Enter arguments : 4 POP
# 0