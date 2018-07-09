import time

from FlightLib import FlightLib as f
f.init()
from FlightLib import LedLib as led

led.fill(255, 255, 255)
f.safety_check()
f.takeoff()
led.rainbow()
f.reach(1, 1, 1)
led.chase(0, 255, 0)
f.land()
led.off()
time.sleep(3)
