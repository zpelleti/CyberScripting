# mongodb Atlas: https://account.mongodb.com/account/login
# creating a database user: https://docs.atlas.mongodb.com/security-add-mongodb-users/

# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]


import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://scriptForCyber:Pa55word01@cluster0.lk1ed.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #"mongodb+srv://scriptForCyber:Pa55word01@cluster0-34sac.mongodb.net/")
db = dbconnection["MyDB"]
dbcollection = db["movies"]


def main():
    x = {}
    
    # you can use input to get data from user
    name = 'Jack'    
    lastname = 'Frost'
    age = 20

    x["name"] = name 
    x["lastname"] = lastname
    x["age"] = age
    
    print (x)  # just to see the format
    
    oID = dbcollection.insert_one(x)

    print(oID.inserted_id) # displaying the id of the newly created document
    
    show_alldata()
    
    


def show_alldata():
    theMovie = list(dbcollection.find({}).limit(20))
    display(theMovie)
    
def display(data):
    print (data)
    
if __name__ == '__main__':
    main()
