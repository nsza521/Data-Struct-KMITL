ary = [1,2,3,7,8,9]
def sum_ary(ary):
    if len(ary) == 1:
        return ary[0]
    else:
        return ary[0] + sum_ary(ary[1:]) 
print(sum_ary(ary))