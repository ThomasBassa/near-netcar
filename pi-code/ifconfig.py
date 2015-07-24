import sys
import os

def ifconfig():
	os.system("ifconfig > ipdata")
	with open ("ipdata.txt", "r") as myfile:
		data = myfile.read().replace('/n', '')
	print data
ifconfig	