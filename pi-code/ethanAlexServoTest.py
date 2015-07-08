#!/usr/bin/python
from Adafruit_PWM_Servo_Driver import PWM
import time

# This is executed before anything else

# Initialise the PWM device using the default address
pwm = PWM(0x40,debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMiddle = 375 # middle servo value

pwm.setPWMFreq(60) # Set frequency to 60 Hz

servoChannel = 3

def moveServos(value):
    pwm.setPWM(servoChannel, 0, value)

moveServos(417)
'''
while True:
    for x in range(0,7):
        value = 340 - x*10
        moveServos(value)
        time.sleep(0.25)
        print "value: %d" % value

'''


    
   