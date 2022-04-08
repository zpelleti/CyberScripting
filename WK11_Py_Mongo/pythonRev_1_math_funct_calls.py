num1 = 0
FACTOR = 3      ## global constants

def main():
    global num1
    num1 = int(input("Enter a number: "))
    
    value = 15
    dblMe(value)
    
    multiMe()
    print(f"The new value of num1: {num1} -> userInput")
    print(f"FACTOR is {FACTOR} -> global constant")
    
    texas()
    cali()
    
def dblMe(num2):
    result = num2*2
    print("Inside dblMe: [{:>5d}] -> value=15 (num2*2)".format(result))
    
def multiMe():
    global num1
    #global FACTOR      # -> uncommented: FACTOR = 2
    FACTOR = 2
    
    print(f"The number you entered is {num1}")
    
    num1*=FACTOR        # -> num1 = userInput from main() (global)
    
def texas():
    specialty = "Barbecue"
    print(f"Texas has {specialty}")

def cali():
    specialty = "Salsa"
    print(f"Cali has {specialty}")
    
if __name__ == "__main__":
    main()    
    

