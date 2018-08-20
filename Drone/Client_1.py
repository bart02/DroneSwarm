from FlightLib import FlightLib as f
import threading
from threading import Thread
f.init('server')
# from FlightLib import TelemLib
from FlightLib import LedLib as led
from time import sleep
import socket
import sys
import time

sq = []

while True:
    try:
        sock = socket.socket()
        sock.connect(('192.168.43.117', 35001))
    except socket.error:
        print("No connection. Sleep 10 secs.")
        sleep(10)
    else:
        break

def animation():
        
        data = ''

        op = open('swarm.swarm', 'r')
        read = op.read()
        xm = read.split('*')

        for i in range(1, len(xm)):
            #print('i=', i)
            #print('xm[i]=', xm[i])
            for k in range(1, len(xm[i].split('/'))-1):
                #print('k=', xm[i].split('/')[k])
                timeout='1000'

                for func in xm[i].split('/')[k].split(' '):
                    #print('f=', f)


                    if func[0] == 'c':

                        data = 'led.off()'

                        r = str(func[1:].split(',')[0])
                        g = str(func[1:].split(',')[1])
                        b = str(func[1:].split(',')[2])
                        if float(r)+float(g)+float(b)==0:
                            data = 'led.off()'
                        else:
                            data = 'led.fill' + '(' + g + ',' + r + ',' + b + ')'

                        print(bytes(data), str(xm[i].split('/')[k][1]))
                        # led.fill( float(g), float(r), float(b))
                        print('_______________________')
                    elif func[0] == 'p':
                        x = str(func[1:].split(',')[0])
                        y = str(func[1:].split(',')[1])
                        z = str(func[1:].split(',')[2])

                        speed = 'speed=0.6'
                        data = 'f.reach' + '(' + x + ',' + y + ',' + z + ',' + speed + ',' + 'timeout=' + timeout + ')'
                        # f.reach(float(x) ,float(y) ,float(z) ,speed=0.5 ,timeout=int(timeout))
                        print(bytes(data), str(xm[i].split('/')[k][1]))
                        print('_______________________')
                    elif func[:2] == 'tf':
                        z = func[:2].split(',')[0]


                        data = 'f.takeoff(' + z + ',' + 'timeout_arm=1500' + ',' + 'timeout_fcu=' + str(
                            (float(timeout))) + ',' + 'timeout=' + str(
                            (float(timeout)) * 10) + ')'
                        # f.takeoff(float(z) , timeout_arm=1500,timeout_fcu=(float(timeout)) , timeout=(float(timeout)) * 10)

                        print(bytes(data), str(xm[i].split('/')[k][1]))

                        print('_______________________')
                    elif func[:2] == 'ld':
                        data = 'f.land(timeout=' + str(float(timeout)*7) + ')'
                        # f.land(timeout=float(timeout)*7)

                        print(bytes(data), str(xm[i].split('/')[k][1]))
                        print('_______________________')
                        # elif f == 'attitude':
                        #     z = str(l[f]['z'])
                        #     data = 'f.attitude(' + z + ',' + 'timeout =' + timeout + ')'
                        #
                        #     self.sender(bytes(data, 'utf-8'), str(k[0]))
                        #     print(bytes(data, 'utf-8'), str(k[0]))
                        #     print('_______________________')
                    elif func == 's':
                        x = str(l[f]['x'])
                        y = str(l[f]['y'])

                        print(bytes(x + ' ' + y, 'utf-8'), str(xm[i].split('/')[k][1]))
                        print('_______________________')
            time.sleep(1)

        op.close()
                        
            
            

try:
    while True:
        data = str(sock.recv(1024))
        print(data)
        try:
            if b'programm' in data:
                print(1)
                xm = open('swarm.swarm', 'w')
                print(2)
                data = data[data.index(b'programm') + 10:]
                print(3)
                xm.write(data)
                print(4)

                while True:
                    print('5___________')
                    
                    data = str(sock.recv(1024))
                    print(data)
                    if b'$$' in data:
                        xm.write(data[:data.index(b'$$')])
                        print('stop_byte')
                        xm.close()
                        xm = open('swarm.swarm', 'r')
                        
                        print(xm.read())
                        xm.close()
                        
                        
                        
                        t_0 = Thread(target=animation)
                        t_0.daemon = True
                        t_0.start()
                        
                        time.sleep(2)
                        break
                    else:
                        xm.write(data)

            else:
                try:
                    sq = data.split('$$')
                    for i in range(len(sq) - 1):
                        print(sq[i])
                        eval(sq[i])

                except Exception as e:
                    print(e)

        except Exception as er:
            print(er)
    sock.close()
except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()
