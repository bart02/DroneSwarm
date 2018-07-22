import time
from FlightLib import FlightLib as f
f.init('CleverSwarmFlight')
from FlightLib import LedLib as led

led.wipe_to(0, 255, 0)

f.takeoff()
led.rainbow()

f.reach(0.2, 0.2, 1)
led.fade_to(255, 0, 0)

f.reach(1, 0.2, 1)
led.fade_to(0, 255, 0)

f.reach(1, 1, 1)
led.fade_to(0, 0, 255)

f.reach(0.2, 1, 1)
led.fade_to(255, 255, 0)

f.reach(0.2, 0.2, 1)


led.chase(0, 255, 0)
f.land()
led.off()
time.sleep(3)


