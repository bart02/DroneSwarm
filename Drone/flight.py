from FlightLib import FlightLib as f
from FlightLib import LedLib as led

led.fill(255, 255, 255)
f.takeoff()
led.fill(0, 255, 0)
f.land()
led.fill(0, 0, 0)