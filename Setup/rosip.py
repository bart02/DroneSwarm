import socket
import fcntl
import struct
from subprocess import check_output, call

files = ['/home/pi/.bashrc',
         '/home/pi/catkin_ws/src/clever/clever/launch/mavros.launch',
         '/home/pi/catkin_ws/src/clever/deploy/roscore.env']


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname[:15]))
    )[20:24])


def replace(file, old, new):
    with open(file, 'r+') as f:
        text = f.read()
        text = text.replace(old, new)
        f.seek(0)
        f.write(text)
        f.truncate()


ros_ip = check_output("echo $ROS_IP")
ip = get_ip_address('wlan0')
for fil in files:
    replace(fil, ros_ip, ip)

print "Please, hard reboot the copter"
# TODO: test it
