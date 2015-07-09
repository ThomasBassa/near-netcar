#!/usr/bin/python

import Adafruit_I2C

class ColorSensor:

	TCS34725_CDATAL = 0x14    # Clear channel data
	TCS34725_RDATAL = 0x16    # Red channel data
	TCS34725_GDATAL = 0x18    # Green channel data
	TCS34725_BDATAL = 0x1A    # Blue channel data
	TCS34725_ID = 0x12    # 0x44 = TCS34721/TCS34725, 0x4D = TCS34723/TCS34727 
	TCS34725_ATIME = 0x01    # Integration time 
	TCS34725_ENABLE = 0x00
	TCS34725_ENABLE_PON = 0x01    # Power on - Writing 1 activates the internal oscillator, 0 disables it 
	TCS34725_ENABLE_AEN = 0x02    # RGBC Enable - Writing 1 actives the ADC, 0 disables it 
	TCS34725_INTEGRATIONTIME_2_4MS  = 0xFF   # 2.4ms - 1 cycle    - Max Count: 1024 
	TCS34725_GAIN_4X = 0x01   #  2x gain 

	#
	def enable(self):
		self.i2c.write8(self.TCS34725_ENABLE, self.TCS34725_ENABLE_PON);
 	 	delay(3);
  		self.i2c.write8(self.TCS34725_ENABLE, self.TCS34725_ENABLE_PON | self.TCS34725_ENABLE_AEN);


  	#
	def disable(self):
  		reg = self.i2c.read8(self.TCS34725_ENABLE);
  		self.i2c.write8(self.TCS34725_ENABLE, reg & ~(self.TCS34725_ENABLE_PON | self.TCS34725_ENABLE_AEN));


	#
	def __init__(self, address=0x29):
		self.I2C_Address = address
		self.i2c = Adafruit_I2C(self.I2C_Address, 1)

		#connect
		x = self.i2c.read8(self.TCS34725_ID)

		if x != 0x44:
			print "failed to connect"

		#set the integration time
		self.i2c.write8(self.TCS34725_ATIME, TCS34725_INTEGRATIONTIME_2_4MS);

		#set the gain
  		self.i2c.write8(self.TCS34725_CONTROL, TCS34725_GAIN_4X);

  		#enable it
		self.enable()


	#
	def read(self):
		c = self.i2c.read16(TCS34725_CDATAL)
  		r = self.i2c.read16(TCS34725_RDATAL)
  		g = self.i2c.read16(TCS34725_GDATAL)
  		b = self.i2c.read16(TCS34725_BDATAL)

  		#add a delay here

  	#
  	def interpret(self):

  		if r > 200 and g > 200 and b > 200:
      		return 1
  		elif r > 160 and g > 160 and b > 160:
      		if r == g and g == b:
          		return 1
      		elif r > g:
          		if (g + 6) > r:
              		if g == b:
                  		return 1
              		elif g > b:
                  		if (b + 6) > g:
                      		return 1
                  		else:
                      		return 0
              		else:
                  		if (g + 6) > b:
                      		return 1
                  		else:
                      		return 0
          		else:
              		return 0
      		elif r == g:
          		if g == b:
              		return 1
          		elif g > b:
              		if (b + 6) > g:
                  		return 1
              		else:
                  		return 0
          		else:
              		if (g + 6) > b:
                  		return 1
              		else:
                  		return 0
      		else:
          		if (r + 6) > g:
              		if g == b:
                  		return 1
              		elif g > b:
                  		if (b + 6) > g:
                      		return 1
                  		else:
                      		return 0
              		else:
                  		if (g + 6) > b:
                      		return 1
                  		else:
                      		return 0       
          		else:
              		return 0
  		else:
     		return 0  