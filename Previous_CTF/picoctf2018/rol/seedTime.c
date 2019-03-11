#include <stdio.h>

int main(int argc, char **argv)
{
	long random;
    int seed = atoi(argv[1]);
    srand(seed);
    random = (rand() % 36) + 1;
    printf("%lu\n", random);

	return 0;
}