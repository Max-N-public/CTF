#!/usr/bin/env python 

import subprocess

proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout = proc.communicate('./monster')


for i in range(1, 1):
	input = "A"*i
	proc.stdout.readline()
	print(proc)