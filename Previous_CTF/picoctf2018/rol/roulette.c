#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>

#define MAX_NUM_LEN 12
#define HOTSTREAK 3
#define MAX_WINS 16
#define ONE_BILLION 1000000000
#define ROULETTE_SIZE 36
#define ROULETTE_SPINS 128
#define ROULETTE_SLOWS 16
#define NUM_WIN_MSGS 10
#define NUM_LOSE_MSGS 5

long cash = 0; //must be greater than 1 billion
long wins = 0; //needs to be greater or equal to 3 

/*
*** means suspis
***you can bet 0 dollars
LONG_MAX = 9223372036854775807
ULONG_MAX = 18446744073709551615
https://www.onlinegdb.com/online_c_compiler <-- test code segments
*/




/*
must be digit checker
int is_digit(char c)
{
    return '0' <= c && c <= '9';
}*/

long get_long() 
{
  printf("> ");
  uint64_t l = 0;
  char c = 0;
  //loop verifies bet is a number
  //only checks 1st value is a digit
  //would only check 3 if the value 33 is inputted
  while(!is_digit(c))
  {
    c = getchar(); //keep scanning input for characters until a digit exists
  }
  //now you know the first char is digit continue looping until the digit chars end
  while(is_digit(c))
  {
      //boundary check is only for values greater
      //what about negative numbers? l var is unsigned so no negative num are possible
      //c is input and then is converted from  char to long
      if(l >= LONG_MAX)
      {
        l = LONG_MAX;
        break;
      }
      //the multiple by ten shifts the placement of the char
      //345 would be 30 then 30* then 500 <--------------------------------------------
      //***suspis
      l *= 10;
      l += c - '0';
      c = getchar();
  }
  while(c != '\n')
  {
      c = getchar();
  }
    
  return l;
}

'''
probably useless because this would be exploitation
'''
long get_rand()
 {
  long seed;
  FILE *f = fopen("/dev/urandom", "r");
  fread(&seed, sizeof(seed), 1, f);
  fclose(f);
  seed = seed % 5000;
  if (seed < 0) seed = seed * -1;
  srand(seed);
  return seed;
}

long get_bet()
{
  while(1) 
  {
    puts("How much will you wager?");
    printf("Current Balance: $%lu \t Current Wins: %lu\n", cash, wins); 
    long bet = get_long(); 
    if(bet <= cash) 
    {
      return bet;
    }
    else
    {
      puts("You can't bet more than you have!");
    }
  }
}

long get_choice() 
{
  while (1)
 {
    printf("Choose a number (1-%d)\n", ROULETTE_SIZE);
    long choice = get_long();
    if (1 <= choice && choice <= ROULETTE_SIZE)
    {
      return choice;
    }
    else
    {
      puts("Please enter a valid choice.");
    }
  }
}

/*
USELESS
ONLY CALLED WHEN PROPER CONDITIONS ARE MET

int print_flag()
 {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Failed to open the flag file\n");
    return -1;
  }
  fgets(flag, sizeof(flag), file);
  printf("%s", flag);
  return 0;
}*/

/*
USELESS
const char *win_msgs[NUM_WIN_MSGS] = 
{
  "Wow.. Nice One!",
  "You chose correct!",
  "Winner!",
  "Wow, you won!",
  "Alright, now you're cooking!",
  "Darn.. Here you go",
  "Darn, you got it right.",
  "You.. win.. this round...",
  "Congrats!",
  "You're not cheating are you?",
};*/

/*
USELESS
const char *lose_msgs1[NUM_LOSE_MSGS] = {
  "WRONG",
  "Nice try..",
  "YOU LOSE",
  "Not this time..",
  "Better luck next time..."
};*/

/*
USELESS
const char *lose_msgs2[NUM_LOSE_MSGS] = 
{
  "Just give up!",
  "It's over for you.",
  "Stop wasting your time.",
  "You're never gonna win",
  "If you keep it up, maybe you'll get the flag in 100000000000 years"
};*/

void spin_roulette(long spin)
 {
  int n;
  puts("");
  printf("Roulette  :  ");
  int i, j;
  int s = 12500;
  for (i = 0; i < ROULETTE_SPINS; i++)
  {
    n = printf("%d", (i%ROULETTE_SIZE)+1);
    usleep(s);
    for (j = 0; j < n; j++)
    {
      printf("\b \b");
    }
  }
  for (i = ROULETTE_SPINS; i < (ROULETTE_SPINS+ROULETTE_SIZE); i++)
  {
    n = printf("%d", (i%ROULETTE_SIZE)+1);
    if (((i%ROULETTE_SIZE)+1) == spin)
    {
      for (j = 0; j < n; j++)
      {
        printf("\b \b");
      }
      break;
    }
    usleep(s);
    for (j = 0; j < n; j++)
    {
      printf("\b \b");
    }
  }
  for (int k = 0; k < ROULETTE_SIZE; k++)
  {
    n = printf("%d", ((i+k)%ROULETTE_SIZE)+1);
    s = 1.1*s;
    usleep(s);
    for (j = 0; j < n; j++)
    {
      printf("\b \b");
    }
  }
  printf("%ld", spin);
  usleep(s);
  puts("");
  puts("");
}

void play_roulette(long choice, long bet)
 {
  
  printf("Spinning the Roulette for a chance to win $%lu!\n", 2*bet);
  long spin = (rand() % ROULETTE_SIZE)+1;

  spin_roulette(spin);
  
  if (spin == choice)
  {
    cash += 2*bet;
    puts(win_msgs[rand()%NUM_WIN_MSGS]);
    wins += 1;
   }
  else 
{
    puts(lose_msgs1[rand()%NUM_LOSE_MSGS]);
    puts(lose_msgs2[rand()%NUM_LOSE_MSGS]);
  }
  puts("");
}

'''
START OF EXECUTION
'''
int main(int argc, char *argv[])
{
  setvbuf(stdout, NULL, _IONBF, 0);

  cash = get_rand();
  
  puts("Welcome to ONLINE ROULETTE!");
  printf("Here, have $%ld to start on the house! You'll lose it all anyways >:)\n", cash);
  puts("");
  
  long bet;
  long choice;
  //infinite loop until you run out of money
  while(cash > 0)
  {
      bet = get_bet();
      cash -= bet;
      choice = get_choice();
      puts("");
      
      play_roulette(choice, bet);
      
      if (wins >= MAX_WINS)
      {
        printf("Wow you won %lu times? Looks like its time for you cash you out.\n", wins);
        printf("Congrats you made $%lu. See you next time!\n", cash);
        exit(-1);
      }
      
      if(cash > ONE_BILLION) 
      {
          printf("*** Current Balance: $%lu ***\n", cash);
          if (wins >= HOTSTREAK)
          {
              puts("Wow, I can't believe you did it.. You deserve this flag!");
              print_flag();
              exit(0);
          }
          else
          {
            puts("Wait a second... You're not even on a hotstreak! Get out of here cheater!");
            exit(-1);
          }
      }
  }
  puts("Haha, lost all the money I gave you already? See ya later!");
  return 0;
}
