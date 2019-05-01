



'''
When the function addresses are randomized you need to use the provided libc library to calculate the offset

High Level
1)Leak the address of a library function in the GOT. In this case, we’ll leak memset()’s GOT entry, which will give us memset()’s address.
2)Get libc’s base address so we can calculate the address of other library functions. libc’s base address is the difference between memset()’s address, and memset()’s offset from libc.so.6.
3)A library function’s address can be obtained by adding its offset from libc.so.6 to libc’s base address. In this case, we’ll get system()’s address.
4)Overwrite a GOT entry’s address with system()’s address, so that when we call that function, it calls system() instead.


https://blog.techorganic.com/2016/03/18/64-bit-linux-stack-smashing-tutorial-part-3/
'''
