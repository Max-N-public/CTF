#!/usr/bin/python3

from pwn import *
from time import time
import subprocess

conn = remote("2018shell1.picoctf.com", 48312)

def getnum():
	seed = int(time() % 5000)
	process = subprocess.Popen(['./seedTime', str(seed)], stdout=subprocess.PIPE)
	randVal = process.stdout
	randVal = randVal.readline().strip()
	print("RANDOM INPUT---->" + randVal)
	#print("send seed to C program")
	return randVal

bet = '1000'
outputs = []#list(range(5))

#socket
for x in range(1):
	conn.recvline_contains("Current")
	conn.sendline(bet)	
	sleep(2)
	conn.recvline_contains("number")
	conn.sendline(getnum())		
	outputs.append(str((conn.recvline_contains("Roulette  :")).split(':')[1].strip()))
	#print("ROULETTE OUTPUT --------->" + (conn.recvline_contains("Roulette  :")).split(':')[1].strip())
	sleep(2)	

print(outputs)
conn.interactive()



