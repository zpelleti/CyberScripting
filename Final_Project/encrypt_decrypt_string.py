# terminal install: python -m pip install cryptography

from cryptography.fernet import Fernet


## First: Generate unique user key:

# # key = automatic gen. bytes object of code base64 encoded string
# # (new key is generated every time the program is ran)
key = Fernet.generate_key() 


# # storing the key to be able to use it for decryption in all the other programs:
file = open('key.key', 'wb') # open file as 'write bytes'
file.write(key)
file.close()


# reading the keys:
file = open('key.key', 'rb') # open file as 'read bytes'
key = file.read()
file.close()
# key found in the file should be printed:
print("This is the user key:")
print(key, '\n')


##   send the key to mongo as .json file =====================================





## ================= Example of encryption / decryption of a user string : ==========================================================

#to encode a string:
message =  input("Enter your secret message\n")
message = "secret message"
encoded = message.encode()

# encrypt message:
f = Fernet(key)
encrypted = f.encrypt(encoded)
print("This is the encrypted message:")
print (encrypted, '\n')


# # get the key again for decrypting : 
file = open('key.key', 'rb') 
key2 = file.read()
file.close()

# decrypt the encrypted message:
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print("This is the decrypted message in byte type:")
print(decrypted, '\n') # message prints, but is still a byte object - b''


# to decode the message: 
original_message = decrypted.decode()
print("Original message after decryption:")
print(original_message, '\n')



