#!/usr/bin/env python

#https://www.shellblade.net/docs/ret2libc.pdf

'''
TLDR; You want to overflow the buffer so the program returns to system and executes the address of where "/bin/sh" is stored in memory
USED ON NX

ANATOMY:

[Fill the stack frame][Fill ebp with 4 bytes][address of system()][address of exit()][address of "/bin/sh" string]

!!If you cant isolate the "/bin/sh" string using the addresses
0xbffffe4a: "EGG=/bin/sh"
EGG= is 4 bytes --> 4 + 0xbffffe4a = the address you want for "/bin/sh"

You can also use a /bin/sh SLED by --> ///////.../bin/sh into the stack space
Or just write it to the stack as "/bin/sh"
'''