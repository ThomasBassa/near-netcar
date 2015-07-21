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
	#Begin GPS Code
	@asyncio.coroutine
	def gpsUpdate(self):
		while True:
			swag.system('cls' if swag.name == 'nt' else 'clear')
			gps_string = self.gpsRead()[1:] #getting rid of the stupid $ marker at the beginning of the strings
			gps_list = string.split(gps_string, ',')
			if gps_list[0] == "GPRMC":
				if gps_list[4] == 'S':
					self.gps_data['latitude'] = -1 * (float(gps_list[3][0:2]) + (float(gps_list[3][2:])/60.0))
				else:
					self.gps_data['latitude'] = (float(gps_list[3][0:2]) + (float(gps_list[3][2:])/60.0))
			 	if gps_list[6] == 'W':
			 		self.gps_data['longitude'] = -1 * (float(gps_list[5][0:3]) + (float(gps_list[5][3:])/60.0))
			 	else:
			 		self.gps_data['longitude'] = float(gps_list[5][0:3]) + (float(gps_list[5][3:])/60.0)	
			 	self.gps_data['speed'] = (float(gps_list[7]) * 1.15078)
			 	self.publish(u'aero.near.carPos', self.gps_data['latitude'], self.gps_data['longitude'])
			 	self.publish(u'aero.near.carSpeed', self.gps_data['speed'])
			elif gps_list[0] == "GPVTG":
				degrees = float(gps_list[1])
			 	if degrees > 90 and degrees < 270:
			 		if degrees > 180:
			 			self.gps_data['heading'] = "S&#176;{}W".format(degrees-180) #&#176 converted to degree symbol in html
			 		else:
			 			self.gps_data['heading'] = "S&#176;{}E".format(180-degrees)
			 	else:
			 		if degrees > 270:
			 			self.gps_data['heading'] = "N&#176;{}W".format(360-degrees)
			 		else:
			 			self.gps_data['heading'] = "N&#176;{}E".format(degrees)
			 	self.publish(u'aero.near.carHeading', self.gps_data['heading'])
			print self.gps_data
			yield From(asyncio.sleep(.03333))

	def gpsRead(self):
		self.ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
		if self.ser.isOpen():
			print 'Open: '
		data = self.ser.readline()
		print data
		return data

	#End GPS code

	def joyMonitor(self, event):
		vertical = event["vertical"]
		horizontal = event["horizontal"]
		swag.system('cls' if swag.name == 'nt' else 'clear')
		print "calling joyMonitor with value %.3f and %.3f" % (horizontal, vertical)

		newServoValue = int(((126 * horizontal) * -1) + self.servoMiddle)
		newMotorValue = int(((vertical * 102.4) * -1) + self.motorMiddle)
		print "New servo value: {}".format(newServoValue)
		print "New motor value: {}".format(newMotorValue)
		#if math.fabs(lastServoValue - newServoValue) > pwmMaxChange:
		#    newServoValue = lastServoValue + math.copysign(pwmMaxChange, (lastServoValue - newServoValue))

		self.moveServos(int(newServoValue))
		self.lastServoValue = newServoValue

		self.moveMotor(int(newMotorValue))
		self.lastMotorValue = newMotorValue

	def moveServos(self, value):
		self.pwm.setPWM(self.servoChannel, 0, value)

	def moveMotor(self, value):
		self.pwm.setPWM(self.motorChannel, 0, value)

	@asyncio.coroutine
	def honk(self):
		print "attempting to start honk loop"
		while True:
			print "HONK"
			yield From(asyncio.sleep(2))
			#honks the horn for 0.5 s when called
	
	def honkCommand(self, event):
		print "HONK"
	
	def emergencyStop(self, event):
		#stop the motors
		None

	def manualOverride(self, event):
		#???
		None

	@asyncio.coroutine	
	def lidarRead(self):
		while True:
			print "Reading LIDAR"	
			yield From(asyncio.sleep(.03333))

	def onJoin(self, details):
		print("Session Joined.")
		#res = yield self.call('aero.near.checkStatus')
		#print("Got result: {}".format(res))

		#Setting variables
		self.lastServoValue = 417 #Assumes it starts in the middle
		self.pwm = PWM(0x40,debug=True)
		self.servoMin = 268  # Min pulse length out of 4096
		self.servoMax = 520  # Max pulse length out of 4096
		self.servoMiddle = 394 # middle servo value
		self.pwm.setPWMFreq(50) # Set frequency to 60 Hz
		self.servoChannel = 3        

		self.pwm.setPWM(self.servoChannel, 0, self.servoMiddle) #have vehicle wheels turn to center
		print "What is happening????"
		self.motorMiddle = 307.2
		self.motorChannel = 0
		self.subscribe(self.joyMonitor, 'aero.near.joystream')
		print "joystream ok"
		#subscribe to methods to prevent register conflicts
		self.subscribe(self.honkCommand, 'aero.near.honkHorn')
		print "honk ok"
		self.subscribe(self.emergencyStop, 'aero.near.emergStop')
		print "emergstop ok"
		self.subscribe(self.manualOverride, 'aero.near.override')
		#self.register(checkStatus, u'aero.near.checkStatus')
		print "About to make the loop"
		self.gps_data = {'latitude': 0,'longitude': 0,'heading': 0,'speed': 0}
		swag.system('cls' if swag.name == 'nt' else 'clear')
		
 		self.loop = asyncio.get_event_loop()
		tasks = [
			asyncio.async(self.gpsUpdate()),
			asyncio.async(self.honk()),
			asyncio.async(self.lidarRead())]
		print tasks
		try:
			done, pending = yield self.loop.run_until_complete(asyncio.wait(tasks))
		except Exception as e:
			print e
		print tasks
		print "running"
		self.loop.close()
# 		runner.run_until_complete(self.gpsUpdate())

if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)