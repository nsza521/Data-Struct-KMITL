
def asteroid_collision(asts,index=0):

    def compare_size(x1,x2):
        if(abs(x1)>abs(x2)):
            return 1
        elif(abs(x1)<abs(x2)):
            return 0
        else :
            return "Both Remove"
        
    def compare_sign(x,y):
        if(x>0 and y<0):
            return True
        return False

    try:
        if(compare_sign(asts[index],asts[index+1])):
            x = compare_size(asts[index],asts[index+1])
            if(x == "Both Remove"):
                asts.remove(asts[index])
                asts.remove(asts[index])
            else:
                asts.pop(index+x)
            index = 0
            return asteroid_collision(asts,index)
        else:
            index += 1
            return asteroid_collision(asts,index)
    except:
        return asts
        

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))