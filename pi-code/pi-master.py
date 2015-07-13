from pynmea2.stream import NMEAStreamReader
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from Adafruit_PWM_Servo_Driver import PWM
import serial
import time
import math
import trollius as asyncio

class MyComponent(ApplicationSession):
	#Begin GPS Code
	@asyncio.coroutine
	def gpsUpdate(self):
		while True:
			gps_string = self.gpsRead()[1:] #getting rid of the stupid $ marker at the beginning of the strings
	
			'''with open('fake_gps.txt', 'r') as data_file:  
				streamer = NMEAStreamReader(data_file)
				gps_data = streamer.next()'''
	
	
			if gps_string[0:5] == "GPRMC":
				gps_data = {'latitude': 0,'longitude': 0,'heading': 0,'speed': 0}    
				if gps_string[30] == 'S':
					gps_data['latitude'] = -1 * (float(gps_string[19:21]) + (float(gps_string[22:27])/60.0))
				else:
					gps_data['latitude'] = (float(gps_string[19:21]) + (float(gps_string[22:27])/60.0))
				if gps_string[42] == 'W':
					gps_data['longitude'] = -1 * (float(gps_string[31:34]) + (float(gps_string[34:40])/60.0))
				else:
					gps_data['longitude'] = float(gps_string[31:34]) + (float(gps_string[34:40])/60.0)	
				gps_data['speed'] = (float(gps_string[44:48]) * 1.15078)
				#latitude = float(gps_string[19:21]) + (float(gps_string[22:27])/60.0)
				degrees = float(gps_string[50:55])
				if degrees > 90 and degrees < 270:
					if degrees > 180:
						gps_data['heading'] = "S&#176;{}W".format(degrees-180) #&#176 converted to degree symbol in html
					else:
						gps_data['heading'] = "S&#176;{}E".format(180-degrees)
				else:
					if degrees > 270:
						gps_data['heading'] = "N&#176;{}W".format(360-degrees)
					else:
						gps_data['heading'] = "N&#176;{}E".format(degrees)
				print gps_data
	
			#print gps_string[0:6:]
			
			self.publish(u'aero.near.carPos', gps_data['latitude'], gps_data['longitude'])
			self.publish(u'aero.near.carSpeed', gps_data['speed'])
			self.publish(u'aero.near.carHeading', gps_data['heading'])
			yield asyncio.sleep(.03333)

	def gpsRead(self):
		self.ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
		if self.ser.isOpen():
			print 'Open: '
		data = self.ser.readline()
		return data
	#End GPS code

	def moveServos(self, value):
		self.pwm.setPWM(self.servoChannel, 0, value)

	def joyMonitor(self, event):
		vertical = event["vertical"]
		horizontal = event["horizontal"]
		print "calling joyMonitor with value %.3f and %.3f" % (horizontal, vertical)

		newServoValue = int((horizontal * 102.5) + self.servoMiddle)
		newMotorValue = int((vertical * 500) + self.motorMiddle)

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

		self.pwm.setPWM(3, 0, self.servoMiddle) #have vehicle wheels turn to center
		self.motorMiddle = 1500
		self.motorChannel = 2
		self.subscribe(self.joyMonitor, 'aero.near.joystream')

		#register the methods
		#self.register(self.honk, 'aero.near.honkHorn')
		#self.register(self.emergencyStop, 'aero.near.emergStop')
		#self.register(self.manualOverride, 'aero.near.override')

#		self.gpsloop = asyncio.get_event_loop()

#		self.gpsloop.run_until_complete(self.gpsUpdate())

if __name__ == '__main__':
    print "I'M TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)