# Trinket IO demo
# Welcome to CircuitPython :)

from touchio import *
from digitalio import *
from analogio import *
from board import *
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import dotstar
import time
import neopixel

# One pixel connected internally!
dot = dotstar.DotStar(APA102_MOSI, APA102_SCK, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(D13)
led.direction = Direction.OUTPUT

# Analog input on D0
analog1in = AnalogIn(D0)

# Analog output on D1
aout = AnalogOut(D1)

# Digital input with pullup on D2
button = DigitalInOut(D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Capacitive touch on D3
touch = TouchIn(D3)

# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 16
neopixels = neopixel.NeoPixel(D4, NUMPIXELS, brightness=0.2, auto_write=False)

# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around!
  dot[0] = wheel(i)
  dot.show()

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  # set analog output to 0-3.3V (0-65535 in increments)
  aout.value = i * 256

  # Read analog voltage on D0
  print("D0: %0.2f" % getVoltage(analog1in))

  # use D3 as capacitive touch to turn on internal LED
  if touch.value:
      print("D3 touched!")
  led.value = touch.value

  if not button.value:
      print("Button on D2 pressed!")
      # optional! uncomment below & save to have it sent a keypress
      #kbd.press(Keycode.A)
      #kbd.release_all()

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down
