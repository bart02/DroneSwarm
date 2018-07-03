import rospy
from clever import srv
from std_srvs.srv import Trigger
from mavros_msgs.srv import SetMode

rospy.init_node('CleverFlight')   # название вашей ROS-ноды

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)