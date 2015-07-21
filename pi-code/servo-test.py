from pynmea2.stream import NMEAStreamReader
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
import serial
import time
import math
import trollius as asyncio
import os as swag
from trollius import From
import logging
import string
from statusCheck import checkStatus
logging.basicConfig()


class MyComponent(ApplicationSession):
	def joyMonitor(self, event):
			vertical = event["vertical"]
			horizontal = event["horizontal"]
			swag.system('cls' if swag.name == 'nt' else 'clear')
			print "calling joyMonitor with value %.3f and %.3f" % (horizontal, vertical)

			newServoValue = int(((horizontal * 102.5) * -1) + self.servoMiddle)
			#newMotorValue = int((vertical * 500) + self.motorMiddle)
			print "New servo value: {}".format(newServoValue)
			#print "New motor value: {}".format(newMotorValue)
			#if math.fabs(lastServoValue - newServoValue) > pwmMaxChange:
			#    newServoValue = lastServoValue + math.copysign(pwmMaxChange, (lastServoValue - newServoValue))

			#self.moveServos(int(newServoValue))
			self.lastServoValue = newServoValue

			#self.moveMotor(int(newMotorValue))
			#self.lastMotorValue = newMotorValue

	def moveServos(self, value):
			self.pwm.setPWM(self.servoChannel, 0, value)		

	def onJoin(self, details):
		print "Session joined"
		self.subscribe(self.joyMonitor, 'aero.near.joystream')
		#Setting variables
		self.lastServoValue = 417 #Assumes it starts in the middle
		self.pwm = PWM(0x40,debug=True)
		self.servoMin = 315  # Min pulse length out of 4096
		self.servoMax = 520  # Max pulse length out of 4096
		self.servoMiddle = 417 # middle servo value
		self.pwm.setPWMFreq(60) # Set frequency to 60 Hz
		self.servoChannel = 3        

		self.pwm.setPWM(self.servoChannel, 0, self.servoMiddle) #have vehicle wheels turn to center
		


if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)			