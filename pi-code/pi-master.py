from pynmea2.stream import NMEAStreamReader
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
import serial
import time
import math
import trollius as asyncio
import os as swag

class MyComponent(ApplicationSession):
	#Begin GPS Code
	@asyncio.coroutine
	def gpsUpdate(self):
		while True:
			print "GPS"

#			gps_string = self.gpsRead()[1:] #getting rid of the stupid $ marker at the beginning of the strings
#			gps_list = string.split(gps_string, ',')
#			if gps_list[0] == "GPRMC":
 #   
#				if gps_list[4] == 'S':
#					self.gps_data['latitude'] = -1 * (float(gps_list[3][0:2]) + (float(gps_list[3][2:])/60.0))
#				else:
#					self.gps_data['latitude'] = (float(gps_list[3][0:2]) + (float(gps_list[3][2:])/60.0))
#				if gps_list[6] == 'W':
#					self.gps_data['longitude'] = -1 * (float(gps_list[5][0:3]) + (float(gps_list[5][3:])/60.0))
#				else:
#					self.gps_data['longitude'] = float(gps_list[5][0:3]) + (float(gps_list[5][3:])/60.0)	
#				self.gps_data['speed'] = (float(gps_list[7]) * 1.15078)
#				self.publish(u'aero.near.carPos', self.gps_data['latitude'], self.gps_data['longitude'])
#				self.publish(u'aero.near.carSpeed', self.gps_data['speed'])
#			elif gps_list[0] == "GPVTG":
#				degrees = float(gps_list[1])
#				if degrees > 90 and degrees < 270:
#					if degrees > 180:
#						self.gps_data['heading'] = "S&#176;{}W".format(degrees-180) #&#176 converted to degree symbol in html
#					else:
#						self.gps_data['heading'] = "S&#176;{}E".format(180-degrees)
#				else:
#					if degrees > 270:
#						self.gps_data['heading'] = "N&#176;{}W".format(360-degrees)
#					else:
#						self.gps_data['heading'] = "N&#176;{}E".format(degrees)
#				self.publish(u'aero.near.carHeading', self.gps_data['heading'])
#	
#			print self.gps_data
			yield asyncio.sleep(.03333)

	def gpsRead(self):
		self.ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
		if self.ser.isOpen():
			print 'Open: '
		data = self.ser.readline()
		return data

	#End GPS code

	def joyMonitor(self, event):
		vertical = event["vertical"]
		horizontal = event["horizontal"]
		swag.system('cls' if swag.name == 'nt' else 'clear')
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
		self.pwm.setPWM(self.servoChannel, 0, value)

	def moveMotor(self, value):
		self.pwm.setPWM(self.motorChannel, 0, value)	    	
        	
	def honk(self):
		#honks the horn for 0.5 s when called
		None
	
	def emergencyStop(self):
		#stop the motors
		None

	def manualOverride(self):
		#???
		None

	def onJoin(self, details):
		print("Session Joined.")
		#Setting variables
		self.lastServoValue = 417 #Assumes it starts in the middle
		self.pwm = PWM(0x40,debug=True)
		self.servoMin = 315  # Min pulse length out of 4096
		self.servoMax = 520  # Max pulse length out of 4096
		self.servoMiddle = 417 # middle servo value
		self.pwm.setPWMFreq(60) # Set frequency to 60 Hz
		self.servoChannel = 3        

		self.pwm.setPWM(self.servoChannel, 0, self.servoMiddle) #have vehicle wheels turn to center
		self.motorMiddle = 1500
		self.motorChannel = 2
		self.subscribe(self.joyMonitor, 'aero.near.joystream')

		#register the methods
		#self.register(self.honk, 'aero.near.honkHorn')
		#self.register(self.emergencyStop, 'aero.near.emergStop')
		#self.register(self.manualOverride, 'aero.near.override')
 		self.gpsloop = asyncio.get_event_loop()
		self.gpsloop.run_until_complete(self.gpsUpdate())
#		self.gpsloop.run_until_complete(self.initializing())
		self.gpsloop.close()
# 		runner.run_until_complete(self.gpsUpdate())
#		gpsloop.close()

	@asyncio.coroutine
	def initializing(self):
		print "Starting"
		self.lastServoValue = 417 #Assumes it starts in the middle
		self.pwm = PWM(0x40,debug=True)
		self.servoMin = 315  # Min pulse length out of 4096
		self.servoMax = 520  # Max pulse length out of 4096
		self.servoMiddle = 417 # middle servo value
		self.pwm.setPWMFreq(60) # Set frequency to 60 Hz
		self.servoChannel = 3        

		self.pwm.setPWM(self.servoChannel, 0, self.servoMiddle) #have vehicle wheels turn to center
		self.motorMiddle = 1500
		self.motorChannel = 2
		self.subscribe(self.joyMonitor, 'aero.near.joystream')

		#register the methods
		#self.register(self.honk, 'aero.near.honkHorn')
		#self.register(self.emergencyStop, 'aero.near.emergStop')
		#self.register(self.manualOverride, 'aero.near.override')

if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)