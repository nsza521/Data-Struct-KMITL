print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
max_lines = 2*n + n - 2
max_dot_center = 2*n-3

min_plus = 1
max_plus = 4*n-7

min_dot_left_right=1
max_dot_lef_right = n-1

def left_dot(value):
    for i in range(value):
        print(".",end='')
    print("*",end='')

def center(value,str):
    for i in range (value):
        print(str,end='')

def right_dot(max,i):
    if not(i+1==max_lines):
        print("*",end='')
    for i in range(max):
        print(".",end='')

def plus(method,min,i):
    if(method == "left"):
        for i in range(min):
            print("+",end='')
        print("*",end='')
    elif(method == "right"):
        if not(i+1 == n):
            print("*",end='')
        for i in range(min):
            print("+",end='')

for i in range(max_lines):
    if(i+1<=n):
        left_dot(max_dot_lef_right)
        if(i>=1):
            plus("left",min_plus,i)
        center(max_dot_center,".")
        if(i>=1):
            plus("right",min_plus,i)
        right_dot(max_dot_lef_right,i)

        max_dot_lef_right-=1
        max_dot_center-=2
        if(i>=1):
            min_plus += 2

    if(i+1>n):
        left_dot(min_dot_left_right)
        center(max_plus,"+")
        right_dot(min_dot_left_right,i)

        min_dot_left_right+=1
        max_plus -= 2
        pass
    
    print("")
