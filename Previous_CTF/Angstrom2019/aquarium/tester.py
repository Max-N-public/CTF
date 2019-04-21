#!/usr/bin/env python2

from pwn import *

payload = ''
payload += p64(0x4011b6)
second = ''
second += pack(0x4011b6)

print(payload)
print(second)
