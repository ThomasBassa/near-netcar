
#======================================================================================================================
#Code for LIDAR?
#======================================================================================================================

from Adafruit_I2C import write8, readList

class Lidar:
  
    #
    def __init__(self, address=0x62):
    	self.LIDARLite_ADDRESS =  address          # Default I2C Address of LIDAR-Lite.
      self.RegisterMeasure   =  0x00          # Register to write to initiate ranging.
      self.MeasureValue      =  0x04          # Value to initiate ranging.
      self.RegisterHighLowB  =  0x8f          # Register to get both High and Low bytes in 1 call.
      self.i2c = Adafruit_I2C(self.LIDARLite_ADDRESS, 1)

    #
    def read(self):
	    #Write 0x04 to register 0x00
      self.i2c.write8(self.RegisterMeasure, self.MeasureValue) #Write 0x04 to 0x00

      #delay(1)

      # Read 2 Bytes from LIDAR-Lite Address and store in array
      distanceArray = self.i2c.readList(self.RegisterHighLowB, 2) 
      distance = (distanceArray[0] << 8) | distanceArray[1]  # Shift high byte [0] 8 to the left and add low byte [1] to create 16-bit int

      #this distance is in cm
      return distance
