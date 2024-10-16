inp = input("Enter list  of numbers: ").split()
inp = list(map(int,inp))
inp_dict = {}

for i in inp:
    if i not in inp_dict:
        inp_dict[i] = 1
    else :
        inp_dict[i] += 1

def buble_sort(x):
    items = list(x.items())
    for i in range(len(items)):
        for j in range(0,len(items)-i-1):
            if items[j+1][1] > items[j][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

result = buble_sort(inp_dict)

for i in range(len(result)):
    print(f"number {result[i][0]}, total: {result[i][1]}")