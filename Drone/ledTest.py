from FlightLib import LedLib as led
import time

time.sleep(0.1)
print("Starting test...")
led.fill(255, 0, 0)
time.sleep(10)
led.wipe_to(0, 255, 0)
time.sleep(10)
led.rainbow()
time.sleep(10)
led.chase(0, 0, 255)
time.sleep(10)
led.blink(255, 255, 255)
time.sleep(10)
led.off()
