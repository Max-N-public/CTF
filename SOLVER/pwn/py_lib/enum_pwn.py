from subprocess import call



#run enumeration scripts on a pwn and output to screen
#add learning if/else struct to determine what the problem type is
def pwn_enumeration(filename):
    call('checksec filename')
    call('readelf -a filename')
    call('objdump -d filename')