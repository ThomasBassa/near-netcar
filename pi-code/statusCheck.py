from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import math
import trollius as asyncio
import os as swag
import logging
import string

logging.basicConfig()

def checkStatus():
	return "GPS Status: {}\nLIDAR Status: {}\nCamera Status: {}".format(self.gpsCheck(),self.lidarCheck(),self.camCheck())
	return "Some Garbage"



def gpsCheck():
	gpsOn = True
	self.ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
	if self.ser.isOpen():
		print 'Open: '
	data = self.ser.readline()
	print data
	return data
	gps_string = self.gpsRead()[1:] #getting rid of the stupid $ marker at the beginning of the strings
	gps_list = string.split(gps_string, ',')
	if gps_list[4] == '':
		gpsOn = False		
	return gpsOn		

def lidarCheck(self):
	return False

def cameraCheck(self):
	return False
