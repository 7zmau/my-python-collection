import socket

def revNum(n):
    rev = 0
    while n != 0:
        r = n%10
        rev = r + rev*10
        n=n//10
    return rev
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))

serversocket.listen(1)
clientsocket, addr = serversocket.accept()

while True:
    data = clientsocket.recv(1024).decode()
    if not data:
        break
    print("Data from client: ", data)
    data = revNum(int(data))
    data = str(data)
    clientsocket.send(data.encode())
    
clientsocket.close()
