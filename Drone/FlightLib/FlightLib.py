#!/usr/bin/python
# imports
from __future__ import print_function
import math
import sys
import rospy
from clever import srv
from mavros_msgs.srv import SetMode
from mavros_msgs.srv import CommandBool


# init ros node
def init(node_name="CleverSwarmFlight"):
    print("Initing")
    rospy.init_node(node_name)
    print("Node inited")


# create proxy service
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
arming = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
print("Proxy services inited")

# variables
x_current = 0
y_current = 0
z_current = 0


# functions

# noinspection PyCompatibility
def safety_check():
    telemetry = get_telemetry(frame_id='aruco_map')
    print("Telems are:", "x=", telemetry.x, ", y=", telemetry.y, ", z=", telemetry.z, "yaw=", telemetry.yaw, "pitch=",
          telemetry.pitch,
          "roll=", telemetry.pitch)
    telemetry = get_telemetry(frame_id='fcu_horiz')
    print("Telems are:", "V-z=", telemetry.vz, "voltage=", telemetry.voltage)
    raw_input("Are you sure about launch?")
    ans = raw_input("Are you ready to launch? Y/N: ")
    if ans.lower() != "y":
        sys.exit()


def get_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def capture_position(frame_id='aruco_map'):
    telemetry = get_telemetry(frame_id=frame_id)

    global x_current
    global y_current
    global z_current

    x_current = round(telemetry.x, 3)
    y_current = round(telemetry.y, 3)
    z_current = round(telemetry.z, 3)


def reach(x, y, z, yaw=float('nan'), yaw_rate=0.0, speed=1.0, tolerance=0.2, frame_id='aruco_map', wait_ms=100,
          timeout=7500):
    navigate(frame_id=frame_id, x=x, y=y, z=z, yaw=yaw, yaw_rate=yaw_rate, speed=speed)
    print('Reaching point | x: ', '{:.3f}'.format(x), ' y: ', '{:.3f}'.format(y), ' z: ', '{:.3f}'.format(z), ' yaw: ',
          '{:.3f}'.format(yaw), sep='')

    # waiting for completion
    telemetry = get_telemetry(frame_id=frame_id)
    time = 0
    while get_distance(x, y, z, telemetry.x, telemetry.y, telemetry.z) > tolerance:
        telemetry = get_telemetry(frame_id=frame_id)
        print('Reaching point | Telemetry | x: ', '{:.3f}'.format(telemetry.x), ' y: ', '{:.3f}'.format(telemetry.y),
              ' z: ', '{:.3f}'.format(telemetry.z), ' yaw: ', '{:.3f}'.format(telemetry.yaw), sep='')
        rospy.sleep(wait_ms / 1000)
        time += wait_ms
        if timeout != 0 and (time >= timeout):
            print('Reaching point | Timed out! | t: ', time, sep='')
            return False
    print("Point reached!")
    return True


def attitude(z, yaw=float('nan'), yaw_rate=0.0, speed=1.0, tolerance=0.2, frame_id='aruco_map', wait_ms=100,
             timeout=7500):
    capture_position(frame_id=frame_id)
    navigate(frame_id=frame_id, x=x_current, y=y_current, z=z, yaw=yaw, yaw_rate=yaw_rate, speed=speed)
    print('Reaching attitude | z: ', '{:.3f}'.format(z), ' yaw: ', '{:.3f}'.format(yaw), sep='')

    # waiting for completion
    telemetry = get_telemetry(frame_id=frame_id)
    time = 0
    while abs(z - telemetry.z) > tolerance:
        telemetry = get_telemetry(frame_id=frame_id)
        print('Reaching attitude | Telemetry | z: ', '{:.3f}'.format(telemetry.z), ' yaw: ', '{:.3f}'.format(telemetry.yaw), sep='')
        rospy.sleep(wait_ms / 1000)
        time += wait_ms
        if timeout != 0 and (time >= timeout):
            print('Reaching attitude | Timed out! | t: ', time, sep='')
            return False
    print("Attitude reached!")
    return True


