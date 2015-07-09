from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
from pynmea2.stream import NMEAStreamReader
import serial
import time


ser=None

def init_serial():
    global ser  
    ser = serial.Serial('/dev/ttyAMA0',57600,timeout=1)
#   try:
#       ser.open()
#   except Exception as e:
#       print("Error: {}".format(e))
    if ser.isOpen():
        print 'Open: '
    data = ser.readline()
    return data


init_serial()

def doALoop():
    global ser
    data = ser.readline()
    print data

'''class MyComponent(ApplicationSession):


    def onJoin(self, details):
        gpsUpdate(self, '$GPRMC,194530.000,A,3051.8007,N,10035.9989,W,1.49,111.67,310714,,,A*74')'''
        
    
if __name__ == '__main__':
    a = 0
    while a < 100:
        whatevs = ser.readline()
        print whatevs
        a = a + 1
