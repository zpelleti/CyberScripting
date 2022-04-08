
# socket = endpoints that receive the data
## Server side: 
# 

#server.py file
import socket
from project3560 import main   ## (encryptedFile)
import pymongo
from pymongo import MongoClient
from cryptography.fernet import Fernet


dbconnection = pymongo.MongoClient("mongodb+srv://project3560:williammario@cluster0.zqsmp.mongodb.net/encryptdecrypt?retryWrites=true&w=majority")
db = dbconnection["encryptdecrypt"]
dbcollection = db["keycontainer"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.31.32.126' # private ip4 cloud9
port = 55555
s.bind((host, port))
s.listen(5) 
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
#=========================================================
    
def sendDoc(encryptedFile):
    print("Data: ", encryptedFile)
    c.send(b'Thank you for connecting', encryptedFile)   # file to be sent  
    c.close()


# sendDoc(encryptedFile)




