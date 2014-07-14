#!/usr/bin/env python
# 
# Dead simple send console input message to OSC
# (Needs pyOSC)
# by Sam Neurohack
# No licence. It"s not bullet proof, just handy.
# To be improved !!
# 
#  Usage : 
#  OSC destination IP  OSC destination port  OSC command
#
#	192.168.1.3 8000 /box/clear 1 4 2		

import socket, time,random, OSC

while 1:
	var = raw_input("Enter something: ")
	print "You entered", var
	commands = var.split()
	nb_oscargs = len(commands)
	oscargs = 3
	msg = OSC.OSCMessage()
	send_address = commands[0], int(commands[1]) # 0 : IP address 1: port
	c = OSC.OSCClient()
	c.connect( send_address ) # set the address for all following messages
	msg.setAddress(commands[2]) # set OSC address
	print "adresse", commands[2]
	print "data 1", commands[3]
	while oscargs != nb_oscargs:
		#print commands[oscargs]
		msg.append(float(commands[oscargs]))
		oscargs = oscargs + 1
	#msg.append(1) int
	c.send(msg) # send it!  
conn.close()