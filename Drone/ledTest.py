from FlightLib import LedLib as led
import time

time.sleep(0.1)
print("Starting test...")
print("Fill")
led.fill(255, 0, 0)
time.sleep(5)
print("Wipe")
led.wipe_to(0, 255, 0)
led.wipe_to(255, 0, 0, direction=True)
print("Fade")
led.fade_to(0, 255, 255)
print("Rainbow")
led.rainbow()
time.sleep(10)
print("Chase")
led.chase(255, 0, 255)
time.sleep(5)
led.chase(255, 0, 255, direction=True)
time.sleep(5)
print("Run")
led.run(0, 255, 255, 15, direction=True)
time.sleep(10)
print("Blink")
led.blink(255, 255, 255)
time.sleep(10)
led.off()
print("The end")
time.sleep(3)
