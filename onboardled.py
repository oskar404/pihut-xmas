from machine import Pin

print("On board LED test")

onboardLED = Pin(25, Pin.OUT)
onboardLED.value(1)
