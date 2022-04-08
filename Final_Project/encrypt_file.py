
from cryptography.fernet import Fernet

# get user key from file:
file = open('key.key', 'rb')
key = file.read()
file.close()


# open file to encrypt:
with open('CARS.json', 'rb') as f:
    data = f.read()
    
# create Fernet object:
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# write encrypted data to a new file:
with open('CARS.json.encrypted', 'wb') as f:
    f.write(encrypted)
    
    
