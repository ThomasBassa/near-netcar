from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner
from pynmea2.stream import NMEAStreamReader
import string
import serial
import trollius as asyncio
class MyComponent(ApplicationSession):

	def gpsUpdate(self, gps_string):
		while True:
			gps_string = gps_string[1:] #getting rid of the stupid $ marker at the beginning of the strings
			gps_list = string.split(gps_string, ',')
	
			'''with open('fake_gps.txt', 'r') as data_file:  
				streamer = NMEAStreamReader(data_file)
				gps_data = streamer.next()'''
	
	
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
			asyncio.sleep(.03333)
			print self.gps_data
		#print gps_string[0:6:]
		
		#sleep(.0333)

	def gpsRead(self):
		while True:
			self.ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
			if self.ser.isOpen():
				print 'Open: '
			data = self.ser.readline()
			print data
		return data



	def onJoin(self, details):
		self.gps_data = {'latitude': 0,'longitude': 0,'heading': 0,'speed': 0}
		self.gpsRead()#(self.gpsRead())
		#gpsUpdate(self, '$GPRMC,194530.000,A,3051.8007,N,10035.9989,W,9.76,111.67,310714,,,A*74')
		
	
if __name__ == '__main__':
    print "IM TRYING."
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
	