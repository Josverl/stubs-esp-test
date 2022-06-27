# Neopixel
import esp
from machine import Pin

# For low-level driving of a NeoPixel:
pin = Pin(18)
grb_buf = (1, 20, 2, 40)
is800khz = False

# Note: ESP8266 only

esp.neopixel_write(pin, grb_buf, is800khz) # type: ignore # FIXME: Is not resolved yet
