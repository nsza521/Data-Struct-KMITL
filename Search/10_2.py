def first_greater(sorted_arr, x):
    l = 0
    r = len(sorted_arr) - 1
    result = None

    while l <= r:
        mid = (l + r) // 2
        if sorted_arr[mid] > x:
            result = sorted_arr[mid]
            r = mid - 1
        else:
            l = mid + 1

    if result is not None:
        return result
    else:
        return "No First Greater Value"

# 2 3 6 7 8

inp = input('Enter Input : ').split('/')
left = list(map(int, inp[0].split()))
right = list(map(int, inp[1].split()))

sorted_left = sorted(left)

results = []
for x in right:
    res = first_greater(sorted_left, x)
    results.append(str(res))

for i in results:
    print(i)