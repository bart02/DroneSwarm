from FlightLib import LedLib as led
import time

print("Starting test...")
led.fill(255, 0, 0)
time.sleep(1)
led.wipe_to(0, 255, 0)
time.sleep(1)
led.rainbow()
time.sleep(1)
led.chase(0, 0, 255)
time.sleep(1)
led.blink(255, 255, 255)
time.sleep(1)
led.off()