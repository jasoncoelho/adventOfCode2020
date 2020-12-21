import os
import sys

def waitTimesAtTimestamp(buses,earliest_time):
    return [ (bus - (earliest_time % bus), bus) for bus in buses ]


with (open(os.path.join(sys.path[0],'input.txt'),"r")) as file:
    
    lines = [ line.rstrip() for line in file.readlines() ]

    earliest_time       = int(lines[0]) 
    operating_buses     = [int(bus) for bus in lines[1].split(',') if bus != 'x']

    print((earliest_time, operating_buses))

    # 1006401 / 10 = 1006400 , rem:1; wait: 9 (10-remainder)
    # getMin(wait_times)

    # tuple (wait_time -> bus)
    wait_times = waitTimesAtTimestamp(operating_buses,earliest_time)

    (min_wait,min_wait_bus) = min(wait_times)

    print(wait_times)

    print((min_wait,min_wait_bus))
    print ("min wait time solution : {}".format(min_wait * min_wait_bus))