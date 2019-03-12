'''
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) #strip color is stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('missile!', font='cybermedium'), 'green', 'on_grey', attrs=['bold'])
'''

import platform
print("This solver runs on --> " + platform.python_version())

def main_menu():
    #Menu selection block
    print("0: Rev_solver")
    print("1: Pwn_solver")
    print("2: Forensics_solver")
    print("3: Crypto_solver")
    print("4: Web")
    print("5: Misc")

    x = input("--> ")

    if x == 0:
        print("Test1")
    elif x == 1:
        print("Test2")
    elif x == 2:
        print("main_crypto()")

main_menu()

'''
     0: main_rev()
     1: main_pwn()
     2: main_forensics()
     3: main_crypto()
     4: main_web()
     5: main_misc()
'''