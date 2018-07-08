import socket
import os
import time
sock = socket.socket()
sock.connect(('10.23.45.159', 35001))
# 10.23.45.159
    
data=r''
while True:#бесконечный цикл отправки данных
    
    sock.setblocking(False)
    
    try:
        
        data=sock.recv(2048)
        data=r''
    except:
        pass

    try:
        sock.send(b'test_client')#отправка данных
    except:
        #time.sleep(0.1)
        pass
conn.close()#никогда не наступающее закрытие соединения
    
