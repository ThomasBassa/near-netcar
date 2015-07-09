from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
from pynmea2.stream import NMEAStreamReader
import serial
import time


class GPS:
    #
    def __init__(self):
	    self.ser = serial.Serial('/dev/ttyAMA0', 57600, timeout=1)
	
	    try:
		    self.ser.open()
	    except Exception as e:
            print("Error: {}".format(e))
	
	    return self.ser.isOpen()


	#Attempt to read from the GPS module
	def gpsRead(self):
		return self.ser.readline()
