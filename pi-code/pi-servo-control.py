#!/usr/bin/python
#from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
import Serial
import math
#import time

# This is executed before anything else

# Initialise the PWM device using the default address
pwm = PWM(0x40,debug=True)

servoMin = 315  # Min pulse length out of 4096
servoMax = 520  # Max pulse length out of 4096
servoMiddle = 417 # middle servo value

pwm.setPWMFreq(60) # Set frequency to 60 Hz

lastServoValue = 375 #assume it starts in the middle
pwmMaxChange = 15


class MyComponent(ApplicationSession):

    def onJoin(self, details):

        #register the methods
        self.register(honk, 'aero.near.honkHorn')
        self.register(emergencyStop, 'aero.near.emergStop')
        self.register(manualOverride, 'aero.near.override')
        self.register(joyMonitor, 'aero.near.joyMonitor')
        callID = reactor.callLater(.015, emergencyStop)
        print("Session Joined.")

        pwm.setPWM(3, 0, servoMiddle) #have vehicle wheels turn to center

    def moveServos(channel,value):
        pwm.setPWM(channel, 0, value)

    def joyMonitor(servo, motor):

        global lastServoValue

        print "calling joyMonitor with value %d and %d" % (servo, motor)

<<<<<<< Updated upstream
        newServoValue = ((servo * 102.5) + 417.5)

	    moveServos(3,int(newServoValue))

=======
        newServoValue = 375 - servo*225

        if math.fabs(lastServoValue - newServoValue) > pwmMaxChange:
            newServoValue = lastServoValue + math.copysign(pwmMaxChange, (lastServoValue - newServoValue))

        moveServos(3,int(newServoValue))
        lastServoValue = newServoValue

>>>>>>> Stashed changes
        callID.cancel()
        callID = reactor.callLater(.015, emergencyStop)

    def honk():
        #honks the horn for 0.5 s when called
        None

    def emergencyStop():
        #stop the motors
        None

    def manualOverride():
        #???
        None

    def connectGPS():
        None

    def checkGPS():
        session.publish('aero.near.carPos', 200)
        session.publish('aero.near.carSpeed', 250)

    def rotor(servo, motor):
     while(true = true):
        moveservos(2,int(8-servoMiddle))
        time.sleep(.1)
        moveservos(2,int(8+servoMiddle))
        time.sleep(.1)



if __name__ == '__main__':
    #This is run "first" (really after the servo min/max)
    moveServos(3,417)
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
