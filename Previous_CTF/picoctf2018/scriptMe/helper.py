#!/usr/bin/python3

loop = 1
while(loop == 1):
	try:
		execfile("script.py")
		loop = 0
		print("ROUNDS COMPLETE")
	except:

		sleep(1)
		print('RESET')
		
