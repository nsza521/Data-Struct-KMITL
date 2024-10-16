def find_triplets(arr):
    arr = sorted(arr)
    n = len(arr)
    triplets = []

    if n < 3:
        return "Array Input Length Must More Than 2"

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets

arr = list(map(int, input("Enter Your List : ").split()))
result = find_triplets(arr)
print(result)
