#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char* strength;
	strength = malloc(sizeof(int) * 8);
	strength[8] = rand() % 10;
	printf(strength);
}