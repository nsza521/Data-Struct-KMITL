x = input("Enter input : ").split()
x = list(map(int,x))

# ------------------------------------------------------------------------------------------------
def insertion_sort(x):
    for i in range(1,len(x)):
        j = i
        while j > 0 and x[j-1] > x[j]:
            x[j-1] , x[j] = x[j] , x[j-1]
            j=j-1
    return x

y = insertion_sort(x)
print(y)

# ------------------------------------------------------------------------------------------------

def insertion_sort_again(x):
    for i in range(1,len(x)):
        j = 1
        while j>0 and x[j-1] > x[j]:
            x[j-1] , x[j] = x[j] , x[j-1]
            j = j-1
    return x
y = insertion_sort_again(x)
print(y)
