/*
general attack:
we need to fill then name buffer with predefined values
        -fill with data
        -fills to 99-23+\x00
Use the scanf do send to addresses with the defined values
        -x/100wx $esp

top of stack changes --> 2nd passcode2 --> 13371337 --> 00CC07C9
\xC9\x07\xCC\x00
2nd of top changes --> 1st passcode1 --> place 338150?
528E6
\xE6\x28\x05\x00


#include <stdio.h>
#include <stdlib.h>

void login(){
        int passcode1;//where are you?
        int passcode2;

        printf("enter passcode1 : ");

        scanf("%d", passcode1);
        //I want hex FFBD2734 I think
        fflush(stdin);

        // ha! mommy told me that 32bit is vulnerable to bruteforcing :)
        printf("enter passcode2 : ");
        scanf("%d", passcode2);

        printf("checking...\n");
        if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
                exit(0);
        }
}

/*                              //passcode1?    //passcode22?
!!0xffbd2730:     !!0x08048783      //0x00414141//      0x41414141      0x41414141
0xffbd2740:     0x41414141      0x41414141      //0x00414141//     0x41ca1b00
*/

//99 A's plus null byte
//AAAABBBBCCCCDDDDEEEEAAAABBBBCCCCDDDDEEEEAAAABBBBCCCCDDDDEEEEAAAABBBBCCCCDDDDEEEE
//python -c 'print ("A"*4 + "B"*4 + "C"*4 + "D"*4 + "E"*4)*4'

void welcome(){
        char name[100];
        printf("enter you name : ");
        scanf("%100s", name);
        printf("Welcome %s!\n", name);
}

int main(){
        printf("Toddler's Secure Login System 1.0 beta.\n");

        welcome();
        login();

        // something after login...
        printf("Now I can safely trust you that you have credential :)\n");
        return 0;
}