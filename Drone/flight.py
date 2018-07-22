import time
from FlightLib import FlightLib as f
f.init('SingleCleverFlight')
from FlightLib import LedLib as led

led.wipe_to(0, 255, 0)

f.takeoff(1.5)
led.rainbow()

f.reach(0.25, 0.25, 1.2)
led.fade_to(255, 0, 0)

f.reach(1.35, 0.25, 1.2)
led.fade_to(0, 255, 0)

f.reach(1.35, 2.2, 1.2)
led.fade_to(0, 0, 255)

f.reach(0.25, 2.2, 1.2)
led.fade_to(255, 255, 0)

f.reach(0.25, 0.25, 1.2)


led.chase(0, 255, 0)
f.land()
led.off()
time.sleep(3)


