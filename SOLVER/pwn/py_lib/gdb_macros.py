'''
    TODO:
        get gdb to run the python script
        have the python script stack examine functions written
        somehow format the stack examine to be printed to user
'''


import os
import sys
#import pexpect
import subprocess
import pwn_main

LOG_FILE='/TMP/gdb_logs.txt/../'

#only provide functionality for a single binary currently
files = [
        'babypwn'
        ]

#allow user to input functions they want to break at
func = [
        'main'
        ]




def setup():
    gdb.execute("set pagination off")
    gdb.execute("set print pretty")
    # if connecting to remote target
    # gdb.execute('target remote <ip>:<port>')
    gdb.execute('set logging file %s'%(LOG_FILE))
    gdb.execute('set logging on')
    print('\nReading gdb env..\n')
    gdb.execute('show script-extension')
    gdb.execute('show sysroot')
    gdb.execute('show solib-search-path')
    print('\nSetup complete !\n')

# Acts as an event listener <--> what to do when break point hit
def stop_handler(event):
    print('HIT FUNCTION: %s' % (event))
    stack = grep_gdb("x/100wx $ebp")
    print_output(stack)
    print_libc
    #gdb.execute("p func3_var")
    #gdb.execute("p *func3_ptr")
    user_input = input("Type 1 to continue: ")
    if(user_input == 1)
        gdb.execute("c")
    else
        exit(0)
    
# set bp on all the functions specified in all the files specified in 'this_file'
def set_bp_from_files():
    for f in this_files:
        try:
            gdb.execute("rbreak %s:."%(f))
            print('rbreak %s:.'%(f))
        except:
            print('Error inserting breakpoint %s'%(fn))
    print('\nDone setting breakpoints from list of files\n')

# set breakpoint on all the functions specified in 'this_fn'
def set_bp_from_funs():
    for fn in this_fn:
        if fn:
            try:
                gdb.Breakpoint(fn)
                print('break ' + fn)
            except:
                print('Error inserting breakpoint %s'%(fn))
    print('\nDone setting breakpoints from list of funs\n')

def register_stop_handler():
    gdb.events.stop.connect(stop_handler)
    #unregister
    #gdb.events.stop.disconnect(stop_handler)
    print('\nDone setting stop-handler\n')

def grep_gdb(string):
    return gdb.execute(string, to_string=True)

def print_libc():
    return 
    #not sure how to print
    #set print elements number-of-elements


#TODO!!!: pass pwn filename to gdb
#for some reason calling gdb and running the python script is hard
def setup_gdb():
    child = subprocess.Popen(["gdb", "--command", "gdb_macros.py", "./babypwn"])
    #call('gdb --command gdb_macros.py ./babypwn', shell=True)
    #child = pexpect.spawn('gdb --command gdb_macros.py ./babypwn')
    child.communicate()
    #setup()
    #set_bp_from_funs()
    #set_bp_from_files()
    #register_stop_handler()
    #gdb.execute("c")

setup_gdb()

