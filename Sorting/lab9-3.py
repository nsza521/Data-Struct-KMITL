def digits_to_list(num):
    num = str(num)
    digits_list = [int(char) for char in num]
    return digits_list

inp = input("Enter Input : ")
list_inp = digits_to_list(inp)

def buble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1): 
            if x[j] > x[j+1]:
                x[j] , x[j+1] = x[j+1] , x[j]
    return x

def buble_sort_rev(x):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1): 
            if x[j] < x[j+1]:
                x[j] , x[j+1] = x[j+1] , x[j]
    return x

def something_drome(list_inp):
    if len(set(list_inp)) == 1:
        return "Repdrome"
    
    copy_inp = list_inp[:]
    buble_sort(list_inp)
    
    if(copy_inp == list_inp):
        if(len(set(copy_inp)) == len(list_inp)):
            return "Metadrome"
        else:
            return "Plaindrome"
        
    buble_sort_rev(list_inp)

    if(copy_inp == list_inp):
        if(len(set(copy_inp)) == len(list_inp)):
            return "Katadrome"
        else:
            return "Nialpdrome"
        
    return "Nondrome"

print(something_drome(list_inp))