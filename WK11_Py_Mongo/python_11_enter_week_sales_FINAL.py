##   Program adding user entered sales for a period of two months:

## ========================================= in FINAL EXAM =================================================

def main():
    Sales1 = getSales("Month 1")  
    Sales2 = getSales("Month 2")
    
    print(f"Values entered week 1: {Sales1}")   
    print(f"Values entered week 2: {Sales2}")

    SalesTotal = Sales1 + Sales2
    
    for value in SalesTotal:
        print(value)
        
def getSales(title):
    
    Sales = []   ## array automaticcaly expanding if again.upper == "Y" is entered
    counter = 0
    
    print (title)
    print("Enter sales for each day: ")
    
    ## get sales for each day:
    again = "y"
    
    while again.lower() == "y":    ## OR again.upper == 'Y' 
        ## capture num and append to list:
        num = float(input(f"Day #{counter + 1}: "))
        Sales.append(num)   ## OR: Sales[ind] = num   
        counter += 1
        
        print("Do you wish to add another number?: ")
        again = input("y = yes, n = no\n")

    return Sales   ## after arrays are built, return them to Month 1 or 2

if __name__ == "__main__":
    main()
    
    