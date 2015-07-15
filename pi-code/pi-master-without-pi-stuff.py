from pynmea2.stream import NMEAStreamReader
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import serial
import time
import math
import trollius as asyncio
import os as swag
from trollius import From
import string
import logging
logging.basicConfig()

class MyComponent(ApplicationSession):
	#Begin GPS Code
	@asyncio.coroutine
	def gpsUpdate(self):
		print self.gps_data
		while True:
			print "GPS"
			gps_string = self.gpsRead()[1:] #getting rid of the stupid $ marker at the beginning of the strings
			gps_list = string.split(gps_string, ',')
			print gps_list
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
		data = "$GPRMC,123519,A,4807.038,S,01131.000,W,022.4,084.4,230394,003.1,W*6A"
		print data
		return data

	#End GPS code

	def joyMonitor(self, event):
		vertical = event["vertical"]
		horizontal = event["horizontal"]
		print "calling joyMonitor with value %.3f and %.3f" % (horizontal, vertical)

		newServoValue = int((horizontal * 102.5) + self.servoMiddle)
		newMotorValue = int((vertical * 500) + self.motorMiddle)
		print "New servo value: {}".format(newServoValue)
		print "New motor value: {}".format(newMotorValue)
		#if math.fabs(lastServoValue - newServoValue) > pwmMaxChange:
		#    newServoValue = lastServoValue + math.copysign(pwmMaxChange, (lastServoValue - newServoValue))

		self.moveServos(int(newServoValue))
		self.lastServoValue = newServoValue

		self.moveMotor(int(newMotorValue))
		self.lastMotorValue = newMotorValue

	def moveServos(self, value):
		print "Servo moved to {}".format(value)

	def moveMotor(self, value):
		print "Motor moved to {}".format(value)

	@asyncio.coroutine
	def honk(self):
		while True:
			swag.system('cls' if swag.name == 'nt' else 'clear')
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
		#Setting variables
		self.lastServoValue = 417 #Assumes it starts in the middle
		self.servoMin = 315  # Min pulse length out of 4096
		self.servoMax = 520  # Max pulse length out of 4096
		self.servoMiddle = 417 # middle servo value
		self.servoChannel = 3        
		print "What is happening????"
		self.motorMiddle = 1500
		self.motorChannel = 2
		self.subscribe(self.joyMonitor, 'aero.near.joystream')
		print "joystream ok"
		#subscribe to methods to prevent register conflicts
		self.subscribe(self.honkCommand, 'aero.near.honkHorn')
		print "honk ok"
		self.subscribe(self.emergencyStop, 'aero.near.emergStop')
		print "emergstop ok"
		self.subscribe(self.manualOverride, 'aero.near.override')
		print "About to make the loop"
		self.gps_data = {'latitude': 0,'longitude': 0,'heading': 0,'speed': 0}
		
 		self.loop = asyncio.get_event_loop()
		print self.loop.is_running()
#		self.loop.stop()
#		future = asyncio.Future()
#		print "the future exists"
#		asyncio.async(self.gpsUpdate())
#		self.loop.run_until_complete(future)
#		self.loop = asyncio.new_event_loop()
		self.blazeit = asyncio.new_event_loop()
		asyncio.set_event_loop(self.blazeit) #may or may not work, test tomorrow
		tasks = [
			asyncio.async(self.honk()),
			asyncio.async(self.lidarRead()),
			asyncio.async(self.gpsUpdate())]
		print tasks
		swag.system('cls' if swag.name == 'nt' else 'clear')
		done, pending = yield self.blazeit.run_until_complete(asyncio.wait(tasks))
		print tasks
		print "running"
		self.blazeit.close()
# 		runner.run_until_complete(self.gpsUpdate())

if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)