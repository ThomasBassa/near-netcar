#!/usr/bin/python
#from twisted.internet.defer import inlineCallbacks
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
import serial
import math
import trollius as asyncio
import json

class MyComponent(ApplicationSession):

    def moveServos(self, value):
        self.pwm.setPWM(self.servoChannel, 0, value)

    def joyMonitor(self, event):
        vertical = event["vertical"]
        horizontal = event["horizontal"]
        print "calling joyMonitor with value %.3f and %.3f" % (horizontal, vertical)

        newServoValue = int((horizontal * 102.5) + self.servoMiddle)

        #if math.fabs(lastServoValue - newServoValue) > pwmMaxChange:
        #    newServoValue = lastServoValue + math.copysign(pwmMaxChange, (lastServoValue - newServoValue))

        self.moveServos(int(newServoValue))
        self.lastServoValue = newServoValue

    def honk(self):
        #honks the horn for 0.5 s when called
        None

    def emergencyStop(self):
        #stop the motors
        None

    def manualOverride(self):
        #???
        None

    def connectGPS(self):
        None

    def onJoin(self, details):
        print("Session Joined.")    
        self.lastServoValue = 417 #assume it starts in the middle
        #register the methods
        #self.register(honk, 'aero.near.honkHorn')
        #self.register(emergencyStop, 'aero.near.emergStop')
        #self.register(manualOverride, 'aero.near.override')
        self.pwm = PWM(0x40,debug=True)
        self.servoMin = 315  # Min pulse length out of 4096
        self.servoMax = 520  # Max pulse length out of 4096
        self.servoMiddle = 417 # middle servo value
        self.pwm.setPWMFreq(60) # Set frequency to 60 Hz
        self.servoChannel = 3        
        self.pwm.setPWM(3, 0, self.servoMiddle) #have vehicle wheels turn to center
        self.subscribe(self.joyMonitor, 'aero.near.joystream') 

if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
