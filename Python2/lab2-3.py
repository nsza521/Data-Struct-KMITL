def new_range():
    start, end, step = 0.0, 0.0, 1.0
    
    if num_values == 1:
        end = float(values[0])
    elif num_values == 2:
        start = float(values[0])
        end = float(values[1])
    elif num_values == 3:
        start = float(values[0])
        end = float(values[1])
        step = float(values[2])

    print("(", end='')  

    current = start
    while current < end:
        if(decimal_default_max != 0):
            x = f"{current:.{decimal_default_max}f}".rstrip('0').rstrip('.')
            if(len(x) == 1):
                print(f"{float(x):.1f}",end="")
            else:
                print(x,end="")
        else:
            print(f"{current:.{decimal_default}f}",end="")
        current += step
        if current < end:
            print(", ", end='') 

    print(")")

print("*** New Range ***")
user_input = input("Enter Input : ")

values = user_input.split()
num_values = len(values)
decimal_default = 1
decimal_default_max = 0
try :
    decimal_default = len((values[0].split("."))[1])
    max = len((values[2].split("."))[1])
    if(max > decimal_default):
        decimal_default_max = max
except:
    pass
new_range()