def fac(n):
    if n==0 or n==1:
        return 1
    else:
        x = fac(n-1)
        return n*x
print(fac(4))