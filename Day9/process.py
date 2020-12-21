import os
import sys
import queue

PREAMBLE_SIZE = 25

failed_value = 0

def bufferHas2Sum(buffer,sumTarget):

    inverse = []

    for val in buffer:
        inverse.append(sumTarget - val)

    for val in buffer:
        if val in inverse:
            return True
        
    return False
    
with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    buffer = queue.Queue(PREAMBLE_SIZE)

    for count, line in enumerate(reader, start=1):

        val = int(line.rstrip())

        print(val)

        if (buffer.qsize() == PREAMBLE_SIZE):
            if bufferHas2Sum(list(buffer.queue),val):
                buffer.get()
            else:
                failed_value = val
                print("failed value: {}".format(failed_value))
                break

        buffer.put(val)

    reader.seek(0)

    startAt = 1
    currentSum = 0
    found = False
    while not found:
        sumList = []

        counter = 0

        # print("starting at {}".format(startAt))

        for count, line in enumerate(reader):
            
            counter += 1
            if counter < startAt:
                continue

            # print("{} rrr".format(line.rstrip()))
            val = int(line.rstrip())
            currentSum += val

            sumList.append(val)

            if (currentSum == failed_value):

                print(sumList)
                sumList.sort()
                minValue,maxValue = min(sumList), max(sumList)
                print("found list {} with Sum:{} with min:{} and max:{} and minMaxSum:{}"
                .format(sumList,currentSum,minValue,maxValue, minValue+maxValue))

                found = True
                break
            elif (currentSum > failed_value):
    
                # print("failed current sum:{} target sum:{} seeking to {}"
                # .format(currentSum,failed_value,startAt))
                reader.seek(0)
                startAt += 1
                sumList = []
                currentSum = 0
                counter = 0
                break;
