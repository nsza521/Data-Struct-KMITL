class Queue:
    def __init__(self,items=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.special_items = []
        self.special_items = []
        self.special_count = 0

    def enQueue(self, value):
        self.items.append(value)

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
    
class Stack:
    def __init__(self,list=None):
        self.explosive = 0
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self,n):
        if(n=='n' and self.isEmpty()):
            return 'Empty'
        if(self.isEmpty()):
            return 'ytpmE'
        s = ''
        for e in reversed(self.items):
            s+= str(e)+''
        return s
    
    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def items(self):
        return self.items

    def reverse(self):
        s = ''
        for e in reversed(self.items):
            s+= str(e)+''
        self.items = []
        for i in s:
            self.items.append(i)
            
    
normal , mirror = input("Enter Input (Normal, Mirror) : ").split()
# ------------------------------------------------------------------------

def pop_3(stack):
    for i in range(3):
        stack.pop()

def countequal3():
    count = 0
    pop_3(mirror_stack)
    mirror_stack.explosive+=1
    no_explosive.enQueue(char)

# ------------------------------------------------------------------------

mirror_stack = Stack()
normal_stack = Stack()
no_explosive = Queue()

# ------------------------------------------------------------------------
count = 0
for char in reversed(mirror):
    if(not mirror_stack.isEmpty() and mirror_stack.peek() == char):
            count += 1
    else:
            count = 1

    mirror_stack.push(char)

    if(count == 3):
            countequal3()


# ------------------------------------------------------------------------

char = ''
size = no_explosive.size()
is_explosive = True
while(is_explosive):
    count = 0
    for check in mirror_stack.items:    
        if(check == char):
            count+=1
        else:
            count = 1
        char = check
        if(count == 3):
            countequal3()
    if(size == no_explosive.size()):
        is_explosive = False
    else:
        size = no_explosive.size()

# ------------------------------------------------------------------------
interrupt_fail = 0
count = 0
for char in (normal):
    if(not normal_stack.isEmpty() and normal_stack.peek() == char):
        count += 1
    else:
        count = 1
    # print(count,end='')
    normal_stack.push(char)
    if(count == 3):
        if(no_explosive.isEmpty()):
            count = 0
            pop_3(normal_stack)
            normal_stack.explosive+=1
        else:
            count = 0
            queue = no_explosive.deQueue()
            normal_stack.pop()
            normal_stack.push(queue)
            normal_stack.push(char)
            if(queue == char):
                interrupt_fail += 1

# ------------------------------------------------------------------------
queue = Queue(normal_stack.items)
result = Stack()
explosion = True
bomb = 0
count = 0
i = 0
while explosion:
    result = Stack()
    bomb_default = bomb
    for s in queue.items:
        if not result.isEmpty() and result.peek() == s:
            count += 1
        else:
            count = 1

        result.push(s)

        if count == 3:
            count = 0
            result.pop()
            result.pop()
            result.pop()
            bomb += 1
    queue = Queue(result.items)

    if(bomb_default == bomb or i>=76):
        break
    i+=1

# ------------------------------------------------------------------------



print("NORMAL :")
print(result.size())
print(result.__str__('n'))
print(f"{result.explosive + normal_stack.explosive + bomb - interrupt_fail} Explosive(s) ! ! ! (NORMAL)")
if(bomb!=0):
    print(f"Failed Interrupted {interrupt_fail} Bomb(s)")
print('------------MIRROR------------')
print(': RORRIM')
print(mirror_stack.size())
print(mirror_stack.__str__('m'))
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_stack.explosive}")

# print(result.explosive)
# print(normal_stack.explosive)
# print(bomb)
# print(interrupt_fail)


