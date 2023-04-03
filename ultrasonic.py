from machine import Pin
import time

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


while True:
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signal_off = time.ticks_us()
    while echo.value() == 1:
        signal_on = time.ticks_us()
    timepassed = signal_on - signal_off
    distance = (timepassed * 0.0343) / 2
    print(f"Distance: {distance} cm")
    time.sleep(0.1) 