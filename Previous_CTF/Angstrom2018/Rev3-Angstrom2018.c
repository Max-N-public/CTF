#include <stdio.h>
 
void main()
{
    char input[] = "egzloxi|ixw]dkSe]dzSzccShejSi^3q";
    char flag[32] = "";
 
    for(int i = 0; i < 32; i++)
    {
        int num;
        num = (int)input[i];
        num = num + 3;
        flag[i] = num^9;
    }
   
    printf(flag);
       
}