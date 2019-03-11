#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;

unsigned long check_password(char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        char *input[21] = "AAAABBBBCCCCDDDDEEEE";
        if(strlen(input) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( input )){
                puts("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
