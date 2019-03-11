#include <stdio.h>
#include <stdlib.h>

#define FLAG "-----REDACTED-----"

void interview(int secret) {  

	/* secret = 0  0xdeadbeef = 3735928559
	rand() --> Different values for this program compared to test - gdb debug to find them
	debug --> x/4x $esp+0x08
	1797891066
	1596878256
	1550494404
	1688063051
	808965304

	0x6b29a3fa	0x5f2e6db0	0x5c6aaac4	0x649dcc4b
	0x3037d4b8	0x2920c607	0x136cfb60	0x1a3abd31
	0x42655351	0x5e51be39
	can[] & check [] have all these rand values
    */

    int i, j;
    int canary[10];
    char name[64];
    int check[10];

    for (i = 0; i < 10; ++i) {
        canary[i] = check[i] = rand();
    }

    printf("Welcome to the Future Canary Lab!\n");
    printf("What is your name?\n");
    gets(name); /* vuln */

    for (j = 0; j < 10; ++j) { /*You tripped the buffer and changed the rand values*/
        if (canary[j] != check[j]) 
        {
            printf("Alas, it would appear you lack the time travel powers we desire.\n");
            exit(0);
        }
    }

    if (secret - i + j == 3735928559) 
    {
        printf("You are the one. This must be the choice of Stacks Gate!\n");
        printf("Here is your flag: %s\n", FLAG);
    } else 
    {
        printf("Begone, FBI Spy!\n");
    }

    exit(0);
}

int main() {

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    setbuf(stdout, NULL);

    srand(time(NULL));

    interview(0);

    return 0;
}