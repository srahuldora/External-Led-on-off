from machine import Pin
import utime

ledPin = Pin(25,Pin.OUT)

while True:
  ledPin.value(1)
  print("LED ON")
  utime.sleep(1)
  ledPin.value(0)
  print("LED OFF")
  utime.sleep(1)