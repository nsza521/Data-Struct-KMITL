def findMin(i,lis):

    if i == len(lis)-1:
        return i

    temp = findMin(i+1,lis)
    if lis[i] > lis[temp]:
        return temp
    else:
        return i

def Select(lis,i=0):

    if i == len(lis)-1:
        return

    temp = findMin(i,lis)
    lis[i],lis[temp] = lis[temp],lis[i]
    Select(lis,i+1)

    return lis

def Selectloop(lis):

    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            if lis[i] > lis[j]:
                lis[j],lis[i] = lis[i] , lis[j]
        
    return lis

l=[5,3,1,4,9]

print(Selectloop(l))
print(Select(l))