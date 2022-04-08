
def main():
    print("Please enter the wall space you need painted - in sq. feet")
    sqFeet = int(input())
    print("Please enter the price per gallon:")
    ppg = int(input())
    
    
    calculate(sqFeet, ppg)
    
def calculate(sqFeet, ppg):
    # per 112 sqFeet = 1 gallon =  $35.00/8hrs labor
    
    numGall = sqFeet/115
    print (f'Number of gallons required:{numGall:5.2f} gals')
    hrs = numGall*8
    print (f'Number of hours required: {hrs:2.2} hrs')
    totPpg = ppg*numGall
    print (f'Price for total paint:${totPpg:5.2f}')
    totLab = hrs*35.00
    print (f'Price for total labor:${totLab:5.2f}')
    print ("===========================================")
    totJob = numGall+hrs+totPpg+totLab
    print (f'Total price for job:${totJob:5.2f}')
    

main()


    





