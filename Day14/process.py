import os
import sys
import re

def transformMemoryValue(memoryValue,currentMask):

    binStr = str(bin(memoryValue)).lstrip('0b').rjust(len(currentMask),'0')
    binValue =[ b for b in binStr ]

    print("currenMask:\t{}\nvalue:\t\t{}\t{}"
    .format("".join(currentMask),"".join(binValue),memoryValue))
    
    for index,mask in enumerate(currentMask):
        if 'X' not in mask:
            binValue[index] = '1' if '1' in mask else '0'

    intvalue = int("".join(binValue),2)

    print("trans value:\t{}\t{}\n".format("".join(binValue),intvalue))

    return intvalue


with (open(os.path.join(sys.path[0],'input.txt'),"r")) as file:

    lines = [ line.rstrip() for line in file.readlines() ]

    currentMask = []
    memory = {}

    for line in lines:
        if "mask" in line:
            currentMask = [m for m in line.split("=")[1].lstrip()]
        else:
            m = re.search('mem\[(\d+)\]\s=\s(\d+)', line)
            memoryLocation,memoryValue = (m.group(1) , int(m.group(2)))
            memory[memoryLocation] = transformMemoryValue(memoryValue,currentMask)

    print(sum(memory.values()))
