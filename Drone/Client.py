from FlightLib import LedLib as led
import socket
sock=socket.socket()
sock.connect(('192.168.1.5', 35001))


while True:
    data = sock.recv(1024)
 
    try:
        if len(data) == data.index(b'$$')+1:
            eval(str(data[:-2]))
        else:
            eval(str(data[:data.index('$$')]))
            eval(str(data[data.index('$$') + 2:len(data)]))
    except():
        print('er')
sock.close()
