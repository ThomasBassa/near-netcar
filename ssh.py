import paramiko
import re
import string 
import os
print ("not useless garbage")

def jazzercise():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
	ssh.connect('10.33.93.83', username='laurenczech', password='a')
	#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('touch testFile.txt')
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ifconfig')
	ifconfig = ""
	for line in ssh_stdout:
		ifconfig = ifconfig + line

	arr = string.split(ifconfig)
	found = False

		#look for the address
	for x in range(0, len(arr)):
		if not found:
			if "inet" == arr[x]:
				ip = arr[x+1][5:]
				found = True

	#print the results
	print ip	
	#self.publish(u'aero.near.onDisconnect', ip)
	print('published')

os.mkdir("/Users/melanie/Desktop/gorbSucks")
jazzercise()

	