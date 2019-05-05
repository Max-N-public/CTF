#!/usr/bin/env python

'''
'''

#notes
#64 bit
#Canary and aslr
#You need to leak libc address
#!!!looking at arguments you can tell where the read buffer is stored
#--->I.E. in mov rsi, rax then its in rsi