def main():
    x = 0
    
    while(x < 5):
        print (x)
        x += 1
        
    print("range:2-10")
    for x in range(2,10):
        print(x)
    
    print("\nrange:2-10-3")
    for x in range(2,10,3):         # last digit = in range 1 to 10, every x (3rd) values
        print(x)
        
    # for collection (array) , use for loop to print all:
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for value in days:
        print(value)
    #    print(days)     # prints whole array 
        
    # use of break & continue statements:
    for x in range(2,10):
        if(x == 7):break        # stops looping through range at 7
        print(x)  
    
    # use of two output values = row number + value (can be any letter - not rn)
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for rn, value in enumerate(days):
       print (rn,value)
       
       
if __name__ == "__main__":        
    main()
