

#include <stdio.h>
#include <math.h>

void main()
{
    //Take user input
        //add x and y counter
        //create directions 

    //calcuate resultant
    //do output Bullshit

    int loop_calc;
    FILE *fp = NULL;
    fp = fopen("12.txt","r"); 

    fscanf(fp,"%d", &loop_calc);
    
    int x=0, y=0, i;
    for(i = 0; i < loop_calc; i++)
    {
        char temp[100];
        fscanf(fp,"%s", temp);

        if(strcmp(temp, "east") == 0)//-1
            x--;
        else if(strcmp(temp, "north") == 0)
            y--;
        else if(strcmp(temp, "west") == 0)
            x++;
        else if(strcmp(temp, "south") == 0)
            y++;
        else if(strcmp(temp, "northeast") == 0)
        {
            x--;
            y--;
        }
        else if(strcmp(temp, "northwest") == 0)
        {
            x++;
            y--;
        }
        else if(strcmp(temp, "southwest") == 0)
        {
            y++;
            x++;
        }
        else if(strcmp(temp, "southeast") == 0)
        {
            y++;
            x--;
        }

    }


    //find resultant
    
    //result = sqrt(result); SQRT DOESNT IMPORT FOR SOME REASON
    //solve IN CALC
    //printf("\n%d\n%d\n", x, y);
    //manual sqrt


    int result1 = 68/26;  
    int result2 = 26/26;  
    int result3 = 9/26;  
    int result4 = 19/26;  
    int result5 = 17/26;  
    int result6 = 7/26;  
    int result7 = 15/26;  
    int result8 = 9/26;  
    int result9 = 10/26;  
    int result10 = 40/26;  
    int result11 = 18/26;  
    int result12 = 26/26; 

    printf("%d%d%d%d%d%d%d%d%d%d%d%d", result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12);

    //cbaaaaaaabab
    //hsctf{cbaaaaaaabab}
}