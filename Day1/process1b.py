import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    combinationCount = 3

    # first initialize
    vals = []
    for line in reader:
        vals.append(int(line))

    vals.sort()

    # [ 1, 2, 4 , 5]
   
    pointer1 = 0    
    pointer2 = 1
    pointer3 = 2
    
    count = len(vals)
    combinationCount = 0

    while (pointer1 < count):    

        sum = vals[pointer1] + vals[pointer2] + vals[pointer3]

        print(str(pointer1) + "-" + str(pointer2) + "-" 
        + str(pointer3) + " : " + str(count) + " : " + str(sum))

        combinationCount += 1

        if (sum == 2020):
            print(vals[pointer1] * vals[pointer2] * vals[pointer3])
            break

        if pointer3 == count - 1:
            if pointer2 == count - 2:
                if pointer1 == count - 3:
                    break
                else:
                    pointer1 += 1
                    pointer2 = pointer1 + 1
                    pointer3 = pointer2 + 1
            else:
                pointer2 += 1
                pointer3 = pointer2 + 1
        else:
            if sum > 2020:
                pointer2 += 1
                pointer3 = pointer2 + 1
            else:
                pointer3 += 1
