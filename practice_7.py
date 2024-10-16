a = [1, 3, 4, 5, 17, 18, 31, 33, 35]

def searchR(low, high, x):
    if high < low:
        return -1
    mid = (low + high) // 2
    if x == a[mid]:
        return mid
    elif a[mid] < x:
        return searchR(mid + 1, high, x)
    else:
        return searchR(low, mid - 1, x)

print(searchR(0, 8, 17))