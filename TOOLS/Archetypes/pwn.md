# A COMPILED LIST OF ALL PWN CHALL ARCHETYPES

## Challenge Types

* Buffer Overflows
    * Overflow variables
    * Overflow eip
* Shellcoding
    * Crafting Shellcode
    * Crafting NOP sleds
    * Overcoming character filters
* ROP
    * Return-to-libc
    * GOT
    * Function chaining
* Format String
    * Outputting the stack
        * %x %d %s
    * Writing to the stack
        * Low address
            * Use $n
        * High address
            * Chain $hn and $n
* UAF
* Integer overflows + other OBO
    * Off by One loops
    * Overflowing floats/ints/longs
* Python Jailbreak
* Java?
---

## Protections

* NX / DEP
    * Non executable stack
        * Cant buffer overflow
        * Use ROP
        * No shellcode
* RELRO
    * Partial
        * GOT before .bss
            * global var cant buffer overflow GOT
    * FULL
        * GOT read only
            * Can't GOT overwrite
* Stack Canaries
    * PRNG on srand/time for canary creation
    * Bruteforcing 1 byte at a time
        * just brute force x32 bit
    * Format string to leak canary
    * Overwrite and then repair the null byte later
* ASLR
    * Randomized address layout
    * Leak a struct and use math to find offsets

---

## x86 vs x64

* Calling Conventions