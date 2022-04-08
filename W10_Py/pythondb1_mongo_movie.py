# for mongodb Atlas: 
# https://account.mongodb.com/account/login
# to create new user:
# https://docs.atlas.mongodb.com/security-add-mongodb-users/
# To install+run on Windows: 
# [terminal]
# To install+run on Linux:
# [terminal] sudo pip3 install pymongo[srv]


import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://scriptForCyber:Pa55word01@cluster0.lk1ed.mongodb.net/")
db = dbconnection["sample_mflix"]
dbcollection = db["movies"]

#app.config["MONGO_URI"] = "mongodb+srv://myuser:mypassword@cluster0-34sac.mongodb.net/sample_mflix?retryWrites=true&w=majority" # replace the URI with your own connection
#mongo = PyMongo(app)
## ?? 


def main():
    show_data()
    print("=======================")
    show_alldata()
    
    
def show_data():
    theMovie = dbcollection.find({}).limit(1)    # {} = all  limit(1) = 1 result only 
    display(theMovie)
   

def show_alldata():
    ## show 20 results:
    #theMovie = list(dbcollection.find({}).limit(20))
    ## find 20 comedy results:
    #theMovie = list(dbcollection.find({"genres" : "Comedy"}).limit(20))
    
    # show 20 results data with rating greater than 7.0:
    theMovie = list(dbcollection.find({ "imdb.rating" : { "$gt" : 7.0 } }).limit(20))
    display(theMovie)
    
def display(data):
    # cast is an Array, awards is an Object
    
    cast = ""   ## ARRAY
    imdbKeys = ["rating","votes","id"]   # OBJECT
    
    ## Title Row:
    print('{:40s}{:5s}{:25s}{:15s}'.format("Title","Year","imdb","Cast(s)"))
    ## scan data from mongodb: 
    for d in data:
        # imdbValue = json.dumps(d["imdb"]) # converts dictionary to string
        # print (imdbValue)                 # if you want to see the string result
        count = 0 ;
       # imdbVal = ""
        cast = ""
        ## formatting of output data:       [0:39]= stop title at 39 char
        print('{:40s}{:<5d}'.format(d["title"][0:39],d["year"]),end='')
        #print(imdbKeys[count], d["imdb"][imdbKeys[count]])
        
        ## formatting cast - (need explanations) : 
        for c in d["cast"]:
            
            if count < len(imdbKeys):
                v = imdbKeys[count] + " : " + str(d["imdb"][imdbKeys[count]])
                cast += v + "".ljust(25-len(v)) + c + "\n" + "".ljust(45) 
                count += 1
            else:
                cast += "".ljust(25) + c + "\n" + "".ljust(70)
        for i in range(count,len(imdbKeys)):
            v = imdbKeys[i] + " : " + str(d["imdb"][imdbKeys[i]])
            cast += v + "".ljust(25-len(v)) + "\n" + "".ljust(45) 
            
        print('{:40s}'.format(cast))
    
if __name__ == '__main__':
    main()
