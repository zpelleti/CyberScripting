
def main():
    print("The sum of 10 + 46 is: ")
    show_sum(10, 46)

    show_interest(rate = 0.01, period = 10, principal = 10000.0)
    firstName, lastName = getNames() 
    print(f"Billie Jean: {firstName} {lastName}")
    

def show_sum(num1, num2):
    result = num1+num2
    print(result)

def show_interest(principal, rate, period):
    interest = principal*rate*period
    print(f"The interest will be: ${interest:,.2f}.")
    
def getNames():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    return firstName, lastName

if __name__ == "__main__":
    main()
    