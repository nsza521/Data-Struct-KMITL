class Stack:
    def __init__(self):
        self.items = []

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

def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    S = Stack()

    for char in infix:
        if char.isalnum():  # Check if the character is an operand
            output.append(char)
        elif char == '(':
            S.push(char)
        elif char == ')':
            while not S.isEmpty() and S.items[-1] != '(':
                output.append(S.pop())
            S.pop()  # Remove '(' from the stack
        else:  # The character is an operator
            while (not S.isEmpty() and S.items[-1] != '(' and
                   precedence.get(char, 0) <= precedence.get(S.items[-1], 0)):
                output.append(S.pop())
            S.push(char)

    while not S.isEmpty():
        output.append(S.pop())

    return ''.join(output)

inp = input('Enter Infix : ')
postfix = infix_to_postfix(inp)
print('Postfix :', postfix)

# ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

# test case 1
# Enter Infix : a+b
# Postfix : ab+

# test case 2
# Enter Infix : a+b*c
# Postfix : abc*+

# test case 3
# Enter Infix : a*b+c
# Postfix : ab*c+

# test case 4
# Enter Infix : a+b*c-d
# Postfix : abc*+d-

# test case 5
# Enter Infix : a+b*c-(d/e+f)*g
# Postfix : abc*+de/f+g*-

# test case 6
# Enter Infix : A+(B*C-(D/E^F)*G)*H
# Postfix : ABC*DEF^/G*-H*+

# test case 7
# Enter Infix : K+L-M*N+(O^P)*W/U/V*T+Q
# Postfix : KL+MN*-OP^W*U/V/T*+Q+

# test case 8
# Enter Infix : G+A+(U-R)^I
# Postfix : GA+UR-I^+



