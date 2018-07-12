from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import socket
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
import easygui
import threading
from threading import Thread
import math

qt_resource_data = b"\
\x00\x00\x01\x72\
\x00\
\x00\x11\x77\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x05\x32\x99\x2e\x70\x30\x01\x29\
\x07\x79\x2f\x46\x20\xc5\x58\x1c\xe4\xee\xc4\xb0\xee\x9c\xcc\x4b\
\x20\x87\x25\xdd\xd1\xd7\x91\x81\x61\x63\x3f\xf7\x9f\x44\x90\x52\
\xce\x02\x8f\xc8\x62\x06\x06\xbe\xc3\x20\xcc\x78\x3c\x7f\x45\x0a\
\x03\x83\x20\x8f\xa7\x8b\x63\x48\x45\xdc\xdb\x3b\x1b\x7b\x0f\x05\
\x08\x38\x38\xbe\xe9\x39\xe0\x22\xe2\x90\x58\xe2\xea\x59\xe2\xdc\
\xd4\xd0\xc0\xf2\xf0\x71\x8b\xf6\x0e\x6f\x81\x7c\xb5\x0d\x65\xdb\
\x9b\x9f\x3f\xe0\xff\x6c\xb3\x1e\x68\xd4\x83\xdb\xba\x8c\x35\x56\
\x73\xef\x59\x33\xfc\xb9\x69\xe2\xbb\xfd\x76\xae\xcc\xf1\x54\x76\
\x86\x1f\x3c\xb7\xdf\x7e\xfb\xfa\x97\xf7\x41\xf8\x5f\xae\x04\x86\
\x7f\x99\xdb\x6f\xaf\xbd\xfe\xfa\xfa\x86\xfb\xef\xef\x8b\x33\x34\
\xf0\x17\x5a\xc8\xc4\xf1\xbe\x51\xb7\x05\xb9\x84\x49\x82\x81\xa1\
\x81\x85\x91\x07\xe8\xf0\x26\x06\x36\x06\x06\x05\x47\x06\x66\x06\
\x86\x09\x0a\x0d\x40\x4f\x78\x08\x1c\x00\x2a\x51\xe1\x48\x00\x92\
\x42\x2c\x06\xa3\xca\x47\x95\x8f\x2a\x1f\x55\x3e\xaa\x7c\x54\xf9\
\xa8\xf2\x51\xe5\xa3\xca\x47\x95\x8f\x2a\x1f\x55\x4e\x3d\xe5\x89\
\x3b\x62\xf4\xce\x3f\x2f\x9e\xb5\xec\x29\x03\x43\xfd\xd7\x0a\x9b\
\x77\xdf\x7f\xa7\x6d\x8e\x2c\x63\x68\x38\x5f\xb0\x37\xee\x78\xa1\
\xcc\xb3\xca\x38\x3e\xa0\xc6\x0f\x7b\xdb\x3e\xff\xdc\xd3\x03\x61\
\x3d\xfe\xb8\x03\xc2\xb2\x69\x62\x1d\x9c\xbe\x1a\x55\x3e\xaa\x7c\
\x54\x39\xf1\xca\x59\xd6\x84\xd9\xcf\x4a\x37\x29\x9f\xf0\xf1\xdf\
\x41\x20\x97\xc1\xd3\xd5\xcf\x65\x9d\x53\x42\x13\x00\xd0\xc4\x2c\
\xa0\
\x00\x00\x01\x72\
\x00\
\x00\x11\x77\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x05\x32\x99\x2e\x70\x30\x01\x29\
\x07\x79\x2f\x46\x20\xc5\x58\x1c\xe4\xee\xc4\xb0\xee\x9c\xcc\x4b\
\x20\x87\x25\xdd\xd1\xd7\x91\x81\x61\x63\x3f\xf7\x9f\x44\x90\x52\
\xce\x02\x8f\xc8\x62\x06\x06\xbe\xc3\x20\xcc\x78\x3c\x7f\x45\x0a\
\x03\x83\x20\x8f\xa7\x8b\x63\x48\x45\xdc\xdb\x3b\x1b\x7b\x0f\x05\
\x08\x38\x38\xbe\xe9\x39\xe0\x22\xe2\x90\x58\xe2\xea\x59\xe2\xdc\
\xd4\xd0\xc0\xf2\xf0\x71\x8b\xf6\x0e\x6f\x81\x7c\xb5\x0d\x65\xdb\
\x9b\x9f\x3f\xe0\xff\x6c\xb3\x1e\x68\xd4\x83\xdb\xba\x8c\x35\x56\
\x73\xef\x59\x33\xfc\xb9\x69\xe2\xbb\xfd\x76\xae\xcc\xf1\x54\x76\
\x86\x1f\x3c\xb7\xdf\x7e\xfb\xfa\x97\xf7\x41\xf8\x5f\xae\x04\x86\
\x7f\x99\xdb\x6f\xaf\xbd\xfe\xfa\xfa\x86\xfb\xef\xef\x8b\x33\x34\
\xf0\x17\x5a\xc8\xc4\xf1\xbe\x51\xb7\x05\xb9\x84\x49\x82\x81\xa1\
\x81\x85\x91\x07\xe8\xf0\x26\x06\x36\x06\x06\x05\x47\x06\x66\x06\
\x86\x09\x0a\x0d\x40\x4f\x78\x08\x1c\x00\x2a\x51\xe1\x48\x00\x92\
\x42\x2c\x06\xa3\xca\x47\x95\x8f\x2a\x1f\x55\x3e\xaa\x7c\x54\xf9\
\xa8\xf2\x51\xe5\xa3\xca\x47\x95\x8f\x2a\x1f\x55\x4e\x3d\xe5\x89\
\x3b\x62\xf4\xce\x3f\x2f\x9e\xb5\xec\x29\x03\x43\xfd\xd7\x0a\x9b\
\x77\xdf\x7f\xa7\x6d\x8e\x2c\x63\x68\x38\x5f\xb0\x37\xee\x78\xa1\
\xcc\xb3\xca\x38\x3e\xa0\xc6\x0f\x7b\xdb\x3e\xff\xdc\xd3\x03\x61\
\x3d\xfe\xb8\x03\xc2\xb2\x69\x62\x1d\x9c\xbe\x1a\x55\x3e\xaa\x7c\
\x54\x39\xf1\xca\x59\xd6\x84\xd9\xcf\x4a\x37\x29\x9f\xf0\xf1\xdf\
\x41\x20\x97\xc1\xd3\xd5\xcf\x65\x9d\x53\x42\x13\x00\xd0\xc4\x2c\
\xa0\
"

