from FlightLib import LedLib as led
import socket
sock=socket.socket()
sock.connect(('192.168.1.5', 35001))


while True:
    data = str(sock.recv(1024))
   
    try:
        if '$$' in data:
            eval(str(data[ : data.index(b'$$')]))

    except():
        print('er')
sock.close()

