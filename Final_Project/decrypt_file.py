
from cryptography.fernet import Fernet

# get key from file:
file = open('key.key', 'rb')
key = file.read()
file.close()

# open file to decrypt:
with open('CARS.json.encrypted', 'rb') as f:
    data = f.read()
    

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

# write file back out:
with open('CARS.json.decrypted', 'wb') as f:
    f.write(encrypted)
    

