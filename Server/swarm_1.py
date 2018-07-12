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
\x00\x00\x01\x01\
\x00\
\x00\x11\x27\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x05\x32\x99\x2e\x70\x30\x01\x29\
\x07\x79\x2f\x46\x20\xc5\x58\x1c\xe4\xee\xc4\xb0\xee\x9c\xcc\x4b\
\x20\x87\x25\xdd\xd1\xd7\x91\x81\x61\x63\x3f\xf7\x9f\x44\x90\x52\
\xce\x02\x8f\xc8\x62\x06\x06\xbe\xc3\x20\xcc\x78\x3c\x7f\x45\x0a\
\x03\x83\xc0\x1e\x4f\x17\xc7\x90\x8a\xb8\xb7\xd7\x37\x0a\x1e\x32\
\x60\x60\x71\x74\xe4\xcf\x73\xef\xf4\x2a\x4f\x2c\x5a\xd4\xc2\xa4\
\xf0\xa0\x6c\xf2\x7c\xfd\x87\x71\xdf\x6b\xf9\x19\x7e\x74\xee\xfd\
\x3e\xe7\xf3\x1c\xff\xec\xb5\xaf\x77\x9d\x63\x64\xf8\xd1\xf4\x3d\
\x12\x68\xe4\x8f\x6c\x26\x09\x06\x86\x06\x16\x46\x1e\xa0\x13\x9a\
\x18\xd8\x18\x18\x14\x1c\x19\x98\x19\x18\x26\x28\x34\x00\x9d\xe3\
\x21\x70\x00\xa8\x46\x85\x23\x01\x48\x0a\xb1\x18\x80\x9c\x30\xaa\
\x7c\x54\xf9\xa8\xf2\x51\xe5\xa3\xca\x47\x95\x8f\x2a\x1f\x55\x3e\
\xaa\x7c\x54\xf9\xa8\xf2\x51\xe5\xa3\xca\x47\x95\x8f\x2a\x1f\x55\
\x4e\xbc\x72\x96\x9e\x8f\x0c\x2f\xa5\x79\x56\x38\x34\x3f\xa9\x06\
\x72\x19\x3c\x5d\xfd\x5c\xd6\x39\x25\x34\x01\x00\xe9\xcb\xf7\x1d\
\
"

