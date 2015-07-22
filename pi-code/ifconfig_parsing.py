import re
import string
def IfconfigParsing():
	ifconfig = """

	ath0      Link encap:Ethernet  HWaddr DC:9F:DB:00:DE:12  
	          inet addr:10.33.93.141  Bcast:10.33.93.255  Mask:255.255.254.0
	          UP BROADCAST RUNNING PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
	          RX packets:342 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:61 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:0 
	          RX bytes:39143 (38.2 KiB)  TX bytes:5409 (5.2 KiB)

	eth0      Link encap:Ethernet  HWaddr DC:9F:DB:01:DE:12  
	          inet addr:192.168.1.21  Bcast:192.168.1.255  Mask:255.255.255.0
	          inet6 addr: fe80::de9f:dbff:fe01:de12/64 Scope:Link
	          UP BROADCAST RUNNING PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
	          RX packets:157 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:56 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:20804 (20.3 KiB)  TX bytes:6317 (6.1 KiB)

	lo        Link encap:Local Loopback  
	          inet addr:127.0.0.1  Mask:255.0.0.0
	          UP LOOPBACK RUNNING  MTU:16436  Metric:1
	          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:0 
	          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

	wifi0     Link encap:Ethernet  HWaddr DC:9F:DB:00:DE:12  
	          UP BROADCAST RUNNING MULTICAST  MTU:2286  Metric:1
	          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:2000 
	          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
	          Interrupt:48 Memory:b0000000-b0010000 
	"""
	arr = string.split(ifconfig)
	found = False
	for x in range(0, len(arr)):
		if not found:
			if "inet" == arr[x]:
				ip = arr[x+1][5:]
				found = True
	print ip	
#for through arr
#if inet
#string.split next one by ':'
#string.split second index by '.'

