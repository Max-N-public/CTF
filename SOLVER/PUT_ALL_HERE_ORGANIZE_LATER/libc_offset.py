
'''
i sh
examine the address space of loaded libraries
Search memory for address within this space and comapre to libc
possible with read call and puts combined
NOW YOU KNOW THE OFFSET AMEN
'''

'''
canary
ebp
eip
'''

'''
b = 1
Bytes.
h = 2
Halfwords (two bytes).
w = 4 --> 32 bit
Words (four bytes). This is the initial default.
g = 8 --> 64 bit
Giant words (eight bytes).

#!!!looking at arguments you can tell where the read buffer is stored
#--->I.E. in mov rsi, rax then its in rsi
'''
'''
libc_base = leak - libc_offset
'''





'''
https://sploitfun.wordpress.com <--- GOOD SHIT
'''


'''
When the function addresses are randomized you need to use the provided libc library to calculate the offset

High Level
1)Leak the address of a library function in the GOT. In this case, we’ll leak memset()’s GOT entry, which will give us memset()’s address.
2)Get libc’s base address so we can calculate the address of other library functions. libc’s base address is the difference between memset()’s address, and memset()’s offset from libc.so.6.
3)A library function’s address can be obtained by adding its offset from libc.so.6 to libc’s base address. In this case, we’ll get system()’s address.
4)Overwrite a GOT entry’s address with system()’s address, so that when we call that function, it calls system() instead.


https://blog.techorganic.com/2016/03/18/64-bit-linux-stack-smashing-tutorial-part-3/
'''


'''
EXAMPLE:

import re

*in gdb*
x puts --> get address of function
x system --> get address of system
offset = gdb_puts - gdb_system

elf = pwn.ELF('./<filename>')
p = elf.process()
print(p.recv())

puts = print(re.findall('puts: (.*)', prompt))[0]
bin_bash = re.findall('useful_string: (.*), prompt)[0]

system = int(puts, 16) - offset

[fill stack][fill ebp 4 bytes][system address][JUNK 4 bytes][/bin/sh string address]

'''
