import os
import sys
import re

def isValid(pos1,pos2,character,password):
    pos1Char = password[pos1-1]
    pos2Char = password[pos2-1]
    valid = (pos1Char == character) != (pos2Char == character)
    print(str(pos1) + ":" + pos1Char  + "|" + str(pos2) + ":" + pos2Char + " " + character + " " + password + " " + str(valid))
    return valid


with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    targetValues = set()

    count = 0

    for line in reader:

        m = re.search(r'(\d+)-(\d+)\s(.):\s(.*)', line)

        valid = isValid(int(m.group(1)),int(m.group(2)),m.group(3),m.group(4))

        if valid:
            count += 1

    print(count)


