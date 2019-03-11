#include <stdio.h>
#include <stdlib.h>

void main() {
	int i, j, z;
    int canary[10];
    char name[64];
    int check[10];
	
	for (i = 0; i < 10; ++i) {
		z = rand();
		printf("%d\n", z);
        canary[i] = check[i] = z;
    }
	
	exit(0);
}