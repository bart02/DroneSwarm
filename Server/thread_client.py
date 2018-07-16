import socket
import os
import time
from threading import Thread

sock = socket.socket()
sock.connect(('192.168.1.6', 35002))
# 10.23.45.159


def telemetry_thread():
    data = b''
    sck1 = socket.socket()
    sck1.connect(('192.168.1.6', 35002))
    while True:
        sck1.send(b'2')


t_t = Thread(target=telemetry_thread)
t_t.daemon = True
t_t.start()


while True:
    try:
        sock.send(b'1')
    except:
        # time.sleep(0.1)
        pass
conn.close()


