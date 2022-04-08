import socket




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('18.207.187.220', 55555))    # public ip4 cloud9 


msg = s.recv(1024)
print(msg.decode("utf-8"))
s.close()