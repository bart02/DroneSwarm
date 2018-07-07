from FlightLib import LedLib as led
import time

time.sleep(0.1)
print("Starting test...")
print("Fill")
led.fill(255, 0, 0)
time.sleep(10)
print("Wipe")
led.wipe_to(0, 255, 0)
time.sleep(10)
print("Fade")
led.fade_to(255, 0, 0)
time.sleep(10)
print("Rainbow")
led.rainbow()
time.sleep(10)
print("Chase")
led.chase(0, 0, 255)
time.sleep(10)
print("Blink")
led.blink(255, 255, 255)
time.sleep(10)
led.off()
print("The end")
