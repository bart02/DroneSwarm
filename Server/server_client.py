import socket
import os
import time
sock = socket.socket()
sock.bind(('',35001))#назначается адресс и порт связи для ноутбука
sock.listen(1)
conn, addr = sock.accept()

    
print("connected_controllers:",addr)
data=r''
while True:#бесконечный цикл отправки данных
    
    conn.setblocking(False)
    
    try:
        
        data=conn.recv(2048)
        print(data)
        data=r''
    except:
        pass

    try:
        conn.send(b'test_server')#отправка данных
    except:
         pass
        
conn.close()#никогда не наступающее закрытие соединения
    
