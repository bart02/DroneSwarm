import socket
import os
import time

sock = socket.socket()
sock.bind(('', 35001))  # назначается адресс и порт связи для ноутбука
sock.listen(1)
conn = []
adr = []

for i in range(5):
    conn.append(i)
    adr.apend(i)

command = [b'fill', b'run', b'blink', b'off']
for i in range(5):
    conn[i], addr[i] = sock.accept()

print("connected_controllers:", adr)
data = r''
for i in range(5):
    try:
        for com in command:

            for num in range(5):
                conn[num].send(com)  # отправка данных

            time.sleep(5)
    except:
        pass

conn.close()  # никогда не наступающее закрытие соединения

