#RUN INSIDE GDB USING --> source MY-SCRIPT.py

import gdb

def ptrace_zero():
    gdb.execute("set $rax = 0")
    gdb.execute("c")

def ptrace_neg():
    gdb.execute("set $rax = -1")
    gdb.execute("c")

gdb.execute("file bugger")
gdb.execute("catch syscall ptrace")
gdb.execute("catch syscall readlink")
gdb.execute("run")

ptrace_zero()
ptrace_zero()
ptrace_zero()
ptrace_zero()

ptrace_neg()
ptrace_neg()