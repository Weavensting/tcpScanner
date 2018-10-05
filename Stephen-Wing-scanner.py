#READ ME 

#This scanner works for TCP 40 pts 

#will accept multiple ports 10 pts 

#will allow for variable ttl 20 pts 

#Will print to results to a file 10 pts 

#total 

#80 pts 

#commands to make things easier for you
#also all the files will be written as stephenScan.html for your viewing pleasure

#python3 1.1.1.1 

#python3 1.1.1.1 tcp 

#python3 1.1.1.1 tcp 80

#python3 1.1.1.1 tcp 80-100

#python3 1.1.1.1 tcp 80-100 1 

import socket
import sys
import time
import string
import re
#user input 

max_port = 100
min_port = 1
#scanner 
def scanner(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#set speed if it exists
	if speed !=False:
		sock.settimeout(int(speed))
		print(speed) 
	else:
		#default
		sock.settimeout(.008)
	
	
	try:
		#tcp connect if it works continue else go to except and it's closed
		sock.connect((target, port))
		sock.close()
		print('[*] Port', port, '/tcp','is open')
		#open file and append it
		f=open("stephenScan.html", "a")
		f.write('[*] Port'+ repr(port)+ '/tcp'+' is open')
		f.close()
		return True
	except:
		sock.close()
		print('[*] Port', port, '/tcp','is closed')
		f=open("stephenScan.html", "a")
		f.write('[*] Port'+ repr(port) + '/tcp'+' is closed')
		f.close()

		return False
def scannerUDP(port):
	#tried running udp but always returns open :(
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sock.settimeout(.005)
	f=open("stephenScan.html", "a")
	try:
		sock.connect((target, port))
		sock.close()
		print('[*] Port', port, '/udp','is open')
		f.write('[*] Port', port, '/udp','is open')
		f.close()
		return True
	except:
		sock.close()
		print('[*] Port', port, '/udp','is closed')
		f.write('[*] Port', port, '/udp','is closed')
		f.close()
		return False

def start():
	#create the file 
	f=open("stephenScan.html", "w")
	f.write("Begin Scan")
	f.close()
	#either run one port in tcp udp or both
	if port != False:
		print("Scanning port", port)
		if protocol == "tcp":
			scanner(port)
		elif protocol =="udp":
			scannerUDP(port)
		else:
			scanner(port)
			scannerUDP(port)
		#run multiple ports in tcp udp or both
	else:
		if protocol == "tcp":
			for portNumber in range(min_port, max_port):
				print("Scanning port", portNumber)
				scanner(portNumber)
		elif protocol =="udp":
			for portNumber in range(min_port, max_port):
				print("Scanning port", portNumber)
				scannerUDP(portNumber)
		else:
			for portNumber in range(min_port, max_port):
				print("Scanning port", portNumber)
				scanner(portNumber)
				scannerUDP(portNumber)
	f.close()	
				

# lets do the scan
#check if variables exisit if not set them myself
try:
	speed = sys.argv[4]
except:
	speed = False
try:
	port = sys.argv[3]
	try:
		ports = port.split("-")
		min_port = int(ports[0])
		max_port = int(ports[1])+1
		port = False;

	except:
		min_port = int(port)
		max_port = int(port)
except:
	port = False
try:
	protocol = sys.argv[2]
except:
	#default protocol
	protocol = "tcp" ; 
try:
	target = sys.argv[1]
	start()
except: 
	#if they don't set it up right send them this
	# ip is required the others are required if you want to use the ones behind it
	print("python3 scanner.py <ip #required> <tcp/udp/both> <port> <speed>")
	sys.exit(1)



