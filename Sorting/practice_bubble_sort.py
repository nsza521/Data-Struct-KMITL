x = input("Enter input : ").split()
x = list(map(int,x))

# ------------------------------------------------------------------------------------------------

# Time Complex of This Recursive Code is O(n^2)
def _recursive_buble_sort(x,i=0):
    if (i+1>=len(x)):
        return x
    if(x[i]>x[i+1]):
        x[i] , x[i+1] = x[i+1] , x[i]

    return _recursive_buble_sort(x,i+1)

def recursive_buble_sort(x,n=None):
    if n == None:
        n = len(x)
    if n == 1:
        return x
    
    x = _recursive_buble_sort(x)
    return recursive_buble_sort(x,n-1)

y = recursive_buble_sort(x)
print(y)

# ------------------------------------------------------------------------------------------------

# Time Complex of Normal Code is O(n^2) too
def normal_buble_sort(x):
    n = len(x)
    for i in x:
        for j in range(n-1):
            if x[j] > x[j+1]:
                y = x[j]
                x[j] = x[j+1]
                x[j+1] = y
    return x
        
y = normal_buble_sort(x)
print(y)

def buble_sort_again(x):
    n = len(x)
    for i in range(n):
        for j in range(0,n-i-1):
            if x[j] > x[j+1]:
                x[j] , x[j+1] = x[j+1] , x[j]
    return x
y = buble_sort_again(x)
print(y)