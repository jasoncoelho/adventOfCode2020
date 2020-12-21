import os
import sys
import re

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    group = []
    totalSum = 0

    for count, line in enumerate(reader, start=1):
    
        code = line.rstrip()
        
        if code != "":
            group += [code]
        else:
            print(group)
            totalYes = set()
            for count,g in enumerate(group):                
                if count == 0:
                    totalYes = set(g)
                else:
                    totalYes = totalYes & set(g)

            sum = len(totalYes)
            totalSum += sum

            print("sum:{}\ttotalSum:{}\t\tgroup:{}".format(sum,totalSum,sorted(totalYes)))
            print()
            group = []
            
    print(totalSum)

# Thoughts
# - dont forget the last batch
# - when initializing a first element from an array use enumerate and count instead
# - might be a better way to parse groups of lines from a file
# - can write a function that "yields" items 
        