import paramiko
import re
import string 
import os

print ("not useless garbage")

def jazzercise():
	print "debug1"
	ssh = paramiko.SSHClient()
	print "debug 1.5"
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
	print "debug 1.75"
	ssh.connect('10.33.93.83', username='laurenczech', password='pants')
	print "debug2"
	#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('touch testFile.txt')
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ifconfig')
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('mkdir Destop/Laurenisameanie')
	ifconfig = ""
	print "debug3"
	for line in ssh_stdout:
		ifconfig = ifconfig + line
	print "debug4"	
    
	ip = None
	arr = string.split(ifconfig)
	found = False
	print "debug5"

		#look for the address
	for x in range(0, len(arr)):
		if not found:
			if "inet" == arr[x]:
				ip = arr[x+1][5:]
				found = True
	print "debug6"			

	#print the results
	print ip	
	#self.publish(u'aero.near.onDisconnect', ip)

	print('published')
	print "debug7"

#os.mkdir("/Users/melanie/Desktop/gorbSucks")
jazzercise()
print "debug0"
	