import sys
from colorama import init
init(strip=not sys.stdout.isatty()) #strip color is stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('missile!', font='cybermedium'), 'green', 'on_grey', attrs=['bold'])