import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('101.34.28.245',8000))

s.send(b'Connect sucessfully\n')
s.send(b'q')
