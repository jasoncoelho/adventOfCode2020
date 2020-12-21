import os
import sys
import re

def isValid(min,max,character,password):
    count = password.count(character)
    valid = (count >= min) & (count <= max)
    print(str(min) + " " + str(max) + " " + character + " " + password + " " + str(valid))
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


