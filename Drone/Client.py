from FlightLib import FlightLib as f
f.init('server')

from FlightLib import TelemLib as tem


from FlightLib import LedLib as led

n = True

import socket

sock = socket.socket()
sock.connect(('192.168.1.6', 35001))
sq = []

try:
    while True:
        data = str(sock.recv(1024))
        print(data)
        try:
            sq = data.split('$$')
            tem.telemetry_thread()
            for i in range(len(sq)-1):
                n = eval(sq[i])
                sock.send(bytes(sq[i]+str(n), 'utf-8'))

        except Exception as e:
            print(e)

except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()

