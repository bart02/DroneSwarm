from __future__ import print_function
from threading import Thread
import time
import rospy
from clever import srv


def init(node_name="TelemLib"):
    print("Initing telemetry node")
    rospy.init_node(node_name)
    print("Node inited")


get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

wait_ms = 100


def telemetry_thread():
    while True:
        telemetry = get_telemetry(frame_id='aruco_map')
        x = round(telemetry.x, 3)
        y = round(telemetry.y, 3)
        z = round(telemetry.z, 3)
        # TODO put your TCD sending code here
        time.sleep(wait_ms/1000)


t_t = Thread(target=telemetry_thread)
t_t.daemon = True
t_t.start()