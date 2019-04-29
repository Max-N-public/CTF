#RUN INSIDE GDB USING --> source MY-SCRIPT.py

#BYPASS PTRACE ANTI DEBUGGING TECHNIQUE --> TEST 1
#+--------------------------------------------------+
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
#+--------------------------------------------------+

#BYPASS PTRACE TECHNIQUE 2
#+--------------------------------------------------+
#Place into a file --> fake.c
#include <stdio.h>

long ptrace(int x, int y, int z)
{
    printf(":)\n");
    return 0;
}

#RUN --> gcc -m32 -shared -fPIC -o fake.so fake.c
#RUN --> LD_PRELOAD=./fake.so ./isengard
#+--------------------------------------------------+