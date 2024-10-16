number = int(input("Enter Number : "))
digit = number
number = (2 ** number)-1

def recursive(number,digit,start_number = 0):
    if(digit < 0):
        return "Only Positive & Zero Number ! ! !"
    else :
        if(digit == 1):
            print("0")
            return format(start_number+1, f'0{digit}b')
        else:
            if(start_number>=number):
                return format(start_number, f'0{digit}b')
            else:
                print(format(start_number, f'0{digit}b'))
                start_number += 1
                return recursive(number,digit,start_number)
    
print(recursive(number,digit))