# # thiis code is shit
# เกม Color Crush คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัวทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว
# เนื้อเรื่อง :  หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม Color Crush 2 ขึ้นมา กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง คือ ฝั่งปกติกับฝั่งโลกกระจก โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  ITEM สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty
# อธิบายรูปแบบ Input ของ Test_Case_1 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> HHH โดยฝั่งโลกกระจกจะมีระเบิด H ที่เป็น ITEM สำหรับขัดขวาง 1 ลูกไว้สำหรับขัดขวางการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A และ B ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด H ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3 เพื่อให้เห็นภาพ -> AAABBBCDEE -> AA(H)ABBBCDEE  -> AA(H)ACDEE ลำดับจะเป็นดังนี้  และฝั่งปกติเกิดการระเบิด 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 1 ครั้ง
# อธิบายรูปแบบ Input ของ Test_Case_3 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDDDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> BBBTENETAAA โดยฝั่งโลกกระจกจะมีระเบิด A และ B ที่เป็น ITEM สำหรับขัดขวาง 2 ลูกตามลำดับไว้สำหรับป้องกันการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A B และ D ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด A  ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3  เพื่อให้เห็นภาพ -> AAABBBCDDDEE -> AA(A)ABBBCDDDEE -> ABBBCDDDEE ลำดับจะเป็นดังนี้  ต่อมาจะนำระเบิด B ไปขัดขวางการระเบิดของระเบิด B เพื่อให้เห็นภาพ  ABBBCDDDEE -> ABB(B)BCDDDEE -> ABCDDDEE  ต่อมาเกิดการระเบิดอีก 1 ครั้ง ABCDDDEE -> ABCEE ซึ่งฝั่งโลกกระจกไม่สามารถขัดขวางได้เพราะ ITEM สำหรับขัดขวางหมดแล้ว   และฝั่งปกติเกิดการระเบิดทั้งหมด 3 ครั้ง  ซึ่ง 2 ครั้งเกิดจากการที่ฝั่งโลกกระจกใส่ระเบิดสีเดียวกันมาซึ่งถือว่าเป็นการขัดขวางที่ผิดหและเกิดการระเบิดเองอีก 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 2 ครั้ง
# อธิบายรูปแบบ Output : แบ่งออกเป็น 2 ฝั่งคือฝั่งปกติกับฝั่งโลกกระจก  โดยบรรทัดแรกจะเป็นจำนวนระเบิดที่เหลืออยู่ บรรทัดที่สองจะเป็นระเบิดที่เหลืออยู่แต่ถ้าหากไม่มีระเบิดเหลืออยุ่เลยให้แสดง "Empty" บรรทัดที่สามจะเป็นจำนวนที่เกิดระเบิดขึ้น บรรทัดที่สี่จะมีเฉพาะฝั่งปกติถ้าหากเกิดเหตุการณ์ที่ ITEM ของฝั่งโลกกระจกมาขัดขวาง แต่ระเบิดนั้นดันเป็นลูกเดียวกับที่จะเกิดการระเบิด  ส่วนทีมสีน้ำเงินจะเหมือนกับทีมสีแดงแต่บรรทัดที่ 2 กับ 3 และชื่อทีม จะเป็นแบบ inverse
# คำใบ้ - ใช้ Stack ในการหาลูกระเบิดเรียงกัน 3 ลูก   โดยให้ทำฝั่งโลกกระจกก่อนว่ามีระเบิดลูกอะไรบ้าง (ก่อนเข้า stack ให้ Reverse ก่อน)  จากนั้นเก็บลง Queue แล้วไปทำฝั่งปกติถ้าหากฝั่งปกติเกิดการระเบิดก็ DeQueue ระเบิดที่ได้รับมาจากฝั่งกระจกมาขัดระเบิดระหว่างลูกที่ 2 กับ 3

# อธิบาย Case 10:

# ฝั่งซ้าย = DDDFFFGGG
# ฝั่งขวา = ABBBAACCC
# ทำฝั่งขวาก่อนโดยการ inverse ABBBAACCC -> CCCAABBBA จะได้ระเบิดมา 3 ลูกคือ C B A ตามลำดับจากนั้นเก็บลง Queue ต่อมาดูที่ฝั่งซ้าย DDD จะเกิดการระเบิดเราจะนำ C ไปขัด | ต่อมา F จะระเบิดเราจะนำ B มาขัด | ต่อมา G จะระเบิดเราจะนำ A มาขัด   สุดท้ายจะกลายเป็น DDCDFFBFGGAG


# Enter Input (Normal, Mirror) : AAABBBCDEE HHH
# NORMAL :
# 8
# EEDCAHAA
# 1 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 1

# Enter Input (Normal, Mirror) : AAABBBCDEE FGHHHIOPPP
# NORMAL :
# 12
# EEDCBHBBAPAA
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 4
# FGIO
# (RORRIM) ! ! ! (s)evisolpxE 2

# Enter Input (Normal, Mirror) : AAABBBCDDDEE BBBTENETAAA
# NORMAL :
# 5
# EECBA
# 1 Explosive(s) ! ! ! (NORMAL)
# Failed Interrupted 2 Bomb(s)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 2

# Enter Input (Normal, Mirror) : AAABBBDDD TENET
# NORMAL :
# 0
# Empty
# 3 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 0

# Enter Input (Normal, Mirror) : AAABBBCDDDEE OOOZZZTENETXXXYYY
# NORMAL :
# 15
# EEDZDDCBXBBAYAA
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 4

# Enter Input (Normal, Mirror) : DDDFFFGGG ABBBAACCC
# NORMAL :
# 12
# GAGGFBFFDCDD
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 3

# Enter Input (Normal, Mirror) : AJJJJJJJAA JJJJJJ
# NORMAL :
# 0
# Empty
# 2 Explosive(s) ! ! ! (NORMAL)
# Failed Interrupted 2 Bomb(s)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 2

# Enter Input (Normal, Mirror) : PPPAAAABBBB PPPAAAA
# NORMAL :
# 10
# BAAPAAPAPP
# 1 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 1
# A
# (RORRIM) ! ! ! (s)evisolpxE 2