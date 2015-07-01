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

        def joyMonitor(servoAxis, motorAxis):
            print("calling with value {}".format(servoAxis))
            #value = 375 - (servoAxis*225)
            #pwm.setPWM(3, 0, int(value))

            if servoAxis < 0:
                for x in range(0,100):
                    pwm.setPWM( 3, 0, int(525-x-(servoAxis*175)))
            elif servoAxis > 0: 
                for x in range(0,100):
                    pwm.setPWM( 3, 0, int(525-x-(servoAxis*275)))
            else:
                pwm.setPWM( 3, 0, 425)
            #TODO do stuff with motorAxis, make engine go vroom

        self.register(joyMonitor, 'aero.near.joyMonitor')
        print("Session Joined.")

if __name__ == '__main__':
    #This is run "first" (really after the servo min/max)
    runner = ApplicationRunner(url = u"ws://10.33.92.126:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
    
   



