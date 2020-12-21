import os
import sys
import re

lineCount = 0

def treeInRow(startColumn,step,line):

    endColumn = startColumn + step
    # (30+3 = 33); 33 - 30 = 3
    # (29+3 = 32); 32 - 30 = 2
    # (32+3 = 42); 42 - 30 = 3
    overshoot = endColumn - (len(line) - 1)

    if (overshoot == 0):
        sub = line[startColumn:]
    elif (overshoot > 0):
        sub = line[startColumn:] + line[0:overshoot]
        endColumn = overshoot - 1
    else:
        sub = line[startColumn:endColumn+1]

    # print(sub)
    # if (overshoot >= 0):
    #     print(" overshoot:" + str(overshoot) + " startCol:" + str(startColumn) 
    #     + " endCol:" + str(endColumn) 
    #     + " len:" + str(len(line)))

    return sub[0:1].count('#') , endColumn

def getCount(colStep,rowStep):

    treeCount = 0

    with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

        startColumn = 0
    
        for count, line in enumerate(reader, start=1):
        
            # if (lineCount == 40):
            #     break

            if (count == 1 or (count+1) % rowStep == 0):
                # Note: strip newline or else the len of line will include it
                count , startColumn =  treeInRow(startColumn,colStep,line.rstrip()) 
                treeCount += count

            # print(line + "sum:" + str(treeCount) + " column:" + str(startColumn))
        
    return treeCount


sum1 = getCount(1,1)
sum3 = getCount(3,1)
sum5 = getCount(5,1)
sum7 = getCount(7,1)
sum12 = getCount(1,2)

print(str(sum1) + "::" + str(sum3) + "::" + str(sum5) 
+ "::" + str(sum7) + "::" + str(sum12))

print(str(sum1*sum3*sum5*sum7*sum12))

            # 3 = 223
            # 1 = 58
            # 5 = 105
            # 7 = 74

# Thoughts :
# - Read Problem !!! only count tree on the last spot NOT ALL Trees in a step
# - Break down problem and naming all variables will ease solution
# - smaller functions
# - cleaner print statements will help to debug
