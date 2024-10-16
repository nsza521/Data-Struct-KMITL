x = input("Enter input : ").split()
x = list(map(int,x))

# ------------------------------------------------------------------------------------------------

 

# ------------------------------------------------------------------------------------------------

# Time Complex of This Recursive Code is O(n^2) too BRUH
def selection_sort_recursive(x,n=0):
    if n is None:
        n = len(x)
    if n >= len(x):
        return x
    min = n

    for j in range(n+1,len(x)):
        if x[min] > x[j]:
            min = j
    if n!=min:
        x[n] , x[min] = x[min] , x[n]

    return selection_sort_recursive(x,n+1)

y = selection_sort_recursive(x)
print(y)

# ------------------------------------------------------------------------------------------------
# Most to Least
def again_selection_sort_2(x):
    for i in range(len(x)):
        min = i
        for j in range(i+1,len(x)):
            if x[min] < x[j]:
                min = j
        if min != i:
            x[min],x[i] = x[i] , x[min]
    return x

y = again_selection_sort_2(x)
print(y)

def again_selection_sort_3(x):
    for i in range(len(x)):
        min = i
        for j in range(i+1,len(x)):
            if x[j] > x[min]:
                min = j
        if min != i:
            x[min],x[i] = x[i] , x[min]
    return x
y = again_selection_sort_3(x)
print(y)

    