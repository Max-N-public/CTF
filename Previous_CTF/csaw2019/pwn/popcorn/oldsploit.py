#!/bin/usr/env python
from pwn import *

exe = context.binary = ELF('./popcorn')
libc = ELF('./libc.so.6')

#Many command line args can be controlled
#./exploit.py DEBUG NOASLR
#./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'localhost'
port = int(args.PORT or 1234)
#start nc local
#ncat -e <exe>

#GDB will be launched if this is sent
#./exploit.py GDB

#adaptable break
#break *0x{exe.symbols.main:x}
gdbscript = '''
break *0x00401152
continue
'''.format(**local())

#execute locally
def local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

#connect remotely
def remote(argv=[], *a, **kw):
    conn = connect(host, port)
    if args.GDB:
        gdb.attach(conn, gdbscript=gdbscript)
    return conn

start = local if args.LOCAL else remote

############################################
#              EXPLOIT
############################################
conn = start()

#NONE TEMPLATE


#NONE TEMPLATE END

conn.interactive()
