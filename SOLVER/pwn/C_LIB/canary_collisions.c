#include <stdlib.h>

#define SIZE_32 4
#define SIZE_64 8

'''
SUMMARY:
    A canary is a a reference to birds, miners used to bring with them into mines to signal when something went WRONG
    Some pwns require some sort of hash collision with the stack canary.
    The stack canary is a 4 byte randomly created number that if modified signals a buffer overflow
    Main techniques
        1) Canary relies on the rand() library which can be timing attacked
        2) Canary can be brute forced on 32 bit machines
'''



int main()
{
    srand(time(0));

    for
}