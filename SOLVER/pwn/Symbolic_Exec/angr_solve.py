import angr, claripy

find_address = "<address to jump to>"
binary_name = "<name of binary>"


proj = angr.Project(binary_name)

arg1 = claripy.BVS('arg1', 20*8)
initial_state = proj.factory.entry_state(args=["high_quality_checks", arg1])

simgr = proj.factory.simulation_manager(initial_state)

simgr.explore(find=find_address, avoid=[])

print(simgr.found[0].posix.dumps(0))