import os
import sys
import re

def getCounts(group):
    sum = len(list(dict.fromkeys(group)))
    print("sum:{} \t\tgroup:{}".format(sum,group))
    return sum

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    group = ""
    totalSum = 0

    for count, line in enumerate(reader, start=1):
    
        code = line.rstrip()

        if code != "":
            group += code
        else:
            sum = getCounts(group)
            totalSum += sum
            group = ""

    print(totalSum)

# Thoughts
# - dont forget the last batch
        