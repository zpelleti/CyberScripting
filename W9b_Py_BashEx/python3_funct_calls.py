
def someFunction():                         # def = function
    f = "def"
    print ("Inside the f function: ", f)      # indentation is essential indide function
    

someFunction()                              # function call

#====================================

f = 10                       # new initialization for f
print ("After init: ", f)       # prints value
print (type(f))                 # prints type


f = "Pat"
print (f, type(f))           # same variable different value

print ("String type: " + str(123))  # str() acts as " " 
print ("String type: " + "123")     # same result 

someFunction()      # calling again

print ("After function call 2: f = ", f)

#del f               # removes the variable 

print (f)           # returns error after del f 






