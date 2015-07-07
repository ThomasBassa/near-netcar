
#======================================================================================================================
#Code for LIDAR?
#======================================================================================================================

from Adafruit_I2C import write8, readList

LIDARLite_ADDRESS =  0x62          # Default I2C Address of LIDAR-Lite.
RegisterMeasure   =  0x00          # Register to write to initiate ranging.
MeasureValue      =  0x04          # Value to initiate ranging.
RegisterHighLowB  =  0x8f          # Register to get both High and Low bytes in 1 call.

lidar = Adafruit_I2C(LIDARLite_ADDRESS)

def pull_lidar():
  #Write 0x04 to register 0x00
  lidar.write8(RegisterMeasure, MeasureValue) #Write 0x04 to 0x00

  #distanceArray=[0,0] # array to store distance bytes from read function

  # Read 2byte distance from register 0x8f
  distance = lidar.readList(RegisterHighLowB, 2) # Read 2 Bytes from LIDAR-Lite Address and store in array

  #int distance = (distanceArray[0] << 8) + distanceArray[1];  # Shift high byte [0] 8 to the left and add low byte [1] to create 16-bit int

  # Print Distance
  return distance

if __name__ == '__main__':
	while True:
		print pull_lidar()
