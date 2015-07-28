import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect('10.33.93.83', username='laurenczech', password='a')
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('touch testFile.txt')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ifconfig')
ifconfig = ""
for line in ssh_stdout:
	ifconfig = ifconfig + line
print ifconfig