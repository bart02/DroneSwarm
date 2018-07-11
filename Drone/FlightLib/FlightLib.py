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
def init():
    print("Initing")
    rospy.init_node('CleverSwarmFlight')
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

def safety_check():
    telem = get_telemetry(frame_id='aruco_map')
    print("Telems are:", "x=", telem.x, ", y=", telem.y, ", z=", telem.z, "yaw=", telem.yaw, "pitch=", telem.pitch,
          "roll=", telem.pitch)
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

    global x_current
    global y_current
    global z_current

    x_current = telem.x
    y_current = telem.y
    z_current = telem.z


def reach(x, y, z, yaw=float('nan'), yaw_rate=0.0, speed=1, tolerance=0.15, frame_id='aruco_map', wait_ms=100,
          timeout=0):
    telem = get_telemetry(frame_id=frame_id)
    navigate(frame_id=frame_id, x=x, y=y, z=z, yaw=yaw, yaw_rate=yaw_rate, speed=speed)
    print("Reaching point:", "x=", x, ", y=", y, ", z=", z, "yaw=", yaw)

    # waiting for completion
    time = 0
    while get_distance(x, y, z, telem.x, telem.y, telem.z) > tolerance:
        time += wait_ms
        telem = get_telemetry(frame_id=frame_id)
        # print("Reaching point, telem:", "x=", telem.x, ", y=", telem.y, ", z=", telem.z, "yaw=", telem.yaw)
        rospy.sleep(wait_ms / 1000)
        if timeout != 0 and (time >= timeout):
            print("Not reached, timed out.")
            return False
    print("Point reached!")
    return True


def attitude(z, yaw=float('nan'), yaw_rate=0.0, speed=1, tolerance=0.2, frame_id='aruco_map', timeout=0):
    print("Reaching attitude")
    capture_position()
    result = reach(x=x_current, y=y_current, z=z, yaw=yaw, yaw_rate=yaw_rate, speed=speed, tolerance=tolerance,
                   frame_id=frame_id, timeout=timeout)
    if result:
        print("Attitude reached!")
        return True
    else:
        print("Attitude not reached, timed out")
        return False


def rotate_to(yaw, yaw_rate=0.0, tolerance=0.2, frame_id='aruco_map', wait_ms=100, timeout=0, timeout_yaw=5000):
    print("Rotating to angle:", yaw)
    capture_position()
    result = reach(x=x_current, y=y_current, z=z_current, yaw=yaw, yaw_rate=yaw_rate, frame_id=frame_id,
                   timeout=timeout)
    if result:
        print("Point hold, rotating")
    else:
        print("Not holded point")

    if not math.isnan(yaw):
        telem = get_telemetry(frame_id=frame_id)
        time = 0
        while abs(yaw - telem.yaw) > tolerance:
            time += wait_ms
            telem = get_telemetry(frame_id=frame_id)
            rospy.sleep(wait_ms / 1000)
            if timeout_yaw != 0 and (time >= timeout_yaw):
                print("Not rotated properly")
                return False
        return True


def spin(yaw_rate=0.2, yaw_final=float('nan'), frame_id='aruco_map', wait_ms=5000):
    print("Spinning at speed:", yaw_rate)
    rotate_to(yaw=float('nan'), yaw_rate=yaw_rate, frame_id=frame_id)
    rospy.sleep(wait_ms / 1000)

    print("Spinning complete on timeout")
    if not math.isnan(yaw_final):
        print("Moving to final angle")
        result = rotate_to(yaw=float('nan'), yaw_rate=yaw_rate, frame_id=frame_id)
        return result
    return True


def takeoff(z=1, speed=1, yaw=float('nan'), frame_id='fcu_horiz', tolerance=0.25, wait_ms=100, timeout=0,
            timeout_arm=7000):
    telem = get_telemetry(frame_id=frame_id)
    print("Taking off!")
    navigate(frame_id=frame_id, x=0, y=0, z=z, speed=speed, update_frame=False, auto_arm=True)
    time = 0
    while not telem.armed:
        time += wait_ms
        telem = get_telemetry(frame_id=frame_id)
        rospy.sleep(wait_ms / 1000)
        if timeout_arm != 0 and (time >= timeout_arm):
            print("Not armed, timed out. Not ready to flight, fatal error!")
            return False

    print("In air!")
    rospy.sleep(1)
    if timeout != 0:
        time = 0
        while abs(z - telem.z) > tolerance:
            time += wait_ms
            telem = get_telemetry(frame_id=frame_id)
            rospy.sleep(wait_ms / 1000)
            if time >= timeout:
                print("Not reached minimal takeoff attitude, trying to resolve...")
    else:
        rospy.sleep(5)

    print("Reaching takeoff attitude!")
    result = attitude(z, yaw, tolerance=0.25)
    if result:
        print("Takeoff attitude reached. Takeoff completed!")
        return True
    else:
        print("Not reached takeoff attitude, timed out")
        return False


def land(z=0.75, wait_ms=100, timeout=15000, timeout_land=10000):
    telem = get_telemetry(frame_id='aruco_map')
    print("Pre-Landing!")
    result = attitude(z, tolerance=0.25, timeout=timeout)
    if result:
        print("Ready to land")
    else:
        print("Not ready to land, trying autoland mode.")

    set_mode(base_mode=0, custom_mode='AUTO.LAND')
    time = 0
    while telem.armed:
        time += wait_ms
        telem = get_telemetry(frame_id='aruco_map')
        rospy.sleep(wait_ms / 1000)
        if timeout_land != 0 and (time >= timeout_land):
            print("Not autolanded, timed out. Disarming!")
            arming(False)
            return False
    print("Land completed!")
    return True


if __name__ == "__main__":
    safety_check()
    takeoff()
    land()
