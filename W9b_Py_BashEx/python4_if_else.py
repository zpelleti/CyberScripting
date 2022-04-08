
def main():
    x = 1000
    y = 100
# OR: x, y = 10, 100 

    print (f'x = {x:5d} , y = {y:7.2f}')  # first f = 'format' 
                                          # first format: x = 5 digits
                                          # sec: y = 7 digits, 2 decimals (float)
    if (x < y):
        mess = "x is less than y"
    elif (x == y):
        mess = "x is equal to y"
    else:
        mess = "x is greater than..."
    
    print (mess)

print (__name__)
if __name__ == "__main__":          # __name__ = good for identifying the
                                   # primary function / code 
    main()