def rotate_to(yaw, yaw_rate=0.0, tolerance=0.2, speed=1.0, frame_id='aruco_map', wait_ms=100, timeout=5000):
    capture_position(frame_id=frame_id)
    navigate(frame_id=frame_id, x=x_current, y=y_current, z=z_current, yaw=yaw, yaw_rate=yaw_rate, speed=speed)
    print('Reaching angle | yaw: ', '{:.3f}'.format(yaw), sep='')

    # waiting for completion
    telemetry = get_telemetry(frame_id=frame_id)
    time = 0
    while abs(yaw - telemetry.yaw) > tolerance:
        time += wait_ms
        telemetry = get_telemetry(frame_id=frame_id)
        print('Reaching angle | Telemetry | yaw: ', '{:.3f}'.format(telemetry.yaw), sep='')
        rospy.sleep(wait_ms / 1000)
        if timeout != 0 and (time >= timeout):
            print('Reaching angle | Timed out! | t: ', time, sep='')
            return False
    return True


def spin(yaw_rate=0.2, speed=1.0, frame_id='aruco_map', timeout=5000):
    capture_position(frame_id=frame_id)
    navigate(frame_id=frame_id, x=x_current, y=y_current, z=z_current, yaw=float('nan'), yaw_rate=yaw_rate, speed=speed)
    print('Spinning at speed | yaw_rate: ', '{:.3f}'.format(yaw_rate), sep='')
    rospy.sleep(timeout / 1000)

    navigate(frame_id=frame_id, x=x_current, y=y_current, z=z_current, yaw=float('nan'), yaw_rate=0.0, speed=speed)
    print('Spinning complete | Timeout | t: ', time, sep='')
    return True


def takeoff(z=1, z_coefficient=0.9, speed=1.0, yaw=float('nan'), frame_id='fcu_horiz', tolerance=0.25, wait_ms=50,
            timeout_arm=5000, timeout=7500):
    print("Taking off!")
    navigate(frame_id=frame_id, x=0, y=0, z=z * z_coefficient, yaw=float('nan'), speed=speed, update_frame=False,
             auto_arm=True)

    telemetry = get_telemetry(frame_id=frame_id)
    time = 0
    while not telemetry.armed:
        telemetry = get_telemetry(frame_id=frame_id)
        rospy.sleep(wait_ms / 1000)
        time += wait_ms
        if timeout_arm != 0 and (time >= timeout_arm):
            print("Not armed, timed out. Not ready to flight, exiting!")
            sys.exit()

    print("In air!")
    rospy.sleep(0.25)
    telemetry = get_telemetry(frame_id="aruco_map")
    time = 0
    while z - tolerance > telemetry.z:
        telemetry = get_telemetry(frame_id="aruco_map")
        print('Taking off | Telemetry | z: ', '{:.3f}'.format(telemetry.z), sep='')
        rospy.sleep(wait_ms / 1000)
        time += wait_ms
        if timeout != 0 and (time >= timeout):
            print('Takeoff | Timed out! | t: ', time, sep='')
            return False

    print("Reaching takeoff attitude!")
    result = attitude(z, yaw=yaw, tolerance=tolerance, timeout=timeout)
    if result:
        print("Takeoff attitude reached. Takeoff completed!")
        return True
    else:
        print("Not reached takeoff attitude, timed out")
        return False


def land(z=0.75, wait_ms=100, timeout=10000, timeout_land=5000, preland=True):
    if preland:
        print("Pre-Landing!")
        result = attitude(z, tolerance=0.25, timeout=timeout)
        if result:
            print("Ready to land")
        else:
            print("Not ready to land, trying autoland mode.")

    set_mode(base_mode=0, custom_mode='AUTO.LAND')
    telemetry = get_telemetry(frame_id='aruco_map')
    time = 0
    while telemetry.armed:
        telemetry = get_telemetry(frame_id='aruco_map')
        print('Landing | Telemetry | z: ', '{:.3f}'.format(telemetry.z), ' armed: ', '{:.3f}'.format(telemetry.armed),
              sep='')
        rospy.sleep(wait_ms / 1000)
        time += wait_ms
        if timeout_land != 0 and (time >= timeout_land):
            print("Not detected autoland, timed out. Disarming!")
            arming(False)
            return False
    print("Land completed!")
    return True


if __name__ == "__main__":  # only if run FlightLib directly
    safety_check()
    takeoff()
    land()
