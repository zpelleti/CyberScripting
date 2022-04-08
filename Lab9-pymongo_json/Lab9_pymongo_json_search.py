import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://scriptForCyber:Pa55word01@cluster0.lk1ed.mongodb.net/")
db = dbconnection["MyDB_300325896"]
dbcollection = db["MyFriends_300325896"]


def main():
    
    userIn = "0"
    ## open json file: 
    with open('CARS.json') as json_file:
        data = json.load(json_file)
    ## create index:
    dbcollection.create_index("id", unique = True)  
    try:
        dbcollection.insert_many(data, ordered = False)  ## 
    except Exception:
        pass
    
    userIn = str(input("================\n Please make your choice: " 
                                        + "\n1 Add Data" 
                                        + "\n2 Display Data" 
                                        + "\n3 Exit" 
                                        + "\n================\n"))
    if(userIn == '1'):
        add_data()
    elif(userIn == '2'):
        show_all_data()
    else:
        print("Goodbye...")
        exit()
    
    
def add_data():

    firstName = str(input("Enter first name: "))
    lastName = str(input("Enter last name: "))
    numCars  = int(input("Enter number of cars: "))
    carMake = ""
    
    for i in range(numCars):
        cars = input("Enter car type: " + str(i+1) + ": ")  ## start id at 1
        carMake = carMake + '{"make": "' + cars + '"}'
        if(i+1 != numCars):
            carMake+= ", "
            
    ## adds 1 to the highest id
    newId = dbcollection.find_one(sort=[("id", pymongo.DESCENDING)])
    
    new = {}
    ## create unique id:
    new["id"] = newId["id"]+1
    
    new["first_name"] = firstName
    new["last_name"] = lastName
    
    new["cars"] = json.loads("[{}]".format(carMake))
    dbcollection.insert_one(new)
    
    main()
    
   
def show_all_data():
    data = dbcollection.find({}).limit(20)
    print('{:25s}{:25s}{:15s}'.format("First Name","Last Name","Cars\n"))

    for mak in data:
        car = ""  ## ?? 
        print('{:25s}{:25s}'.format(mak["first_name"],mak["last_name"]),end='')

        for car in range(len(mak["cars"])):
            carObj = mak["cars"][car]["make"]
            car+= carObj +"\n"+"".ljust(50)

        print('{:5s}'.format(car))      
        
    
    main()
    
if __name__ == '__main__':
    main()  