l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Insertion Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    

def insertion_sort(x):
    for i in range(1,len(x)):
        j = i
        while j > 0 and x[j-1] > x[j]:
            x[j-1] , x[j] = x[j] , x[j-1]
            j=j-1 
    return x
 
def mediean(x):
    n = len(x)
    if n % 2 == 1:
        return x[n//2]
    else:
        mid , mid2 = x[n // 2 - 1], x[n // 2]
        return (mid + mid2) / 2

lst = []
for i in l:
    lst.append(i)
    result = lst[:]
    result_sort = insertion_sort(result)
    meadian = mediean(result_sort)
    print(f"list = {lst} : median = {meadian:.1f}")