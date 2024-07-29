class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of' + str(self.size())+"items :  "
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
    
def match(open,close):
    return (open == '(' and close == ')') or (open == '{' and close == '}') or (open == '[' and close == ']')

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
    if(s.isEmpty()):
        print("Parentheses : Matched ! ! !")
    else:
        print("Parentheses : Unmatched ! ! !")

x = input("Enter Input : ")
parenmatch(x)

# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   
# โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ที่บอกว่าคู่วงเล็บที่ Input เข้ามานั้น Match กันหรือไม่
# test case 1
# Enter Input : ()[]
# Parentheses : Matched ! ! !

# test case 2
# Enter Input : [](]
# Parentheses : Unmatched ! ! !