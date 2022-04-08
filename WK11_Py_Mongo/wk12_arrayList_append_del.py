## program to create list + append, update, delete by index, delete by name 



# create food list auto increased array:
foodList = []

def main():
    userIn = "0"
    while userIn != "7":
        showMenu()
        userIn = input("Pick [1-7]")
        
        if(userIn == '1'):
            appendData()
        elif(userIn == '2'):
            updateData()
        elif(userIn == '3'):
            deleteData("itemValue")
        elif(userIn == '4'):
            deleteData("position")
        elif(userIn == '5'):
            insertData()
        elif(userIn == '6'):
            pass    # exit()
                            
            display()
    
def showMenu():
    print ("1] Append")
    print ("2] Update")
    print ("3] Delete by item value")
    print ("4] Delete by position")
    print ("5] Insert")
    print ("6] Search")
    print ("7] Exit")
    
def appendData():
    data = input("Enter food name: ")
    print('\n')
    foodList.append(data)
    
def insertData():
    data = input("Enter food name: ")
    index = input("Where index value is :")
    foodList.insert(index, data)
    
def updateData():
    data1 = input("Enter former food: ")
    data2 = input("Enter new food: ")
    index = searchData(data1)    # returns value of index
    
    if (index == -1):
        print("Food not found")
    else:
        foodList[index] = data2  # new value overrides
        
def searchData(food):
    if food not in foodList:
        return -1
    else:
        return foodList.index(food)

# the two ways of searching & deleting data: 
# by value - str - and by index - int 
def deleteData(code):
    
    if(code == "itemValue"):
        data1 = input("Enter food to be deleted: ")
        if data1 in foodList:
            foodList.remove(data1)
            
    elif(code == "position"):
        data1 = int(input("Enter index to be deleted: "))
        if(data1 >= 0 and data1 < len(foodList)):
            del foodList[data1]
            
def display():
    print("\nContents of list: ")
    print(f"Food list: {foodList}")
    print(f'Length of list: {len(foodList)}')
    

if __name__ == '__main__':
    main()
    