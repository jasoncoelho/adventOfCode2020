
import os
import sys
import queue


with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    adapters = []

    for count, line in enumerate(reader, start=1):
        adapters.append(int(line.rstrip()))

    adapters.sort()

    sum_ones = 0
    sum_threes = 0

    prev_adapter = 0
    for adapter in adapters:
        if adapter-prev_adapter <= 3:
            adapter_diff = adapter - prev_adapter
            print("adapter:{} diff:{} prev:{}"
            .format(adapter,adapter_diff,prev_adapter))
            prev_adapter = adapter
            if adapter_diff == 1:
                sum_ones += 1
            elif adapter_diff == 3:
                sum_threes += 1
    
    solution = sum_ones * (sum_threes + 1)

    print("ones:{} threes:{} solution:{}".format(sum_ones,sum_threes,solution))

    memo = dict()

    def findCandidates(index,prevAdapter):

        key = str(index) + "-" + str(prevAdapter)
        if key in memo:
            return memo.get(key)

        ret = []
        stop = index+5
        subset = adapters[index:index+5]
        # print(subset)
        for index,val in enumerate(subset,start=index):
            if val - prevAdapter <= 3:
                ret.append((index,val)) 

        memo[key] = ret
        
        return ret

    memo2 = dict()

    def helper(index,prevAdapter):

        #  memo-ize , makes a huge differnece in run speed
        key = str(index) + "-" + str(prevAdapter)
        if key in memo2:
            return memo2.get(key)

        s = 0

        #  return 1 if we successully reach the end
        if index == len(adapters):
           return 1 

        for candidateIndex,candidate in findCandidates(index,prevAdapter):
            s += helper(candidateIndex + 1,candidate)

        memo2[key] = s

        return s

    combinations = helper(0,0)
    print(combinations) # 9256148959232
#  1,2,3,4

# 1,2,3





