"""Blink local"""
import time
import machine

print("Hello World")
p2 = machine.Pin(2,machine.Pin.OUT)
while True:
    p2.on()
    time.sleep(0.5)
    p2.off()
    time.sleep(0.5)

adc = machine.ADC()
adc.read()

machine.DEEPSLEEP_RESET
