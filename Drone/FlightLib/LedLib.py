import threading
from threading import Thread

import math
import time
from neopixel import *

# LED strip configuration:
LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 21  # GPIO pin connected to the pixels (18 uses PWM!) (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # Set to '1' for GPIOs 13, 19, 41, 45 or 53

# define led strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

# variables
mode = ""
r = 0
g = 0
b = 0
freq = 10


# functions
def math_wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(frequency=10):
    global freq
    global mode
    freq = frequency
    mode = "rainbow"


def fill(red, green, blue):
    global r
    global g
    global b
    global mode
    r = red
    g = green
    b = blue
    mode = "fill"


def blink(red, green, blue, frequency=10):
    global r
    global g
    global b
    global freq
    global mode
    r = red
    g = green
    b = blue
    freq = frequency
    mode = "blink"


def strip_set(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def led_thread():
    iteration = 0
    while True:
        if mode == "rainbow":
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, math_wheel((i + iteration) & 255))
            strip.show()
            time.sleep(1/freq)
        elif mode == "fill":
            strip_set(Color(r, g, b))
            time.sleep(1/freq)
        elif mode == "blink":
            strip_set(Color(r, g, b))
            time.sleep(1/freq)
            strip_set(Color(0, 0, 0))
            time.sleep(1/freq)

        iteration += 1


# init
strip.begin()
Thread(target=led_thread()).start()
