def fac(num):
    if num < 2:
        return 1
    else:
        return num * fac(num-1)

num = int(input("input num : "))
print(f"{num}! = "+str(fac(num)))

# better code bro im forget
# def fac(n):
#     if n < 2:
#         return 1
#     return n * fac(n-1)

# num = input("Enter Number : ")
# num = int(num)
# print(str(num)+"! = "+str(fac(num)))