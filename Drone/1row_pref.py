
# importing
import math
import rospy
from clever import srv
from time import sleep
from mavros_msgs.srv import SetMode

rospy.init_node('Phoenix_testFlight')

from FlightLib import LedLib as led

# creating proxy service

navigate = rospy.ServiceProxy('/navigate', srv.Navigate)
set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
get_telemetry = rospy.ServiceProxy('/get_telemetry', srv.GetTelemetry)


def height_adjust(zp, sp=1.0):
    st = get_telemetry()
    navigate(x=st.x, y=st.y, z=zp, speed=sp, frame_id='aruco_map')


def flight_to_point(xp, yp, zp, sp=1):
    navigate(frame_id='aruco_map', x=xp, y=yp, z=zp, speed=sp)


def takeoff(h=1.5):
    print ("___takeoff!___")
    navigate(z=h, speed=1, frame_id='fcu_horiz', update_frame=False, auto_arm=True)
    print ("___in air___")
    rospy.sleep(3.5)
    height_adjust(h)


def land():
    print ("___landing...___")
    set_mode(base_mode=0, custom_mode='AUTO.LAND')
    print ("___landed___")


# flight program

led.wipe_to(0, 255, 0)
takeoff()
led.rainbow()

rospy.sleep(3)
led.chase(0, 255, 0)
land()
led.off()
rospy.sleep(1)
