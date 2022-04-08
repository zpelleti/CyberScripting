

## Use of IN operator used with lists:

def main():
    
    # create a list of product numbers: 
    prodNum = ['V458', 'F890', 'Q543', 'R657']
    
    # print a user input/search option:
    userIn = input("Search prod number: ")
    
    # search list for input: 
    if userIn in prodNum:
        print(f"{userIn} was found")
    else:
        print(f"{userIn} was not found")
        
        
if __name__ == "__main__":
    main()

