#Enter Input : Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
# == results ==
# ['Manchester United', {'points': 95}, {'gd': 68}]
# ['Arsenal', {'points': 80}, {'gd': 69}]
# ['Chelsea', {'points': 74}, {'gd': 69}]

inp = input("Enter Input : ").split("/")
list_inp = []
for i in inp:
    i = i.split(",")
    list_inp.append([i[0],{"points":int(i[1])*3 + int(i[2])*0 +  int(i[3])*1} , {"gd"   : int(i[4]) - int(i[5])}])

def buble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1): 
            if x[j][1]["points"] < x[j+1][1]["points"]:
                x[j], x[j+1] = x[j+1], x[j]
            elif x[j][1]["points"] == x[j+1][1]["points"]:
                if x[j][2]["gd"] < x[j+1][2]["gd"]:
                    x[j], x[j+1] = x[j+1], x[j]
    return x

buble_sort(list_inp)
print("== results ==")
for i in list_inp:
    print(i)