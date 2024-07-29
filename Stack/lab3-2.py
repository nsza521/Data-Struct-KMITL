class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = "  " + str(self.size()) + " : "
        for e in self.items:
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
    
def match(open,close):
    return (open == '(' and close == ')') or (open == '{' and close == '}') or (open == '[' and close == ']')

def is_match(string):
    return ("[" in string and "]" in string) or ("(" in string and ")" in string) or ("{" in string and "}" in string) 


def check_open(open):
    return open in "([{"

def check_close(close):
    return close in "}])"

def parenmatch(string):
    s = Stack()
    for str in string:
        if(str in "{[("):
            s.push(str)
        elif(str in ")]}"):
            if(s.isEmpty()):
                s.push(str)
            else:
                if match(s.peek(),str):
                    s.pop()
                else:
                    s.push(str)
    if(s.isEmpty()):
        print(f"{string} MATCH")
    elif(not is_match(string)):
        open = False
        close = False
        for paren in s.items:
            if(check_open(paren)):
                open = True
            if(check_close(paren)):
                close = True

        if(not ("{" in string or "(" in string or "[" in string)):
            print(f"{string} close paren excess")
        elif(open and not close):
            print(f"{string} open paren excess " + s.__str__())
        else:
            print(f"{string} Unmatch open-close")
    else:
        open = False
        close = False
        for paren in s.items:
            if(check_open(paren)):
                open = True
            if(check_close(paren)):
                close = True
        if(open and close):
            print(f"{string} open and close paren excess ")
        if(open):
            print(f"{string} open paren excess " + s.__str__())
        if(close):
            print(f"{string} close paren excess ")

x = input("Enter expresion : ")
parenmatch(x)   

# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด
# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด
# 2. วงเล็บปิดเกิน
# 3. วงเล็บเปิดเกิน
# แล้วให้แสดงผลตามตัวอย่าง

# test case 1
# Enter expresion : [[)))))
# [[))))) Unmatch open-close  

# test case 2
# Enter expresion : [[))
# [[)) Unmatch open-close  

# test case 3
# Enter expresion : (())))
# (()))) close paren excess

# test case 4
# Enter expresion : )}]
# )}] close paren excess

# test case 5
# Enter expresion : (((
# ((( open paren excess   3 : (((

# test case 6
# Enter expresion : (a+c)(a-b)*c(-a
# (a+c)(a-b)*c(-a open paren excess   1 : (

# test case 7
# Enter expresion : (([]))
# (([])) MATCH

# test case 8
# Enter expresion : (){}[]}
# (){}[]} close paren excess
