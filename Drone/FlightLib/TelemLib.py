from __future__ import print_function
from threading import Thread
import time
import rospy
from clever import srv
import socket


def init(node_name="TelemLib"):
    print("Initing telemetry node")
    rospy.init_node(node_name)
    print("Node inited")


get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

wait_ms = 100


def telemetry_thread():
    data = b''
    sock = socket.socket()
    sock.connect(('192.168.1.6', 35002))
    while True:
        telemetry = get_telemetry(frame_id='aruco_map')
        x = bytes(str(round(telemetry.x, 3)), 'utf-8')
        y = bytes(str(round(telemetry.y, 3)), 'utf-8')
        z = bytes(str(round(telemetry.z, 3)), 'utf-8')
        data = x + b',' + y + b',' + z
        sock.send(data)

        time.sleep(wait_ms / 1000)


t_t = Thread(target=telemetry_thread)
t_t.daemon = True
t_t.start()
