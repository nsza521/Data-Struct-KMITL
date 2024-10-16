x = input("Enter Input : ").split()
x = list(map(int, x)) 

def super_recursive_loop_function_very_good(x):
    if len(x) < 2:  
        return "Yes"
    if x[0] <= x[1]:  
        return super_recursive_loop_function_very_good(x[1:]) 
    else:
        return "No"

print(super_recursive_loop_function_very_good(x))
