from FlightLib import LedLib as led
import socket
sock=socket.socket()
sock.connect(('192.168.1.5', 35001))


while True:
    data = str(sock.recv(1024))

    try:
        eval(str(data))

    except:
        print('er')
sock.close()

