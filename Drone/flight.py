import time

from FlightLib import FlightLib as f
f.init()
from FlightLib import LedLib as led

led.fill(255, 255, 255)
f.safety_check()
f.takeoff(yaw=0)
led.rainbow()
f.reach(0.5, 0.5, 1)
led.run(255, 0, 0)
f.spin(yaw_final=0)
led.chase(0, 255, 0)
f.land()
led.off()
time.sleep(3)