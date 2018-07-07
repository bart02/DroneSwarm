from __future__ import print_function
import threading
from threading import Thread
import math
import time
from neopixel import *

# LED strip configuration:
LED_COUNT = 29  # Number of LED pixels.
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

r_prev = 0
g_prev = 0
b_prev = 0

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


def rainbow(frequency=5):
    global freq, mode
    freq = frequency
    mode = "rainbow"


def fill(red, green, blue):
    global r, g, b, mode
    r = red
    g = green
    b = blue
    mode = "fill"


def blink(red, green, blue, frequency=5):
    global r, g, b, freq, mode
    r = red
    g = green
    b = blue
    freq = frequency
    mode = "blink"


def chase(red, green, blue, frequency=20):
    global r, g, b, freq, mode
    r = red
    g = green
    b = blue
    freq = frequency
    mode = "chase"


def wipe_to(red, green, blue, frequency=10):
    global r, g, b, freq, mode
    r = red
    g = green
    b = blue
    freq = frequency
    mode = "wipe_to"


def fade_to(red, green, blue, timing=1):  # do not working with rainbow
    global r, g, b, r_prev, g_prev, b_prev, freq, mode
    r_prev = r
    g_prev = g
    b_prev = b
    r = red
    g = green
    b = blue
    freq = timing
    mode = "fade_to"


def off():
    global mode
    mode = "off"


def strip_set(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def strip_chase_step(color):
    for q in range(3):
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i + q, color)
        strip.show()
        time.sleep(1/freq)
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i + q, 0)


def strip_wipe(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        time.sleep(1 / freq)
        strip.show()


def strip_fade(color1, color2):
    pass


def strip_off():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


def led_thread():
    print("Starting thread")
    iteration = 0
    while True:
        if mode == "rainbow":
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, math_wheel((int(i * 256 / strip.numPixels()) + iteration) & 255))
            strip.show()
            time.sleep(1/freq)
        elif mode == "fill":
            strip_set(Color(r, g, b))
            time.sleep(1/freq)
        elif mode == "blink":
            strip_set(Color(r, g, b))
            time.sleep(1 / freq)
            strip_set(Color(0, 0, 0))
            time.sleep(1/freq)
        elif mode == "chase":
            strip_chase_step(Color(r, g, b))
            time.sleep(1 / freq)
        elif mode == "wipe_to":
            strip_wipe(Color(r, g, b))
        elif mode == "fade_to":
            strip_fade(Color(r_prev, g_prev, b_prev), Color(r, g, b))
        elif mode == "off":
            strip_off()

        iteration += 1
        if iteration >= 256:
            iteration = 0


# init
strip.begin()
Thread(target=led_thread).start()