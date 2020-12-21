import os
import sys

def waitTimesAtTimestamp(buses,earliest_time):
    return [ (bus - (earliest_time % bus), bus) if bus != None else (None,None) for bus in buses ]

def evaluateWaitTimes(wait_times):

    # wait_times            [3,4,5,6,7,8,0,0,11]                      
    # signature to match    [0,1,2,3,4,5,0,0,8]
    
    start_wait,_ = wait_times[0] 

    return all( wait_time ==  index if bus != None else True 
    for index,(wait_time,bus) in enumerate(wait_times,start=start_wait) )

with (open(os.path.join(sys.path[0],'input.txt'),"r")) as file:
    
    lines = [ line.rstrip() for line in file.readlines() ]

    earliest_time       = int(lines[0]) 
    buses               = [ int(bus) if bus != 'x' else None for bus in lines[1].split(',')]
  
    valid_buses = [(bus, index) for index, bus in enumerate(buses) if bus != None]

    time, increment = 0, 1

    # i could not really solve this - and had to copy the following code from:
    #  https://gist.github.com/joshbduncan/65f810fe821c7a3ea81a1f5a444ea81e
    # it is an adaptation of the chinese remainder algorithm


    # iterate through buses (AND through time)
    for bus, index in valid_buses:
        # check to see if bus is departing at current time
        while True:
            if (index + time) % bus == 0:
                break # stop when we find a time where the bus stops
            else:
                time += increment
        # ok we found a bus for the current index, time to move to the next
        # increase the increment to find next min for next bus
        increment *= bus # notice we use a multiplier because we know the previous pattern will repeat

    print(f'Part 2: {time}')