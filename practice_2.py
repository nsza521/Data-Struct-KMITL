def harmonic_sum(num , n=1):
    if n > num:
        return 0
    else:
        if n==1:
            print(1,end='')
            answer = 1 + harmonic_sum(num,n+1)
        else:
            print(f" + 1/{n}",end='')
            answer = 1/n + harmonic_sum(num,n+1)
        return answer
print()
num = int(input("input = "))
print(" = "+str(harmonic_sum(num)))



# chatgpt code lol im better
# # def harmonic_sum(n, num):
#     if n > num:  # Base case: if n exceeds num, return 0 to stop recursion
#         return 0
#     else:
#         if n == 1:
#             print("1", end='')
#         else:
#             print(f" + 1/{n}", end='')
        
#         return 1/n + harmonic_sum(n + 1, num)

# # Main program
# num = int(input("Input: "))
# print(" =", harmonic_sum(1, num))