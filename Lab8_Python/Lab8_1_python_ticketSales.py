
def seatings():
    
    print ("How many tickets were sold from each class?")
    
    classA = 20
    classB = 15
    classC = 10
    
    inputA = int(input("Tickets total cat. A: "))
    inputB = int(input("Tickets total cat. B: "))
    inputC = int(input("Tickets total cat. C: "))
    
   
    print ("The total income generated from ticket sales:\n")
    print ("Class A: $", classA * inputA)
    print ("Class B: $", classB * inputB)
    print ("Class C: $", classC * inputC)

seatings()

