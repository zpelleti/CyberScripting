## create db + generate key 

## username: project3560
## passwd: williammario

import pymongo
from pymongo import MongoClient
import json
from cryptography.fernet import Fernet
import random




# file = open('newKey.txt', 'wb')
#file.write(key)
#file.close()



dbconnection = pymongo.MongoClient("mongodb+srv://project3560:williammario@cluster0.zqsmp.mongodb.net/encryptdecrypt?retryWrites=true&w=majority")
db = dbconnection["encryptdecrypt"]
dbcollection = db["keycontainer"]


def main():
    
    key = Fernet.generate_key()


# open file to encrypt:
    with open('file.txt', 'rb') as f:
        data = f.read()
    
# create Fernet object and encrypt the file with the generated key
    fernet = Fernet(key)
    encryptedFile = fernet.encrypt(data)
    
   # decode the key from byte to str:
    decodedKey = key.decode()

    #create a random number
    ranNum = random.random()
    
    
    # send the key + randnum to mongo
    post = {"key":decodedKey,"ranNum":ranNum}
    dbcollection.insert_one(post)

    # read back from mongodb and convert the key from string to bytes
    #result = dbcollection.find_one({"ranNum": ranNum})
    # encode to byte:
    #keyfrommogo = result["key"].encode()
    
    # other fernet object - decrypted file 
    # fernet2 = Fernet(keyfrommogo)
    # decryptedFile = fernet2.decrypt(encryptedFile)
    # decodedFile = decryptedFile.decode()
    # print(decodedFile, ranNum)
    

    return encryptedFile


if __name__ == '__main__':
    main()
