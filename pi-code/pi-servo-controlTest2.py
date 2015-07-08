#!/usr/bin/python
#from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
#import time

# This is executed before anything else

# Initialise the PWM device using the default address
pwm = PWM(0x40,debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


class MyComponent(ApplicationSession):

    def onJoin(self, details):

        def joyMonitor(servo, motor):

            print("calling with value {}".format(servo))

            if servo < 0:
                pwm.setPWM( 3, 0, 320)
            elif servo > 0: 
                pwm.setPWM( 3, 0, 510)
            else:
                pwm.setPWM( 3, 0, 417)

        #register all the methods we'll need
        self.register(joyMonitor, 'aero.near.joyMonitor')

        print("Session Joined.")

        #face the car's wheels forward
        pwm.setPWM(3, 0, 417)


if __name__ == '__main__':
    #This is run "first" (really after the servo min/max)
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)


  

   



