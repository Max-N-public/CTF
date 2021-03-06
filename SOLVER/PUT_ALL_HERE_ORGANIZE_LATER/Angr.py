
'''
The basics of symbolic execution
How to become a rev g0d
'''

#load binary into angr object
proj = angr.Project('bomb', load_options={'auto_load_libs':False})

#Start at a certain address without running the rest
state = proj.factory.blank_state(addr=0x400f0a)

#You might want to start blank state right after a scanf input
#Therefore if you have an input that asks for 6ints use this
#Alter for whatever type of input is required
for i in xrange(6):
    state.stack_push(state.se.BVS('int{}'.format(i), 4*8))

#Tell the Explorer which object to
    #-->start
    #-->finish
    #-->what to avoid
avoid = 0x40143a
path = proj.factory.path(state=state)
ex = proj.surveyors.Explorer(start=path, find=(0x400f3c,),
                             avoid=(bomb_explode,), enable_veritesting=True)

#Find what input generated said output
#Pop values off of the stack and ask the SMT solver to give us a valid integer solution for those values. 
if ex.found:
    found = ex.found[0].state

    answer = []

    for x in xrange(3):
        curr_int = found.se.any_int(found.stack_pop())

        # We are popping off 8 bytes at a time
        # 0x0000000200000001

        #converts 00003 --> 3
        answer.append(str(curr_int & 0xffffffff))
        #I think this zeros semething
        answer.append(str(curr_int>>32 & 0xffffffff))

    return ' '.join(answer)


#################FULL PROGRAM
## Binary found here: http://csapp.cs.cmu.edu/3e/bomb.tar

import angr, logging
from subprocess import Popen, PIPE
from itertools import product
import struct

def main():
    proj = angr.Project('bomb', load_options={'auto_load_libs':False})

    logging.basicConfig()
    logging.getLogger('angr.surveyors.explorer').setLevel(logging.DEBUG)

    def nop(state):
        return

    bomb_explode = 0x40143a

    # Start analysis at the phase_2 function after the sscanf
    state = proj.factory.blank_state(addr=0x400f0a)

    # Sscanf is looking for '%d %d %d %d %d %d' which ends up dropping 6 ints onto the stack
    # We will create 6 symbolic values onto the stack to mimic this
    for i in xrange(6):
        state.stack_push(state.se.BVS('int{}'.format(i), 4*8))

    # Attempt to find a path to the end of the phase_2 function while avoiding the bomb_explode
    path = proj.factory.path(state=state)
    ex = proj.surveyors.Explorer(start=path, find=(0x400f3c,),
                                 avoid=(bomb_explode, 0x400f10, 0x400f20,),
                                 enable_veritesting=True)
    ex.run()
    if ex.found:
        found = ex.found[0].state

        answer = []

        for x in xrange(3):
            curr_int = found.se.any_int(found.stack_pop())

            # We are popping off 8 bytes at a time
            # 0x0000000200000001

            # This is just one way to extract the individual numbers from this popped value
            answer.append(str(curr_int & 0xffffffff))
            answer.append(str(curr_int>>32 & 0xffffffff))

        return ' '.join(answer)

def test():
    assert main() == '1 2 4 8 16 32'

if __name__ == '__main__':
    print(main())

