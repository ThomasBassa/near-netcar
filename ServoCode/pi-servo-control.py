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

class MyComponent(ApplicationSession):

    def onJoin(self, details):

        def joyMonitor(put):
            print("calling with value {}".format(put))
            #value = 375 - (put*225)
            #pwm.setPWM(3, 0, int(value))

            if put < 0:
             pwm.setPWM( 3, 0, int(425-(put*175)))
            elif put > 0: 
             pwm.setPWM( 3, 0, int(425-(put*275)))
            else:
             pwm.setPWM( 3, 0, 425)

        self.register(joyMonitor, 'aero.near.joyMonitor')
        print("Session Joined.")

if __name__ == '__main__':
    #This is run "first" (really after the servo min/max)
    runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
    runner.run(MyComponent)

# This runs AFTER the runner is killed-- basically never
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


  

   



