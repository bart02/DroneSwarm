from FlightLib import FlightLib as f
f.init('server')

from FlightLib import LedLib as led

n=True
import socket
sock=socket.socket()
sock.connect(('192.168.1.6', 35001))

try:
    while True:
        data = str(sock.recv(1024))
        print(data)
        try:
            n=eval(str(data))
            socket.send(data+str(n))
        except Exception as e:
            print(e)
    sock.close()
except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()

