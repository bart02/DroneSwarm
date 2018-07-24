# -*- coding: utf-8 -*- .
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import socket
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import easygui
import threading
from threading import Thread
import math
import xmltodict
import requests
import json
import telem_rc

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

        self.number_animation_copters = QtWidgets.QPushButton(self.centralwidget)
        self.number_animation_copters.setGeometry(QtCore.QRect(1140, 150, 111, 40))
        self.number_animation_copters.setStyleSheet("")
        self.number_animation_copters.setObjectName("number_animation_copters")

        self.stop_swarm_but = QtWidgets.QPushButton(self.centralwidget)
        self.stop_swarm_but.setGeometry(QtCore.QRect(1140, 60, 111, 40))
        self.stop_swarm_but.setStyleSheet("")
        self.stop_swarm_but.setObjectName("stop_swarm_but")

        # self.telemetry_but = QtWidgets.QPushButton(self.centralwidget)
        # self.telemetry_but.setGeometry(QtCore.QRect(1140, 105, 111, 40))
        # self.telemetry_but.setStyleSheet("")
        # self.telemetry_but.setObjectName("telemetry_but")

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
        self.radius_circle_DoubleSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_circle_DoubleSpinBox.setGeometry(QtCore.QRect(1040, 320, 50, 22))
        self.radius_circle_DoubleSpinBox.setObjectName("radius_circle_DoubleSpinBox")
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
        self.number_animation_copters.raise_()
        # self.telemetry_but.raise_()
        self.stop_swarm_but.raise_()
        self.connect_button.raise_()
        self.square_button.raise_()
        self.circle_button.raise_()
        self.radius_circle_DoubleSpinBox.raise_()
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
        self.control_console_label.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Control console</span></p></body></html>"))
        self.turn_on_led_button.setText(_translate("MainWindow", "Turn on Leds"))
        self.turn_off_led_button.setText(_translate("MainWindow", "Turn off Leds"))
        self.number_animation_copters.setText(_translate("MainWindow", "Number anim"))
        # self.telemetry_but.setText(_translate("MainWindow", "Telemetry"))
        self.stop_swarm_but.setText(_translate("MainWindow", "Stop swarm"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.square_button.setText(_translate("MainWindow", "Square"))
        self.circle_button.setText(_translate("MainWindow", "Circle"))
        self.center_label.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Center</span></p><p><br/></p></body></html>"))
        self.radius_label.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Radius</span></p></body></html>"))
        self.figure_label.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">Figure</span></p></body></html>"))
        self.led_label.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:9pt; color:#c8c8c8;\">LED</span></p></body></html>"))
        self.center_square_lineEdit.setText(_translate("MainWindow", "x,y,z"))
        self.center_circle_lineEdit.setText(_translate("MainWindow", "x,y,z"))
        self.swarm_size_label.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:9pt;\">Swarm Size</span></p></body></html>"))
        self.send_command_label.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Send command</span></p></body></html>"))
        self.console_textEdit.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE html><html><head><title></title></head><body style=""color:white;>Swarm Console</body></html>"))

        self.show_3d_scene_button.setText(_translate("MainWindow", "Show Telemetry"))
        self.upload_animation_button.setText(_translate("MainWindow", "Upload animation"))
        self.state_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; color:red;\">Disconnect</span></p></body></html>"))
        self.statement_swarm_label.setText(_translate("MainWindow", "Swarm\'s state"))
        self.start_animation_button.setText(_translate("MainWindow", "Start animation"))
        self.back_label.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/back/back.png\"/></p></body></html>"))
        self.safty_button.setText(_translate("MainWindow", "Safty check"))
        self.tilt_label.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#c8c8c8;\">Tilt</span></p></body></html>"))
        self.tilt_square_lineEdit.setText(_translate("MainWindow", "x,y"))
        self.tilt_circle_lineEdit.setText(_translate("MainWindow", "x,y"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 240)
        Dialog.setMinimumSize(QtCore.QSize(550, 240))
        Dialog.setMaximumSize(QtCore.QSize(550, 240))
        self.copter_text = QtWidgets.QLabel(Dialog)
        self.copter_text.setGeometry(QtCore.QRect(80, 20, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.copter_text.setFont(font)
        self.copter_text.setAlignment(QtCore.Qt.AlignCenter)
        self.copter_text.setObjectName("copter_text")
        # self.go_pushButton = QtWidgets.QPushButton(Dialog)
        # self.go_pushButton.setGeometry(QtCore.QRect(340, 10, 93, 41))
        # self.go_pushButton.setObjectName("go_pushButton")
        self.number_spinBox = QtWidgets.QSpinBox(Dialog)
        self.number_spinBox.setGeometry(QtCore.QRect(230, 20, 42, 22))
        self.number_spinBox.setObjectName("number_spinBox")
        self.x_1 = QtWidgets.QLabel(Dialog)
        self.x_1.setGeometry(QtCore.QRect(10, 100, 21, 16))
        self.x_1.setAlignment(QtCore.Qt.AlignCenter)
        self.x_1.setObjectName("x_1")
        self.y_1 = QtWidgets.QLabel(Dialog)
        self.y_1.setGeometry(QtCore.QRect(10, 150, 21, 16))
        self.y_1.setAlignment(QtCore.Qt.AlignCenter)
        self.y_1.setObjectName("y_1")
        self.z_1 = QtWidgets.QLabel(Dialog)
        self.z_1.setGeometry(QtCore.QRect(10, 200, 21, 16))
        self.z_1.setAlignment(QtCore.Qt.AlignCenter)
        self.z_1.setObjectName("z_1")
        self.z_2 = QtWidgets.QLabel(Dialog)
        self.z_2.setGeometry(QtCore.QRect(40, 200, 51, 16))
        self.z_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.z_2.setObjectName("z_2")
        self.x_2 = QtWidgets.QLabel(Dialog)
        self.x_2.setGeometry(QtCore.QRect(40, 100, 51, 16))
        self.x_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.x_2.setObjectName("x_2")
        self.y_2 = QtWidgets.QLabel(Dialog)
        self.y_2.setGeometry(QtCore.QRect(40, 150, 51, 16))
        self.y_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.y_2.setObjectName("y_2")
        self.mode_2 = QtWidgets.QLabel(Dialog)
        self.mode_2.setGeometry(QtCore.QRect(470, 130, 71, 16))
        self.mode_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mode_2.setObjectName("mode_2")
        self.armed_2 = QtWidgets.QLabel(Dialog)
        self.armed_2.setGeometry(QtCore.QRect(470, 100, 71, 16))
        self.armed_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.armed_2.setObjectName("armed_2")
        self.frame_id_1 = QtWidgets.QLabel(Dialog)
        self.frame_id_1.setGeometry(QtCore.QRect(400, 170, 61, 16))
        self.frame_id_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_id_1.setObjectName("frame_id_1")
        self.armed_1 = QtWidgets.QLabel(Dialog)
        self.armed_1.setGeometry(QtCore.QRect(400, 100, 51, 16))
        self.armed_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.armed_1.setObjectName("armed_1")
        self.frame_id_2 = QtWidgets.QLabel(Dialog)
        self.frame_id_2.setGeometry(QtCore.QRect(470, 170, 71, 16))
        self.frame_id_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_id_2.setObjectName("frame_id_2")
        self.mode_1 = QtWidgets.QLabel(Dialog)
        self.mode_1.setGeometry(QtCore.QRect(400, 130, 51, 16))
        self.mode_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mode_1.setObjectName("mode_1")
        self.voltage_2 = QtWidgets.QLabel(Dialog)
        self.voltage_2.setGeometry(QtCore.QRect(470, 200, 71, 16))
        self.voltage_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.voltage_2.setObjectName("voltage_2")
        self.voltage_1 = QtWidgets.QLabel(Dialog)
        self.voltage_1.setGeometry(QtCore.QRect(400, 200, 51, 16))
        self.voltage_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.voltage_1.setObjectName("voltage_1")
        self.roll_2 = QtWidgets.QLabel(Dialog)
        self.roll_2.setGeometry(QtCore.QRect(190, 200, 61, 16))
        self.roll_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.roll_2.setObjectName("roll_2")
        self.yaw_1 = QtWidgets.QLabel(Dialog)
        self.yaw_1.setGeometry(QtCore.QRect(140, 100, 31, 16))
        self.yaw_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.yaw_1.setObjectName("yaw_1")
        self.pitch_1 = QtWidgets.QLabel(Dialog)
        self.pitch_1.setGeometry(QtCore.QRect(140, 150, 41, 16))
        self.pitch_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pitch_1.setObjectName("pitch_1")
        self.roll_1 = QtWidgets.QLabel(Dialog)
        self.roll_1.setGeometry(QtCore.QRect(140, 200, 31, 16))
        self.roll_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.roll_1.setObjectName("roll_1")
        self.pitch_2 = QtWidgets.QLabel(Dialog)
        self.pitch_2.setGeometry(QtCore.QRect(190, 150, 61, 16))
        self.pitch_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pitch_2.setObjectName("pitch_2")
        self.yaw2 = QtWidgets.QLabel(Dialog)
        self.yaw2.setGeometry(QtCore.QRect(190, 100, 61, 16))
        self.yaw2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.yaw2.setObjectName("yaw2")
        self.vy_1 = QtWidgets.QLabel(Dialog)
        self.vy_1.setGeometry(QtCore.QRect(270, 150, 31, 16))
        self.vy_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vy_1.setObjectName("vy_1")
        self.vx_2 = QtWidgets.QLabel(Dialog)
        self.vx_2.setGeometry(QtCore.QRect(320, 100, 61, 16))
        self.vx_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vx_2.setObjectName("vx_2")
        self.vz_1 = QtWidgets.QLabel(Dialog)
        self.vz_1.setGeometry(QtCore.QRect(270, 200, 31, 16))
        self.vz_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vz_1.setObjectName("vz_1")
        self.vy_2 = QtWidgets.QLabel(Dialog)
        self.vy_2.setGeometry(QtCore.QRect(320, 150, 61, 16))
        self.vy_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vy_2.setObjectName("vy_2")
        self.vz_2 = QtWidgets.QLabel(Dialog)
        self.vz_2.setGeometry(QtCore.QRect(320, 200, 61, 16))
        self.vz_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vz_2.setObjectName("vz_2")
        self.vx_1 = QtWidgets.QLabel(Dialog)
        self.vx_1.setGeometry(QtCore.QRect(270, 100, 31, 16))
        self.vx_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.vx_1.setObjectName("vx_1")
        self.back = QtWidgets.QLabel(Dialog)
        self.back.setGeometry(QtCore.QRect(0, 0, 551, 241))
        self.back.setObjectName("back")
        self.back.raise_()
        self.copter_text.raise_()
        # self.go_pushButton.raise_()
        self.number_spinBox.raise_()
        self.x_1.raise_()
        self.y_1.raise_()
        self.z_1.raise_()
        self.z_2.raise_()
        self.x_2.raise_()
        self.y_2.raise_()
        self.mode_2.raise_()
        self.armed_2.raise_()
        self.frame_id_1.raise_()
        self.armed_1.raise_()
        self.frame_id_2.raise_()
        self.mode_1.raise_()
        self.voltage_2.raise_()
        self.voltage_1.raise_()
        self.roll_2.raise_()
        self.yaw_1.raise_()
        self.pitch_1.raise_()
        self.roll_1.raise_()
        self.pitch_2.raise_()
        self.yaw2.raise_()
        self.vy_1.raise_()
        self.vx_2.raise_()
        self.vz_1.raise_()
        self.vy_2.raise_()
        self.vz_2.raise_()
        self.vx_1.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Telemetry"))
        self.copter_text.setText(_translate("Dialog", "Copter"))
        self.x_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">x=</span></p></body></html>"))
        self.y_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">y=</span></p></body></html>"))
        self.z_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">z=</span></p></body></html>"))
        self.z_2.setText(_translate("Dialog",
                                    "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.x_2.setText(_translate("Dialog",
                                    "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.y_2.setText(_translate("Dialog",
                                    "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.mode_2.setText(_translate("Dialog",
                                       "<html><head/><body><p><span style=\" color:#c8c8c8;\">MANUALE</span></p></body></html>"))
        self.armed_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#c8c8c8;\">False</span></p></body></html>"))
        self.frame_id_1.setText(_translate("Dialog",
                                           "<html><head/><body><p><span style=\" color:#c8c8c8;\">farme id=</span><br/></p></body></html>"))
        self.armed_1.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#c8c8c8;\">armed=</span></p></body></html>"))
        self.frame_id_2.setText(_translate("Dialog",
                                           "<html><head/><body><p><span style=\" color:#c8c8c8;\">aruco_map</span></p></body></html>"))
        self.mode_1.setText(_translate("Dialog",
                                       "<html><head/><body><p><span style=\" color:#c8c8c8;\">mode=</span></p></body></html>"))
        self.voltage_2.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.voltage_1.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" color:#c8c8c8;\">voltage=</span></p></body></html>"))
        self.roll_2.setText(_translate("Dialog",
                                       "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.yaw_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">yaw=</span></p></body></html>"))
        self.pitch_1.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#c8c8c8;\">pitch=</span></p></body></html>"))
        self.roll_1.setText(_translate("Dialog",
                                       "<html><head/><body><p><span style=\" color:#c8c8c8;\">roll=</span></p></body></html>"))
        self.pitch_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.yaw2.setText(_translate("Dialog",
                                     "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.vy_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">vy=</span></p></body></html>"))
        self.vx_2.setText(_translate("Dialog",
                                     "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.vz_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">vz=</span></p></body></html>"))
        self.vy_2.setText(_translate("Dialog",
                                     "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.vz_2.setText(_translate("Dialog",
                                     "<html><head/><body><p><span style=\" color:#c8c8c8;\">0.000</span></p></body></html>"))
        self.vx_1.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" color:#c8c8c8;\">vx=</span></p></body></html>"))
        self.back.setText(
            _translate("Dialog", "<html><head/><body><p><img src=\":/telem/Без имени.png\"/></p></body></html>"))

ip = [1, 2]
# slids = 0
sq_rad = 0
sq_cet = 0
cr_rad = 0
cr_cet = 0
copters = 1
conn = []
conn_2 = []
file = ''
data = b''
addr = []
addr_2 = []
coord = []
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

sock.bind(('', 35001))  # назначается адресс и порт связи для отпраки команд на коптеры
sock.listen(1)

sock_2 = socket.socket()
sock_2.bind(('', 35002))  # назначается адресс и порт связи для приема данных с коптеров
sock_2.listen(1)

class Dialog(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def up(self):
        self.voltage_2.setText('1234567')

class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_animation_button.clicked.connect(self.start_animation)
        self.stop_swarm_but.clicked.connect(self.stop_swarm)
        self.show_3d_scene_button.clicked.connect(self.show_3d)
        self.disarm_all_button.clicked.connect(self.disarm)
        self.square_button.clicked.connect(self.square)
        self.circle_button.clicked.connect(self.circle)
        self.turn_off_led_button.clicked.connect(self.off_leds)
        self.turn_on_led_button.clicked.connect(self.on_leds)
        self.upload_animation_button.clicked.connect(self.upload_animation)
        self.land_all_button.clicked.connect(self.land)
        self.take_off_button.clicked.connect(self.take_off)
        self.number_animation_copters.clicked.connect(self.number_animation)
        self.take_off_n_button.clicked.connect(self.take_off_n)
        self.land_n_button.clicked.connect(self.land_n)
        self.disarm_n_button.clicked.connect(self.disarm_n)
        self.land_spinBox.valueChanged.connect(self.land_led)
        self.disarm_spinBox.valueChanged.connect(self.disarm_led)
        self.take_off_spinBox.valueChanged.connect(self.take_off_led)
        self.safty_button.clicked.connect(self.safty)
        self.connect_button.clicked.connect(self.connect)
        self.swarm_size_spinBox.valueChanged.connect(self.number_copters)

    def stop_swarm(self):
        global coord
        n = 0
        for s in coord:
            n += 1
            self.sender(b'reach(' + bytes(str(s[0] + ',' + s[1] + ',' + s[2]), 'utf-8') + ')', n)
            print(b'reach(' + bytes(str(s[0] + ',' + s[1] + ',' + s[2]), 'utf-8') + ')', n)

    def receiver(self):
        global copters
        # global data
        global addr
        while True:
            try:
                for k in range(copters):  # len(ip) # для автопоиска коптеров
                    a = requests.get('http://' + addr[k][0] + ':8081/aruco_map')
                    tem = json.loads(a.text)

                    coord[k] = str(tem['x']) + ',' + str(tem['y']) + ',' + str(tem['z']) + ',' + \
                               str(tem['mode']) + ',' + str(tem['armed']) + ',' + str(tem['frame_id']) + str(
                        tem['voltage']) + ',' + \
                               str(tem['yaw']) + ',' + str(tem['pitch']) + ',' + str(tem['roll']) + ',' + \
                               str(tem['vx']) + ',' + str(tem['vy']) + ',' + str(tem['vz'])

                    time.sleep(0.05)



            except Exception as e:

                # print(e)
                    pass
    def sender(self, com, num):
        global conn
        global conn_2
        global copters
        # global ip # для автопоиска коптеров
        print(com)
        print(num)
        try:
            if num == 'all':
                for i in range(copters):  # len(ip) # для автопоиска коптеров
                    conn[i].send(com + b'$$')
            elif int(num) > 0:
                conn[int(num) - 1].send(com + b'$$')
        except:
            pass

    def message(self, mes):
        pass


    def connect(self):
        global copters
        global conn
        global conn_2
        global addr
        global addr_2
        global coord

        addr_2 = []

        conn = []
        conn_2 = []

        self.message('Try connect')
        for i in range(copters):  # len(ip) # для автопоиска коптеров
            conn.append(0)
            addr.append(0)
            coord.append('0')

        t_0 = Thread(target=self.connect_init)
        t_0.daemon = True
        t_0.start()

    def connect_init(self):
        self.state_label.setText("<html><head/><body><p><span style=\" font-size:12pt; color:rgb(255,255,"
                                 "0);\">Wait</span></p></body></html>")
        global copters

        # ip = search_drones() # для автопоиска коптеров
        # global ip # для автопоиска коптеров
        global conn
        global addr
        global conn_2
        global addr_2

        for i in range(copters):  # len(ip) # для автопоиска коптеров
            conn[i], addr[i] = sock.accept()
            print("connected_controllers:", addr[i])

        self.disarm_spinBox.setMaximum(copters)
        self.land_spinBox.setMaximum(copters)
        self.take_off_spinBox.setMaximum(copters)
        self.state_label.setText("<html><head/><body><p><span style=\" font-size:12pt; "
                                 "color:Green;\">Connect</span></p></body></html>")

        t = Thread(target=self.receiver)
        t.daemon = True
        t.start()

    def number_animation(self):
        global copters
        col = [b'(255,0,0)', b'(173,255,47)', b'(255,215,0)', b'(255,0,255)', b'(0,0,255)', b'(205,92,92)',
               b'(255,255,255)', b'(240,128,128)']
        for i in range(copters + 1):
            self.sender(b'led.fill' + col[i], str(i))
            time.sleep(0.5)
            self.sender(b'led.off()', str(i))
        for i in range(copters + 1):
            self.sender(b'led.fill' + col[i], str(i))

            time.sleep(0.5)

    def safty(self):
        self.message('safty check')
        self.sender(b'f.safety_check(False)', 'all')

    def take_off(self):
        self.message('take off')
        self.sender(b'f.takeoff(z=2, speed=2,speed_takeoff=2 , timeout=2)', 'all')

    def take_off_n(self):
        self.message('take off n')
        self.sender(b'f.takeoff()', str(self.take_off_spinBox.value()))

    def land(self):
        self.message('land')
        self.sender(b'f.land(preland=False)', 'all')

    def land_n(self):
        self.message('land n')
        self.sender(b'f.land(preland=False)', str(self.land_spinBox.value()))

    def disarm(self):
        self.sender(b'f.arming(False)', 'all')

    def disarm_n(self):
        self.sender(b'f.arming(False)', str(self.disarm_spinBox.value()))

    def off_leds(self):
        self.sender(b'led.off()', 'all')

    def land_led(self):
        self.sender(b'led.off()', 'all')
        self.sender(b'led.fill(255,0,0)', self.land_spinBox.value())
        # print(1)

    def disarm_led(self):
        self.sender(b'led.off()', 'all')
        self.sender(b'led.fill(0,255,0)', self.disarm_spinBox.value())

    def take_off_led(self):
        self.sender(b'led.off()', 'all')
        self.sender(b'led.fill(0,0,255)', self.take_off_spinBox.value())

    def on_leds(self):
        self.sender(b'led.fill(0, 0, 255)', 'all')

    def square(self):
        try:
            x = int(self.lineEdit.text().split(',')[0])
            y = int(self.lineEdit.text().split(',')[1])
            z = int(self.lineEdit.text().split(',')[2])
            r = int(self.lineEdit_3.text())

            self.sender(bytes('f.reach(' + str(x) + ',' + str(y) + ',' + str(z) + ')', 'utf-8'), 0)
            self.sender(bytes('f.reach(' + str(x + r) + ',' + str(y + r) + ',' + str(z) + ')', 'utf-8'), 1)
            self.sender(bytes('f.reach(' + str(x + r) + ',' + str(y - r) + ',' + str(z) + ')', 'utf-8'), 2)
            self.sender(bytes('f.reach(' + str(x - r) + ',' + sttr(y + r) + ',' + str(z) + ')', 'utf-8'), 3)
            self.sender(bytes('f.reach(' + str(x - r) + ',' + str(y - r) + ',' + str(z) + ')', 'utf-8'), 4)

        except:

            self.message('input normal x,y,z or radius')

    def number_copters(self):
        global copters
        copters = self.swarm_size_spinBox.value()

    def circle(self):
        self.message('circle')

        self.sender(b'f.circle(' + bytes(self.center_circle_lineEdit.text(), 'utf-8') + b',' + bytes(
            str(int(self.radius_circle_DoubleSpinBox.text()) / 10), 'utf-8') + b')',
                    'all')  # ToDO made function for all copters not for 1

    def upload_animation(self):
        global file
        file = easygui.fileopenbox(filetypes=["*.avi"])  # вызов окна проводника для выбора файла

    def start_animation(self):
        t_4 = Thread(target=self.start_animation_1)
        t_4.daemon = True
        t_4.start()

    def start_animation_1(self):
        os.system(r"start C:\Users\allex\Documents\DroneSwarm\music\file.mp3")
        # xml parcer
        time.sleep(4.5)

        types = {

            'x': float,

            'y': float,

            'z': float,

            'yaw': float,

            'yaw_rate': float,

            'speed': float,

            'tolerance': float,

            'frame_id': str,

            'mode': str,

            'wait_ms': int,

            'timeout': int,

            'z_coefficient': float,

            'timeout_arm': int,

            'timeout_land': int,

            'preland': bool,

            'r': int,

            'g': int,

            'b': int,

        }

        def parse_xml(xml_file=None, xml_str=None):

            if (xml_file is None and xml_str is None) or (xml_file is not None and xml_str is not None):
                raise ValueError('You must use one parameter')

            if xml_str is None:

                with open(xml_file, 'r') as f:

                    xml = f.read().strip()

            else:

                xml = xml_str

            xmldict = xmltodict.parse(xml)

            xmldict = dict(xmldict['DroneSwarm'])['time']

            ready = {}

            if type(xmldict) != list:
                xmldict = [xmldict]

            for t in xmldict:

                time = float(t['@t'])

                ready[time] = {}

                try:

                    if type(t['copter']) != list:
                        t['copter'] = [t['copter']]

                    for copter in t['copter']:

                        copternum = int(copter['@n'])

                        ready[time][copternum] = []

                        copter.pop('@n')

                        for action in copter:

                            actiondict = {}

                            try:

                                for prm in dict(copter[action]):

                                    val = dict(copter[action])[prm]

                                    prm = str(prm.replace('@', ''))

                                    try:

                                        actiondict[prm] = types[prm](val)

                                    except KeyError:

                                        print("Types hasn't got " + prm + ', use str.')

                                        actiondict[prm] = str(val)

                                # print {action: actiondict}

                                ready[time][copternum].append({str(action): actiondict})

                            except ValueError:

                                raise ValueError('You can use only "n" parameter in "copter" tag')

                except KeyError:

                    pass

                try:

                    swarm = t['swarm']

                    copternum = 0

                    ready[time][copternum] = []

                    for action in swarm:

                        actiondict = {}

                        try:

                            if swarm[action] is not None:

                                for prm in dict(swarm[action]):

                                    val = dict(swarm[action])[prm]

                                    prm = str(prm.replace('@', ''))

                                    try:

                                        actiondict[prm] = types[prm](val)

                                    except KeyError:

                                        print("Types hasn't got " + prm + ', use str.')

                                        actiondict[prm] = str(val)

                            ready[time][copternum].append({str(action): actiondict})

                        except TypeError:

                            raise ValueError('You can use only one "swarm" tag')

                except KeyError:

                    pass

            return ready

        data = ''
        global file
        xm = parse_xml(file)
        print(xm)
        n = 0
        for i in xm:

            for k in xm[i]:
                # k =  copter number
                s = str(xm.keys())[str(xm.keys()).index('[') + 1:-2]
                p = s.split(', ')
                try:
                    timeout = str(((float(p[n + 1]) - float(p[n])) * 1000)-2000)
                except:
                    print('end')

                for l in xm[i][k]:

                    o = str(l.keys())
                    f = o[o.index('[\'') + 2: -3]  # f =  function

                    # l[f] = parameters
                    if k == 0:
                        k = 'all'

                    if f == 'circle':
                        x = str(l[f]['x'])
                        y = str(l[f]['y'])
                        z = str(l[f]['z'])
                        r = str(l[f]['r'])

                        data = 'f.circle' + '(' + x + ',' + y + ',' + z + ',' + r + ',' + 'timeout =' + timeout + ')'

                        print(data, k)
                        print('_______________________')
                        self.sender(bytes(data, 'utf-8'), str(k))
                    if f == 'music':
                        file = str(l[f]['file'])

                        os.system(r"start" + file)
                        time.sleep(3)


                    elif f == 'led':

                        mode = str(l[f]['mode'])
                        if mode == 'rainbow':
                            data = 'led.rainbow()'
                        elif mode == 'off':
                            data = 'led.off()'


                        else:
                            print(n)
                            r = str(l[f]['r'])
                            g = str(l[f]['g'])
                            b = str(l[f]['b'])

                            data = 'led.' + mode + '(' + g + ',' + r + ',' + b + ')'

                        self.sender(bytes(data, 'utf-8'), str(k))
                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'reach':
                        x = str(l[f]['x'])
                        y = str(l[f]['y'])
                        z = str(l[f]['z'])
                        try:
                            speed = 'speed=' + str(l[f]['speed'])
                            data = 'f.reach' + '(' + x + ',' + y + ',' + z + ',' + speed + ',' + 'timeout=' + timeout + ')'
                        except:
                            speed = 'speed=0.6'
                            data = 'f.reach' + '(' + x + ',' + y + ',' + z + ',' + speed + ',' + 'timeout=' + timeout + ')'

                        self.sender(bytes(data, 'utf-8'), str(k))
                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'takeoff':
                        z = str(l[f]['z'])
                        try:
                            speed = str(l[f]['speed'])
                            data = 'f.takeoff(' + z + ',' + 'timeout_arm=1000' + ',' +'speed='+str(speed)+','+ 'timeout_fcu=' + str(
                                (float(timeout) - 1000) // 2) + ',' + 'timeout=' + str((float(timeout) - 1000) // 2) + ')'

                            self.sender(bytes(data, 'utf-8'), str(k))
                            print(bytes(data, 'utf-8'), str(k))
                        except:
                            data = 'f.takeoff(' + z + ',' + 'timeout_arm=1000' + ',' + 'timeout_fcu=' + str(
                                (float(timeout) - 1000) // 2) + ',' + 'timeout=' + str(
                                (float(timeout) - 1000) // 2) + ')'

                            self.sender(bytes(data, 'utf-8'), str(k))
                            print(bytes(data, 'utf-8'), str(k))

                        print('_______________________')
                    elif f == 'land':
                        data = 'f.land(timeout=' + timeout + ')'

                        self.sender(bytes(data, 'utf-8'), str(k))
                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'attitude':
                        z = str(l[f]['z'])
                        data = 'f.attitude(' + z + ',' + 'timeout =' + timeout + ')'

                        self.sender(bytes(data, 'utf-8'), str(k))
                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')

            s = str(xm.keys())[str(xm.keys()).index('[') + 1:-2]
            p = s.split(', ')
            print(p)

            try:
                time.sleep((float(timeout)+1500)//1000)

            except:
                print('end of list')
            n += 1

    def show_3d(self):

        global data
        global copters
        global coord
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        updateDialog = Dialog()
        updateDialog.show()

        while True:
            s = str(self.console_textEdit.toPlainText())
            if '>' in s:

                print(s[:-2], s[s.index('>') - 1])
                self.console_textEdit.setText('')
                if s[s.index('>') - 1] == '0':
                    self.sender(bytes(str(s[:s.index('>') - 1]),'utf-8'), 'all')
                    print(s[:s.index('>') - 1], 'all')
                else:
                    self.sender(bytes(str(s[:s.index('>') - 1]),'utf-8'), str(s[s.index('>') - 1]))
                    print('sender', s[s.index('>') - 1] )
            try:

                i = updateDialog.number_spinBox.value()
                if i > 0:
                    i -= 1

                coord_drone = []
                coord_drone = coord[i].split(',')

                updateDialog.z_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    0] + "</span></p></body></html>")
                updateDialog.x_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    1] + "</span></p></body></html>")
                updateDialog.y_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    2] + "</span></p></body></html>")
                updateDialog.mode_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    3] + "</span></p></body></html>")
                updateDialog.armed_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    4] + "</span></p></body></html>")
                updateDialog.frame_id_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    5] + "</span></p></body></html>")
                updateDialog.voltage_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    6] + "</span></p></body></html>")
                updateDialog.yaw2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    7] + "</span></p></body></html>")
                updateDialog.pitch_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    8] + "</span></p></body></html>")
                updateDialog.roll_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    9] + "</span></p></body></html>")
                updateDialog.vx_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    10] + "</span></p></body></html>")
                updateDialog.vy_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    11] + "</span></p></body></html>")
                updateDialog.vz_2.setText("<html><head/><body><p><span style=\" color:#c8c8c8;\">" + coord_drone[
                    12] + "</span></p></body></html>")
            except Exception as e:
                # print(e)
                pass
            try:

                n = 0
                # set size of scene

                ax.set_xlim(0, 1.5)
                ax.set_ylim(0, 2.2)
                ax.set_zlim(0, 2)

                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')

                plt.pause(0.01)

                ax.clear()
                try:
                    for i in coord:
                        co = (0, 0, 0)
                        n += 1

                        if self.land_spinBox.value() == n:
                            co = (1, 0, 0)
                        if self.take_off_spinBox.value() == n:
                            co = (1, 0, 0)
                        if self.disarm_spinBox.value() == n:
                            co = (1, 0, 0)

                        ax.scatter(float(i.split(',')[0]), float(i.split(',')[1]), float(i.split(',')[2]), s=50, c=co,
                                   marker='.')
                        ax.text(float(i.split(',')[0]), float(i.split(',')[1]), float(i.split(',')[2]), str(n), size=10, zorder=1, color=(0,0,0))

                except Exception as e:
                     #print(e)
                    pass

                ax.set_xlim(0, 1.5)
                ax.set_ylim(0, 2.2)
                ax.set_zlim(0, 2)

                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')

                plt.draw()
            except KeyboardInterrupt:
                print('stop')
                break

        plt.show()

if __name__ == '__main__':
    app = QApplication([])
    w = Widget()
    w.show()

    app.exec()

"""Code by Alexandr Osherov 9B class phone- +79251834732 email - allexandr2001@mail.ru"""
