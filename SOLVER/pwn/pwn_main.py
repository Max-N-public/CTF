#!/usr/bin/python

import subprocess
import string
from subprocess import Popen, PIPE

#/bin/sh shellcode strings
bin_sh_25 = "\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x31\xc0\x99\x31\xf6\x54\x5f\xb0\x3b\x0f\x05"

'''
0xff
|++++++++++++++|
|   \t         |
|   arg3       | <--- 0x00ff332200
|++++++++++++++| 
|   eip        | <--- 0x00ff332200+4
|++++++++++++++|
|   ebp        | <--- 0x00ff332200+4
|
0x00
'''

#test dictionary
testdict = {
        "arg3":"0x00ff332200",
        "EIP":"0x00ff332204",
        "ebp":"0x00ff332208",
        "trashend":"0x00ff33220B",
        "trashstart":"0x00ff332200",
        "int":"0x00ff332200"
    }

def ask_for_bin():
        print("Binaries should be placed in the pwnhold folder")
        print("Input target binary name")
        binary_name = raw_input("name: ")
        return binary_name

#YO WTF DICTIONARIES DONT OUTPUT IN CORRECT ORDER
#https://sourceware.org/gdb/current/onlinedocs/gdb/Python-API.html#Python-API
def print_output(address_list):
    print("Binary info: ELF x86")
    print("|" + "+"*27 + "|")
    for name,address in address_list.items():
        print("|" + " "*27 + "|")
        print("|\t" + name + " - " + " "*(20-len(name)) + "|" + "<---" + address)
        print("|" + " "*27 + "|")
        print("|" + "+"*27 + "|")



#print_output(testdict)
#do I need to open the program in gdb and run script for there?

def backquotes(cmdwords):
        output = subprocess.Popen(cmdwords, stdout=subprocess.PIPE).communicate()[0]
        return output.strip()

stdout = Popen('gdb babypwn', shell=True, stdout=PIPE).stdout
gdb.r
output = stdout.read()
print(output)