
# importing
import rospy
from clever import srv

rospy.init_node('Phoenix_testFlight')

# creating proxy service

navigate = rospy.ServiceProxy('/navigate', srv.Navigate)

navigate(z=1, speed=0.5, frame_id='fcu_horiz', update_frame=False, auto_arm=True)
print ("___in air___")
