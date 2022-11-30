# -*- coding: utf-8 -*-
import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if indata.decode() == 'EXIT':
            conn.close()
            print('client closed connection.')
            print('wait for connection...')
            break
        else:
            print(str(addr)+ ':' + indata.decode())
            outdata = indata.decode()
            conn.send(outdata.encode())

