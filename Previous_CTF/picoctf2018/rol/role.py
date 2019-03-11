#!/usr/bin/python3

from pwn import *

conn = remote('2018shell1.picoctf.com', 48312)

for x in range(2):
	print(conn.recvline_contains('>'))
	conn.sendline(str(x))
	conn.recvline_contains('>')
	conn.sendline(str(x))
	role = conn.recvline_contains('Roulette:')
	print(x + "ROLLED FOR -->" + role)
	conn.interactive()