qt_resource_name = b"\
\x00\x04\
\x00\x06\x87\x9b\
\x00\x62\
\x00\x61\x00\x63\x00\x6b\
\x00\x08\
\x07\x9e\x5a\x47\
\x00\x62\
\x00\x61\x00\x63\x00\x6b\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0e\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0e\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x64\x8d\x7d\xe9\xe9\
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
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.take_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.take_off_button.setGeometry(QtCore.QRect(760, 60, 100, 40))
        self.take_off_button.setObjectName("take_off_button")
        self.land_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_all_button.setGeometry(QtCore.QRect(890, 60, 91, 40))
        self.land_all_button.setObjectName("land_all_button")
        self.disarm_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_all_button.setGeometry(QtCore.QRect(1010, 60, 101, 40))
        self.disarm_all_button.setStyleSheet("background-color: red")
        self.disarm_all_button.setObjectName("disarm_all_button")
        self.take_off_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.take_off_n_button.setGeometry(QtCore.QRect(760, 160, 100, 30))
        self.take_off_n_button.setObjectName("take_off_n_button")
        self.land_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_n_button.setGeometry(QtCore.QRect(890, 160, 91, 30))
        self.land_n_button.setObjectName("land_n_button")
        self.disarm_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_n_button.setGeometry(QtCore.QRect(1010, 160, 101, 30))
        self.disarm_n_button.setStyleSheet("background-color: red")
        self.disarm_n_button.setObjectName("disarm_n_button")
        self.take_off_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.take_off_spinBox.setGeometry(QtCore.QRect(790, 120, 50, 22))
        self.take_off_spinBox.setObjectName("take_off_spinBox")
        self.land_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.land_spinBox.setGeometry(QtCore.QRect(910, 120, 50, 22))
        self.land_spinBox.setObjectName("land_spinBox")
        self.disarm_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.disarm_spinBox.setGeometry(QtCore.QRect(1040, 120, 50, 22))
        self.disarm_spinBox.setObjectName("disarm_spinBox")
        self.control_console_label = QtWidgets.QLabel(self.centralwidget)
        self.control_console_label.setGeometry(QtCore.QRect(840, 20, 200, 20))
        self.control_console_label.setAlignment(QtCore.Qt.AlignCenter)
        self.control_console_label.setObjectName("control_console_label")
        self.turn_on_led_button = QtWidgets.QPushButton(self.centralwidget)
        self.turn_on_led_button.setGeometry(QtCore.QRect(620, 250, 100, 40))
        self.turn_on_led_button.setStyleSheet("")
        self.turn_on_led_button.setObjectName("turn_on_led_button")
        self.turn_off_led_button = QtWidgets.QPushButton(self.centralwidget)
        self.turn_off_led_button.setGeometry(QtCore.QRect(620, 310, 100, 40))
        self.turn_off_led_button.setObjectName("turn_off_led_button")
        self.stop_swarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_swarm_button.setGeometry(QtCore.QRect(1140, 100, 111, 61))
        self.stop_swarm_button.setStyleSheet("")
        self.stop_swarm_button.setObjectName("stop_swarm_button")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(620, 60, 111, 61))
        self.connect_button.setStyleSheet("")
        self.connect_button.setObjectName("connect_button")
        self.square_button = QtWidgets.QPushButton(self.centralwidget)
        self.square_button.setGeometry(QtCore.QRect(780, 250, 71, 41))
        self.square_button.setStyleSheet("")
        self.square_button.setObjectName("square_button")
        self.circle_button = QtWidgets.QPushButton(self.centralwidget)
        self.circle_button.setGeometry(QtCore.QRect(780, 310, 71, 40))
        self.circle_button.setObjectName("circle_button")
        self.radius_circle_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_circle_spinBox.setGeometry(QtCore.QRect(1040, 320, 50, 22))
        self.radius_circle_spinBox.setObjectName("radius_circle_spinBox")
        self.radius_square_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_square_spinBox.setGeometry(QtCore.QRect(1040, 260, 50, 22))
        self.radius_square_spinBox.setObjectName("radius_square_spinBox")
        self.center_label = QtWidgets.QLabel(self.centralwidget)
        self.center_label.setGeometry(QtCore.QRect(900, 220, 71, 20))
        self.center_label.setAlignment(QtCore.Qt.AlignCenter)
        self.center_label.setObjectName("center_label")
        self.radius_label = QtWidgets.QLabel(self.centralwidget)
        self.radius_label.setGeometry(QtCore.QRect(1040, 220, 55, 16))
        self.radius_label.setAlignment(QtCore.Qt.AlignCenter)
        self.radius_label.setObjectName("radius_label")
        self.figure_label = QtWidgets.QLabel(self.centralwidget)
        self.figure_label.setGeometry(QtCore.QRect(780, 220, 71, 20))
        self.figure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.figure_label.setObjectName("figure_label")
        self.led_label = QtWidgets.QLabel(self.centralwidget)
        self.led_label.setGeometry(QtCore.QRect(640, 220, 61, 20))
        self.led_label.setAlignment(QtCore.Qt.AlignCenter)
        self.led_label.setObjectName("led_label")
        self.center_square_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.center_square_lineEdit.setGeometry(QtCore.QRect(900, 260, 71, 22))
        self.center_square_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.center_square_lineEdit.setObjectName("center_square_lineEdit")
        self.center_circle_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.center_circle_lineEdit.setGeometry(QtCore.QRect(900, 320, 71, 22))
        self.center_circle_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.center_circle_lineEdit.setObjectName("center_circle_lineEdit")
        self.swarm_size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.swarm_size_spinBox.setGeometry(QtCore.QRect(260, 70, 50, 20))
        self.swarm_size_spinBox.setObjectName("swarm_size_spinBox")
        self.swarm_size_label = QtWidgets.QLabel(self.centralwidget)
        self.swarm_size_label.setGeometry(QtCore.QRect(240, 40, 100, 20))
        self.swarm_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.swarm_size_label.setObjectName("swarm_size_label")
        self.send_command_label = QtWidgets.QLabel(self.centralwidget)
        self.send_command_label.setGeometry(QtCore.QRect(840, 370, 200, 20))
        self.send_command_label.setAlignment(QtCore.Qt.AlignCenter)
        self.send_command_label.setObjectName("send_command_label")
        self.console_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.console_textEdit.setGeometry(QtCore.QRect(640, 410, 591, 241))
        self.console_textEdit.setStyleSheet("background-color: rgb(1, 36, 86)")
        self.console_textEdit.setObjectName("console_textEdit")
        self.show_3d_scene_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_3d_scene_button.setGeometry(QtCore.QRect(220, 290, 141, 51))
        self.show_3d_scene_button.setStyleSheet("")
        self.show_3d_scene_button.setObjectName("show_3d_scene_button")
        self.upload_animation_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_animation_button.setGeometry(QtCore.QRect(220, 360, 141, 51))
        self.upload_animation_button.setStyleSheet("")
        self.upload_animation_button.setObjectName("upload_animation_button")
        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(220, 180, 131, 41))
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.statement_swarm_label = QtWidgets.QLabel(self.centralwidget)
        self.statement_swarm_label.setGeometry(QtCore.QRect(230, 150, 111, 20))
        self.statement_swarm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.statement_swarm_label.setObjectName("statement_swarm_label")
        self.start_animation_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_animation_button.setGeometry(QtCore.QRect(220, 430, 141, 51))
        self.start_animation_button.setStyleSheet("")
        self.start_animation_button.setObjectName("start_animation_button")
        self.back_label = QtWidgets.QLabel(self.centralwidget)
        self.back_label.setGeometry(QtCore.QRect(0, -1, 1280, 701))
        self.back_label.setObjectName("back_label")
        self.safty_button = QtWidgets.QPushButton(self.centralwidget)
        self.safty_button.setGeometry(QtCore.QRect(620, 130, 111, 61))
        self.safty_button.setStyleSheet("")
        self.safty_button.setObjectName("safty_button")
        self.tilt_label = QtWidgets.QLabel(self.centralwidget)
        self.tilt_label.setGeometry(QtCore.QRect(1170, 220, 55, 16))
        self.tilt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tilt_label.setObjectName("center_label_2")
        self.tilt_square_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tilt_square_lineEdit.setGeometry(QtCore.QRect(1160, 260, 71, 22))
        self.tilt_square_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tilt_square_lineEdit.setObjectName("tilt_square_lineEdit")
        self.tilt_circle_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tilt_circle_lineEdit.setGeometry(QtCore.QRect(1160, 320, 71, 22))
        self.tilt_circle_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tilt_circle_lineEdit.setObjectName("tilt_circle_lineEdit_2")
        self.back_label.raise_()
        self.take_off_button.raise_()
        self.land_all_button.raise_()
        self.disarm_all_button.raise_()
        self.take_off_n_button.raise_()
        self.land_n_button.raise_()
        self.disarm_n_button.raise_()
        self.take_off_spinBox.raise_()
        self.land_spinBox.raise_()
        self.disarm_spinBox.raise_()
        self.control_console_label.raise_()
        self.turn_on_led_button.raise_()
        self.turn_off_led_button.raise_()
        self.stop_swarm_button.raise_()
        self.connect_button.raise_()
        self.square_button.raise_()
        self.circle_button.raise_()
        self.radius_circle_spinBox.raise_()
        self.radius_square_spinBox.raise_()
        self.center_label.raise_()
        self.radius_label.raise_()
        self.figure_label.raise_()
        self.led_label.raise_()
        self.center_square_lineEdit.raise_()
        self.center_circle_lineEdit.raise_()
        self.swarm_size_spinBox.raise_()
        self.swarm_size_label.raise_()
        self.send_command_label.raise_()
        self.console_textEdit.raise_()
        self.show_3d_scene_button.raise_()
        self.upload_animation_button.raise_()
        self.state_label.raise_()
        self.statement_swarm_label.raise_()
        self.start_animation_button.raise_()
        self.safty_button.raise_()
        self.tilt_label.raise_()
        self.tilt_square_lineEdit.raise_()
        self.tilt_circle_lineEdit.raise_()
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Drone Swarm"))
        self.take_off_button.setText(_translate("MainWindow", "Take off all"))
        self.land_all_button.setText(_translate("MainWindow", "Land all"))
        self.disarm_all_button.setText(_translate("MainWindow", "Disarm all"))
        self.take_off_n_button.setText(_translate("MainWindow", "Take off n"))
        self.land_n_button.setText(_translate("MainWindow", "Land n"))
        self.disarm_n_button.setText(_translate("MainWindow", "Disarm n"))
        self.control_console_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Control console</span></p></body></html>"))
        self.turn_on_led_button.setText(_translate("MainWindow", "Turn on Leds"))
        self.turn_off_led_button.setText(_translate("MainWindow", "Turn off Leds"))
        self.stop_swarm_button.setText(_translate("MainWindow", "Stop swarm"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.square_button.setText(_translate("MainWindow", "Square"))
        self.circle_button.setText(_translate("MainWindow", "Circle"))
        self.center_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Center</span></p><p><br/></p></body></html>"))
        self.radius_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Radius</span></p></body></html>"))
        self.figure_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Figure</span></p></body></html>"))
        self.led_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">LED</span></p></body></html>"))
        self.center_square_lineEdit.setText(_translate("MainWindow", "x,y,z"))
        self.center_circle_lineEdit.setText(_translate("MainWindow", "x,y,z"))
        self.swarm_size_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Swarm Size</span></p></body></html>"))
        self.send_command_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Send command</span></p></body></html>"))
        self.console_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Swarm console</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">&gt;&gt;&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.show_3d_scene_button.setText(_translate("MainWindow", "Show 3d scene"))
        self.upload_animation_button.setText(_translate("MainWindow", "Upload animation"))
        self.state_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Disconnect</span></p></body></html>"))
        self.statement_swarm_label.setText(_translate("MainWindow", "Statement swarm"))
        self.start_animation_button.setText(_translate("MainWindow", "Start animation"))
        self.back_label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/back/back.png\"/></p></body></html>"))
        self.safty_button.setText(_translate("MainWindow", "Safty check"))
        self.tilt_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#c8c8c8;\">Tilt</span></p></body></html>"))
        self.tilt_square_lineEdit.setText(_translate("MainWindow", "x,y"))
        self.tilt_circle_lineEdit.setText(_translate("MainWindow", "x,y"))

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
    try:
        if num == 'all':
            for i in range(copters):  # len(ip) # для автопоиска коптеров
                conn[i].send(com)
        else:
           conn[int(num)-1].send(com)
    except:
        print('is no connect')







