from FlightLib import FlightLib as f
f.init('server')
# from FlightLib import TelemLib
from FlightLib import LedLib as led
from time import sleep
import socket
import sys


n = True

while True:
    try:
        sock = socket.socket()
        sock.connect(('192.168.1.6', 35001))
    except socket.error:
        print "No connection. Sleep 10 secs."
        sleep(10)
    else:
        break
sq = []

try:
    while True:
        data = str(sock.recv(1024))
        try:
            sq = data.split('$$')
            for i in range(len(sq)-1):
                print sq[i]
                n = eval(sq[i])
                sock.send(bytes(sq[i]+str(n)))

        except Exception as e:
            print(e)

except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()

