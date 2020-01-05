import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port = 9999
s.connect((host, port))

msg = input('-->')
while msg != 'q':
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print('Number in reverse: ' + data)
    msg = input('-->')

s.close()
