import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    targetValues = set()

    for line in reader:

        diffValue = 2020-int(line) # what we are looking for

        if int(line) in targetValues:   # have we seen the inverse before
            returnVal = int(line) * diffValue
            print(str(returnVal))
            exit
        else:
            targetValues.add(diffValue)
