
import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://scriptForCyber:Pa55word01@cluster0.ulnvp.mongodb.net/")
db = dbconnection["MyDB_300325896"]
dbcollection = db["MyFriends_300325896"]

#app.config["MONGO_URI"] = "mongodb+srv://myuser:mypassword@cluster0-34sac.mongodb.net/sample_mflix?retryWrites=true&w=majority" # replace the URI with your own connection
#mongo = PyMongo(app)


def main():
    answer="0"
    # Opening JSON file
    with open('CARS.json') as json_file:
        data = json.load(json_file)
    dbcollection.create_index("id",unique=True)
    try:
        dbcollection.insert_many(data, ordered=False)
    except Exception:
        pass
    
    while answer != '3':
        showMenu()
        answer = input('Pick [1-3] : ')
        
        if (answer == '1'):
            addData()
        elif (answer == '2'):
            displayData()
        elif (answer =='3'):
            quit()
    
def showMenu():
    print ("1] Add another document")
    print ("2] Display")
    print ("3] Exit")
    
def addData():
    firstName = input('Enter the first name: ')
    lastName = input('Enter the last name: ')
    noOfCars = int(input('Enter the number of cars you would like to add: '))
    carMake=''
    for i in range(noOfCars):
        car=input('Enter car ' + str(i+1) +': ')
        carMake+='{"make":"'+car+'"}'
        if (i+1!=noOfCars):
            carMake+=','
            
    uid = dbcollection.find_one(sort=[("id", pymongo.DESCENDING)])
    
    x={}
    x["id"] = uid["id"]+1
    x["first_name"] = firstName
    x["last_name"] = lastName
    x["cars"] = json.loads("[{}]".format(carMake))
    dbcollection.insert_one(x)
    
def displayData():
    data = dbcollection.find({}).limit(20)
    print('{:25s}{:25s}{:15s}'.format("First Name","Last Name","Cars"))
    for d in data:
        car=""
        print('{:25s}{:25s}'.format(d["first_name"],d["last_name"]),end='')
        for c in range(len(d["cars"])):
            v=d["cars"][c]["make"]
            car+=v+"\n"+"".ljust(50)
        print('{:5s}'.format(car))
    
if __name__ == '__main__':
    main()
