# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # Loop forever
    
    time.sleep(0.2) # Short Delay

    # the order of if-statements is the priority of inputs
    if button1.value() == 1 and button2.value() == 1:
        
        print("Buttons 1 and 2 pressed")
        red.value(1)
        yellow.value(0)
        green.value(0)

    elif button1.value() == 1:
        
        print("Button 1 pressed")
        red.toggle()
        yellow.value(0)
        green.value(0) 

    elif button2.value() == 1:
        
        print("Button 2 pressed")
        red.value(0)
        yellow.toggle()
        green.value(0)

    elif button3.value() == 1:
        
        print("Button 3 pressed")
        red.value(0)
        yellow.value(0)
        green.toggle()

    else: # no buttons are being pressed
        
        red.value(0)
        yellow.value(0)
        green.value(0)
