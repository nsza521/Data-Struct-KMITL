def perket(nums, s=1, b=0, index=0,flag = True):
    if index == len(nums):
        if flag:
            return 1000000001
        return abs(s - b)
    num = nums[index].split(" ")
    include_current = perket(nums, s * int(num[0]), b + int(num[1]), index + 1,False)
    exclude_current = perket(nums, s, b, index + 1,flag)
    
    return min(include_current, exclude_current)

ingredient_list = input("Enter Input : ").split(",")
result = perket(ingredient_list)
print(result)