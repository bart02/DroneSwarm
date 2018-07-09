from FlightLib import FlightLib as f
f.init()
from FlightLib import LedLib as led

led.fill(255, 255, 255)
f.safety_check()
f.takeoff()
led.fill(0, 255, 0)
f.reach(1, 1, 1)
led.run(255, 0, 0)
f.land()
led.fill(0, 0, 0)