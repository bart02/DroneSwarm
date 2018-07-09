#!/usr/bin/python
# imports
from __future__ import print_function
import math
import sys
import rospy
from clever import srv
from mavros_msgs.srv import SetMode


# init ros node
def init():
    print("Initing")
    rospy.init_node('CleverSwarmFlight')
    print("Node inited")


# create proxy service
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
print("Proxy services inited")


# variables
yaw_current = 0
x_current = 0
y_current = 0
z_current = 0


# functions
def safety_check():
    telem = get_telemetry(frame_id='aruco_map')
    print("Telems are:", "x=", telem.x, ", y=", telem.y, ", z=", telem.z, "yaw=", telem.yaw, "pitch=", telem.pitch, "roll=", telem.pitch)
    telem = get_telemetry(frame_id='fcu_horiz')
    print("Telems are:", "V-z=", telem.vz, "voltage=", telem.voltage)
    ans = raw_input("Are you sure about launch?")
    ans = raw_input("Are you ready to launch? Y/N: ")
    if ans.lower() != "y":
        sys.exit()


def get_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def capture_position():
    telem = get_telemetry(frame_id='aruco_map')

    global yaw_current
    global x_current
    global y_current
    global z_current

    yaw_current = telem.yaw
    x_current = telem.x
    y_current = telem.y
    z_current = telem.z


def reach(x, y, z, yaw=yaw_current, speed=1, tolerance=0.15, frame_id='aruco_map', freq=5):
    telem = get_telemetry(frame_id=frame_id)
    navigate(frame_id=frame_id, x=x, y=y, z=z, yaw=yaw, speed=speed)
    print("Reaching point:", "x=", x, ", y=", y, ", z=", z, "yaw=", yaw)

    # waiting for completion
    while get_distance(x, y, z, telem.x, telem.y, telem.z) > tolerance:
        telem = get_telemetry(frame_id=frame_id)
        print("Reaching point, telem:", "x=", telem.x, ", y=", telem.y, ", z=", telem.z, "yaw=", telem.yaw)
        rospy.sleep(1 / freq)
    print("Point reached!")


def attitude(z, yaw=yaw_current, speed=1, tolerance=0.2, frame_id='aruco_map'):
    print("Reaching attitude")
    capture_position()
    reach(x=x_current, y=y_current, z=z, yaw=yaw, speed=speed, tolerance=tolerance, frame_id=frame_id)
    print("Attitude reached!")


def takeoff(z=1, speed=1, frame_id='fcu_horiz'):
    print("Taking off!")
    navigate(frame_id=frame_id, x=0, y=0, z=z, speed=speed, update_frame=False, auto_arm=True)
    rospy.sleep(5)
    print("In air!")

    attitude(z, tolerance=0.25)
    print("Takeoff completed!")


def land(z=0.75, freq=5):
    telem = get_telemetry(frame_id='aruco_map')
    print("Pre-Landing!")
    attitude(z, tolerance=0.25)
    print("Ready to land")

    set_mode(base_mode=0, custom_mode='AUTO.LAND')
    while telem.armed:
        telem = get_telemetry(frame_id='aruco_map')
        rospy.sleep(1 / freq)
    print("Land completed!")


if __name__ == "__main__":
    takeoff()
    land()
