#!/usr/bin/env python2

import base64
from pwn import *
import time

context.terminal = 'bash'
#context.log_level = 'debug'
#context.arch = 'amd64'

DEBUG = 0

###Env
#+----------------------------------+
binary_name = ''
###Function addresses
#+----------------------------------+

#+----------------------------------+
###Args & globals

#+----------------------------------+
###Gadgets

#+----------------------------------+


#Create payload
#+----------------------------------+
payload = ''


#+----------------------------------+



if DEBUG:
    conn = process('./chain_of_rope')
else:
    #remotely connect to the challenge
    conn = remote('', )



if DEBUG:
    conn.interactive()
