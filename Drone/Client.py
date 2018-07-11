from FlightLib import FlightLib as f
f.init()

from FlightLib import LedLib as led


import socket
sock=socket.socket()
sock.connect(('192.168.1.6', 35001))

try:
    while True:
        data = str(sock.recv(1024))
        print(data)
        try:
            eval(str(data))

        except:
            print('er')
    sock.close()
except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()

