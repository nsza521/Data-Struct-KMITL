def length(txt):
    if(txt[1:]==""):
        return 1
    else:
        return length(txt[1:]) + 1
    
    
print(length(input("Enter Input : ")))