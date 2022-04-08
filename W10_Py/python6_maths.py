
def func1():
    print ("I'm a function")
    
    
def func2(arg1, arg2):
    print (arg1, "also a", arg2)
    
    
def cube(x):
    return x*x*x
    
    
def power(num , x=2):
    result=10
    for i in range(x):
       result = result*num         # num = first argument in print power(2)
    return result                   # 2 * x(2) = 4
                                    # 4* result (10) = 40 
                                    

def multiAdd(*args):
    result = 0
    for x in args:
        result=result+x
    return result


func1()
func2("I'm", "function")            # numbers -> func2(10, 20) 

print (cube(3))
print ("This is cube 3: " , cube(3))

print("Power: " , power(2))         # 2 (*2 = 4) = num  (*10 = 40) 
print("Power: " , power(2, 3))      # num = 2, x = 3 (8)  * 10 = 80 
print("Power: " , power(x=2, num=3))    # opposite args

print ("As many as...: " , multiAdd(10, 10, 10, 1))

