import os
import sys
import re

def transformMemoryValueIntoPattern(memoryLocation,currentMask):

    binStr = str(bin(memoryLocation)).lstrip('0b').rjust(len(currentMask),'0')
    pattern = [ b for b in binStr ]

    for index,mask in enumerate(currentMask):
        pattern[index] = mask if mask in ['1','X'] else pattern[index]

    return pattern


def getFillValues(memoryPattern):
    numberofX = memoryPattern.count('X')
    intValue = int('1' *  numberofX,2)
    print ("int val = {}\t{}".format(intValue,numberofX))
    return (str(bin(a)).lstrip('0b').rjust(numberofX,'0') for a in range(0,intValue+1))
 

def getMemoryLocations(memoryLocation,mask):

    memoryPattern = transformMemoryValueIntoPattern(memoryLocation,mask)

    for fillValue in sorted(getFillValues(memoryPattern)):

        fillDigits = [ a for a in fillValue ]

        retValue = list(memoryPattern)
        counter = 0
        for index,re in enumerate(retValue):
            if 'X' in re:
                retValue[index] = fillDigits[counter]
                counter += 1

        return int("".join(retValue),2)


with (open(os.path.join(sys.path[0],'input.txt'),"r")) as file:

    lines = [ line.rstrip() for line in file.readlines() ]

    currentMask = []
    memory = {}

    for line in lines:
        if "mask" in line:
            currentMask = [m for m in line.split("=")[1].lstrip()]
        else:
            m = re.search('mem\[(\d+)\]\s=\s(\d+)', line)
            memoryLocation,memoryValue = (int(m.group(1)) , int(m.group(2)))

            for mem in getMemoryLocations(memoryLocation,currentMask):
                memory[mem] = memoryValue

    print(sum(memory.values()))

# 2205699916674
# 4355897790573

# thoughts
# use lstrip when removing the 0b or else strip by itself will cause errors