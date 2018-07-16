import socket
import os
import time

sock = socket.socket()
sock.connect(('192.168.1.6', 35001))
# 10.23.45.159

data = r''
while True:

    sock.setblocking(False)

    try:

        data = sock.recv(2048)
        data = r''
    except:
        pass

    try:
        sock.send(b'test_client')
    except:
        # time.sleep(0.1)
        pass
conn.close()