qt_resource_name = b"\
\x00\x04\
\x00\x07\xac\xa4\
\x00\x74\
\x00\x65\x00\x73\x00\x74\
\x00\x08\
\x07\x9e\x5a\x47\
\x00\x62\
\x00\x61\x00\x63\x00\x6b\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x0a\
\x01\x31\x58\x07\
\x00\x62\
\x00\x61\x00\x63\x00\x6b\x00\x5f\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x24\x00\x01\x00\x00\x00\x01\x00\x00\x01\x76\
\x00\x00\x00\x0e\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x24\x00\x01\x00\x00\x00\x01\x00\x00\x01\x76\
\x00\x00\x01\x64\x70\xb8\xfc\x43\
\x00\x00\x00\x0e\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x64\x70\xb8\xfc\x43\
"

qt_version = QtCore.qVersion().split('.')
if qt_version < ['5', '8', '0']:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 620, 1241, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 580, 301, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 110, 150, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1050, 110, 150, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 110, 150, 50))
        self.pushButton_10.setObjectName("pushButton_10")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 30, 301, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 230, 100, 50))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(600, 290, 100, 50))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1100, 230, 100, 50))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1100, 290, 100, 50))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1100, 350, 100, 50))
        self.pushButton_11.setObjectName("pushButton_11")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 701))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 30, 301, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(710, 239, 100, 31))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 299, 100, 31))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 239, 100, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(820, 299, 100, 31))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")


        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(675, 50, 100, 31))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 110, 150, 50))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 410, 150, 50))
        self.pushButton_12.setObjectName("pushButton_12")

        self.label.raise_()
        self.pushButton.raise_()
        self.horizontalSlider.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swarm"))
        self.pushButton.setText(_translate("MainWindow", "Start animation"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">Choose the moment of animation</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop animation"))
        self.pushButton_3.setText(_translate("MainWindow", "Start swarm"))
        self.pushButton_4.setText(_translate("MainWindow", "Disarm"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#c8c8c8;\">Swarm controller</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Square"))
        self.pushButton_6.setText(_translate("MainWindow", "Circle"))
        self.pushButton_7.setText(_translate("MainWindow", "Turn off leds"))
        self.pushButton_8.setText(_translate("MainWindow", "Turn on leds"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/test/back_1.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#585858;\">Try animation</span></p><p><br/></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "Put center x,y,z"))
        self.lineEdit_2.setText(_translate("MainWindow", "Put center x,y,z"))
        self.lineEdit_3.setText(_translate("MainWindow", "Put radius "))
        self.lineEdit_4.setText(_translate("MainWindow", "Put radius"))
        self.lineEdit_5.setText(_translate("MainWindow", "n drones"))
        self.pushButton_9.setText(_translate("MainWindow", "Get animation"))
        self.pushButton_10.setText(_translate("MainWindow", "Connect"))
        self.pushButton_11.setText(_translate("MainWindow", "Land swarm"))
        self.pushButton_12.setText(_translate("MainWindow", "Take off"))
        self.pushButton_4.setStyleSheet("""background-color: red """)

ip = [1, 2]
# slids = 0
sq_rad = 0
sq_cet = 0
cr_rad = 0
cr_cet = 0
copters = 1
conn = []
file = ''
data = b''
addr = []

# function for scanning wi-fi for searching drones
'''def search_drones():
    global ip
    for i in range(256):

        address = ' 192.168.1.' + str(i + 1)
        response = os.system('ping -n 2 -w 10' + address)

        if response == 0:
            ip.append('192.168.1.' + str(i + 1))
    print(ip)
    return(ip)'''



sock = socket.socket()
sock.bind(('', 35001))  # назначается адресс и порт связи для ноутбука
sock.listen(1)


def receiver():
    global copters
    global data
    # global ip # для автопоиска коптеров
    global conn

    for i in range(copters):  # для автопоиска коптеров len(ip)
        conn[i].setblocking(False)

    while True:
        try:
            for i in range(copters):  # len(ip) # для автопоиска коптеров
                data = conn[i].recv(2048)

        except:
            print('er')
            # conn.close()  # никогда не наступающее закрытие соединения


def sender(com, num):
    global conn
    global copters
    # global ip # для автопоиска коптеров
    if num == 'all':
        for i in range(copters):  # len(ip) # для автопоиска коптеров
            conn[i].send(com)
    else:
        conn[int(num)].send(com)


def connect():
    global copters
    global conn
    for i in range(copters):  # len(ip) # для автопоиска коптеров
        conn.append(0)
        addr.append(0)

    t_0 = Thread(target=connect_init)
    t_0.daemon = True
    t_0.start()


def connect_init():
    global copters


    # print(lineEdit_5.text())
    # ip = search_drones() # для автопоиска коптеров
    # global ip # для автопоиска коптеров
    global conn
    global addr
    print(copters)
    print(conn)
    for i in range(copters):  # len(ip) # для автопоиска коптеров
        conn[i], addr[i] = sock.accept()
        conn[i].send(b'$' + bytes(str(i), 'utf-8') + b'$')
        print("connected_controllers:", addr[i])

    # begin receiver
    t = Thread(target=receiver)
    t.daemon = True
    t.start()

    print("connected_controllers:", addr)



class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.start_animation)
        self.pushButton_2.clicked.connect(self.stop_animation)
        self.pushButton_3.clicked.connect(self.start_swarm)
        self.pushButton_4.clicked.connect(self.stop_swarm)
        self.pushButton_5.clicked.connect(self.square)
        self.pushButton_6.clicked.connect(self.circle)
        self.pushButton_7.clicked.connect(self.off_leds)
        self.pushButton_8.clicked.connect(self.on_leds)
        self.pushButton_9.clicked.connect(self.get_animation)
        self.pushButton_11.clicked.connect(self.land)
        self.pushButton_12.clicked.connect(self.take_off)
        self.pushButton_10.clicked.connect(connect)
        self.lineEdit_5.editingFinished.connect(self.Numer)

        # self.horizontalSlider.valueChanged.connect(self.slider)

    def start_animation(self):
        pass

    def stop_animation(self):
        pass

    def start_swarm(self):
        pass

    def take_off(self):
        print('take_off')
        sender(b'f.takeoff()', 'all')

    def land(self):
        print('land')
        sender(b'f.land(preland=False)', 'all')

    def stop_swarm(self):
        sender(b'f.arming(False)', 'all')

    @staticmethod
    def off_leds():
        sender(b'led.off()', 'all')

    @staticmethod
    def on_leds():
        sender(b'led.fill(255, 255, 0)', 'all')

    def square(self):
        try:
            x = int(self.lineEdit.text().split(',')[0])
            y = int(self.lineEdit.text().split(',')[1])
            z = int(self.lineEdit.text().split(',')[2])
            r = int(self.lineEdit_3.text())

            sender(bytes('f.reach(' + str(x) + ',' + str(y) + ',' + str(z) + ')', 'utf-8'), 0)
            sender(bytes('f.reach(' + str(x + r) + ',' + str(y + r) + ',' + str(z) + ')', 'utf-8'), 1)
            sender(bytes('f.reach(' + str(x + r) + ',' + str(y - r) + ',' + str(z) + ')', 'utf-8'), 2)
            sender(bytes('f.reach(' + str(x - r) + ',' + sttr(y + r) + ',' + str(z) + ')', 'utf-8'), 3)
            sender(bytes('f.reach(' + str(x - r) + ',' + str(y - r) + ',' + str(z) + ')', 'utf-8'), 4)

        except:
            print('input normal x,y,z or radius')

    def Numer(self):
        global copters

        copters=int(self.lineEdit_5.text())


    def circle(self):
        print(self.lineEdit_2.text(), self.lineEdit_4.text())
        # sender()
        # self.horizontalSlider.setMaximum(int(tim))

    ''' def slider(self, value): # function of showing animation
        global slids
        value = slids
        print(value)

        ax.clear()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        i = 0

        i += 0.1
        # set size of scene

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)

        plt.pause(0.0001)

        # clear all settings (delete frame)


        ax.scatter(i, i, i, s=100, c=[0, 0.9, 0], marker='.')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)
        plt.draw()

        plt.show()'''

    @staticmethod
    def get_animation():
        global file
        file = easygui.fileopenbox(filetypes=["*.avi"])  # вызов окна проводника для выбора файла

    @staticmethod
    def showing_motion():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        i = 0

        while i < 10:
            i += 0.1
            # set size of scene

            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.set_zlim(0, 10)

            plt.pause(0.0001)

            # clear all settings (delete frame)

            ax.clear()
            ax.scatter(i, i, i, s=100, c=[0, 0.9, 0], marker='.')

            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.set_zlim(0, 10)
            plt.draw()

        plt.show()


if __name__ == '__main__':
    app = QApplication([])
    w = Widget()
    w.show()

    app.exec()
