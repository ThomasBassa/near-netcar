from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
from pynmea2.stream import NMEAStreamReader

def gpsUpdate(self, gps_string):

			gps_string = gps_string[1:] #getting rid of the stupid $ marker at the beginning of the strings

			'''with open('fake_gps.txt', 'r') as data_file:  
				streamer = NMEAStreamReader(data_file)
				gps_data = streamer.next()'''


			if gps_string[0:5] == "GPRMC":
				gps_data = {'latitude': 0,'longitude': 0,'lat-heading': 0,'long-heading': 0,'speed': 0}    
				gps_data['latitude'] = float(gps_string[19:21]) + (float(gps_string[22:27])/60.0)
				gps_data['longitude'] = float(gps_string[31:34]) + (float(gps_string[34:40])/60.0)
				gps_data['speed'] = float(gps_string[44:48])
				latitude = float(gps_string[19:21]) + (float(gps_string[22:27])/60.0)
				print gps_data

			#print gps_string[0:6:]
			
			self.publish(u'aero.near.carPos', gps_data['latitude'], gps_data['longitude'])
			#sleep(.0333)

class MyComponent(ApplicationSession):

	def onJoin(self, details):
		gpsUpdate(self, '$GPRMC,194530.000,A,3051.8007,N,10035.9989,W,1.49,111.67,310714,,,A*74')
		
	
if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://10.33.92.126:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
	