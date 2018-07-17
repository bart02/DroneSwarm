from FlightLib import FlightLib as f
f.init('arm')
from time import sleep

f.arming(True)
sleep(1)
f.arming(False)
