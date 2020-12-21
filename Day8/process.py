
import os
import sys

def isInfiniteLoop(operationBuffer,line):
    
    pastJumps = []
    accSum = 0
    line = 0
    while line < len(operationBuffer):

        (op,val) = operationBuffer[line]

        print("{}: {} {}".format(line,op,val))

        if 'acc' in op:
            accSum += val
            line += 1
        elif 'jmp' in op:
            if val != 0:
                line += val
            if line in pastJumps:
                print("jumping to point already seen: {}".format(line))
                return (True,accSum)
                break
            else:
                pastJumps += [ line ]
        elif 'nop' in op:
            line += 1

    return (False,accSum)

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    operationBuffer = []

    for count, line in enumerate(reader, start=1):
                
        line = line.rstrip()

        operations = line.split()
        operation = operations[0]
        operationSum = int(operations[1])

        operationBuffer += [(operation,operationSum)]
        
    infiniteLoop,acc = isInfiniteLoop(list(operationBuffer),0)

    print("InfinteLoop:{} Sum: {}".format(infiniteLoop,acc))

    for index,op in enumerate(operationBuffer):
        if 'jmp' in op[0] or 'nop' in op[0]:
            print("{} {}".format(op[0],index))
            copied = operationBuffer.copy()
            copied[index] = ('nop' if 'jmp' in op[0] else 'nop',op[1])
            infiniteLoop,acc = isInfiniteLoop(copied,0)
            if infiniteLoop == False:
                print("broken at {}".format(acc))
                break

       
