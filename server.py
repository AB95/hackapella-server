import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('10.83.3.175', 7000)
s.bind(address)
incoming = 0

s.listen(1)
while True:
    connection, client_address = s.accept()
    print "hi"
    incoming = connection.recv(37)
    connection.close()
    break

s.close()
print incoming
