from FlightLib import LedLib as led
import socket
sock=socket.socket()
sock.connect(('192.168.1.5', 35001))


while True:
    data = sock.recv(1024)
    if data == b'fill':
        led.fill(255, 255, 255)
    if data == b'run':
        led.fill(255, 255, 255)
    if data == b'blink':
        led.blink(255, 255, 255)
    if data == b'off':
        led.off()
sock.close()

