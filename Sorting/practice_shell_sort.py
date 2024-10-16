arr = [1,3,2,1,4,6,31,12,9,2,1]
def shell_sort(arr):
    n = len(arr)
    gap = n // 2


    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 

print("Original array:", arr)
shell_sort(arr)
print("Sorted array:", arr)

arr = [1,3,2,1,4,6,31,12,9,2,1]

def shell_sort_again(arr):
    n = len(arr)
    gap = n/2

    while gap>0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j > gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j-= gap
            arr[j] = temp
        gap//2
        