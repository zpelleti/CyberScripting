# mongodb Atlas: https://account.mongodb.com/account/login
# creating a database user: https://docs.atlas.mongodb.com/security-add-mongodb-users/

# Windows : python -m pip install pymongo[srv]
# Linux : sudo pip3 install pymongo[srv]


import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://scriptForCyber:Pa55word01@cluster0.lk1ed.mongodb.net/")
db = dbconnection["MyDB"]
dbcollection = db["employee"]

# https://www.mockaroo.com/

def main():
    x = '{"id":11, "name":"Charlie","salary":"$45.43"}'
    print (type(x))
    x = json.loads(x) # converts the string to dictionary
    print (type(x))     ## shows type conversion ( <class 'dict'> )
    
    # Opening JSON file
    with open('emp.json') as json_file:
        data = json.load(json_file)
  
    dbcollection.insert_one(x) 
    
    
    print("\n",data)
    dbcollection.insert_many(data)
      
    show_alldata()
    
    


def show_alldata():
    rData = list(dbcollection.find({}).limit(20))
    display(rData)
    
def display(data):
    print (data)
    
if __name__ == '__main__':
    main()
