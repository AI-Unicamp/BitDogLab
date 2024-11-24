from machine import Pin
from utime import sleep

led_1 = Pin(12, Pin.OUT)
led_2 = Pin(13, Pin.OUT)

while True:
    led_1.value(1)
    led_2.value(0)
    sleep(0.5)
    led_1.value(0)
    led_2.value(1)
    sleep(0.5)
