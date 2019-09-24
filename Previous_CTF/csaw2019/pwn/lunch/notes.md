1) first input
    put input "AAAA" into string 
    Goodbye len(8)
2) 2nd input
    fgets(size 32)

system_wrapper = 0x40085c

[stack] = ?? bytes
[canary] = 8 bytes
[ebp] = 8 bytes
[eip]<--insert system_wrapper

1) step 1
overwrite the strcat buffer and leak canary
[7 bytes of A][\x00] --> [8 byte canary]
2) step 2
pull the canary out of the puts output
and store for later
3) step 3
trash + found_canary + ebp + system_wrapper
