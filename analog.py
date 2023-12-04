# Imports (including PWM and ADC)
from machine import ADC, Pin, PWM
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LED pin with PWM
red = PWM(Pin(18))

# Set the PWM Frequency
# Sets how often to switch the power between on and off for the LED
red.freq(1000)

# Normal LEDs
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Create a variable for our reading
reading = 0

while True: # Run forever
    
    reading = potentiometer.read_u16() # Read the potentiometer value and set this as our reading variable value
    
    print(reading) # Print the reading
    
    # Set the LED PWM duty cycle to the potentiometer reading value
    # The duty cycle tells the LED for how long it should be on each time
    red.duty_u16(reading)
    
    if reading <= 20000: # If reading is less than or equal to 20000
        amber.value(0)
        green.value(0)
    elif 20000 < reading < 40000: # If reading is between 20000 and 40000
        amber.value(1) # Amber ON
        green.value(0)
    elif reading >= 40000: # If reading is greater than or equal to 40000
        amber.value(0)
        green.value(1) # Green ON    
    
    time.sleep(0.1) # Short delay