class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_animation_button.clicked.connect(self.start_animation)
        # self.pushButton_2.clicked.connect(self.stop_animation)
        self.start_animation_button.clicked.connect(self.start_animation)
        self.disarm_all_button.clicked.connect(self.disarm)
        self.square_button.clicked.connect(self.square)
        self.circle_button.clicked.connect(self.circle)
        self.turn_off_led_button.clicked.connect(self.off_leds)
        self.turn_on_led_button.clicked.connect(self.on_leds)
        self.upload_animation_button.clicked.connect(self.upload_animation)
        self.land_all_button.clicked.connect(self.land)
        self.take_off_button.clicked.connect(self.take_off)

        self.take_off_n_button.clicked.connect(self.take_off_n)
        self.land_n_button.clicked.connect(self.land_n)
        self.disarm_n_button.clicked.connect(self.disarm_n)

        self.safty_button.clicked.connect(self.safty)

        self.connect_button.clicked.connect(self.connect)
        self.swarm_size_spinBox.valueChanged.connect(self.numer_copters)
        #self.lineEdit_5.editingFinished.connect(self.numer_copters)

        # self.horizontalSlider.valueChanged.connect(self.slider)

    def connect(self):
        global copters
        global conn
        conn = []

        for i in range(copters):  # len(ip) # для автопоиска коптеров
            conn.append(0)
            addr.append(0)

        t_0 = Thread(target=self.connect_init)
        t_0.daemon = True
        t_0.start()


    def connect_init(self):
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

        self.disarm_spinBox.setMaximum(copters)
        self.land_spinBox.setMaximum(copters)
        self.take_off_spinBox.setMaximum(copters)

        # begin receiver
        t = Thread(target=receiver)
        t.daemon = True
        t.start()

        print("connected_controllers:", addr)

    def start_animation(self):
        pass

    #def stop_animation(self):
     #   pass

    def safty(self):
        print('sec_ch')
        sender(b'f.safety_check()', 'all')


    def take_off(self):
        print('take_off')
        sender(b'f.takeoff()', 'all')

    def take_off_n(self):
        print('take_off')
        sender(b'f.takeoff()', str(self.take_off_spinBox.value()))



    def land(self):
        print('land')
        sender(b'f.land(preland=False)', 'all')

    def land_n(self):
        print('land')
        sender(b'f.land(preland=False)', str(self.land_spinBox.value()))



    def disarm(self):
        sender(b'f.arming(False)', 'all')

    def disarm_n(self):
        sender(b'f.arming(False)', str(self.disarm_spinBox.value()))

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

    def numer_copters(self):
        print(self.swarm_size_spinBox.value())
        global copters
        copters = self.swarm_size_spinBox.value()

    def circle(self):
        print(self.lineEdit_2.text(), self.lineEdit_4.text())


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
    def upload_animation():
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
