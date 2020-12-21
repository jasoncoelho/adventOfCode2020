
import os
import sys
import re
from collections import defaultdict

straightMap = defaultdict(dict)

def containsBag(listOfContainedBags,bagType):

    if len(listOfContainedBags) == 0:
        return False
    elif bagType in listOfContainedBags:
        return True
    else:
        for containedBag in listOfContainedBags:
            li = straightMap[containedBag]
            if containsBag(li,bagType):
                return True
        
    return False

def findIndividualBagsIn(bagType):

    count = 0 

    containedBags = straightMap[bagType]
    if (len(containedBags) > 0):        
        print("{}: {} - {}".format(len(containedBags),bagType,containedBags))

    for containedBag in containedBags:
        numberOfBags = int(containedBags[containedBag])
        individualBags = findIndividualBagsIn(containedBag)
        countBags = numberOfBags + (numberOfBags * individualBags)
        count += countBags
        print("{} of {} ({}) - {} - {}".format(numberOfBags,containedBag,individualBags,countBags,count))

    return count

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    group = ""
    totalSum = 0

    # reverseMap = {}
    reverseMap = defaultdict(list)

    # reverseMap.setdefault(bag,[])
    bagHolder = []

    for count, line in enumerate(reader, start=1):
        line = line.rstrip()
        parts = line.split(' contain ')
        
        pattern = r'(\d?)\s?([\w\s]+bag)\.{0,1}'

        m = re.search(pattern,parts[0])
        holdingBag = m.group(2)
        bags = parts[1].split(',')

        for bag in bags:

            bag = bag.lstrip()
           
            if "no other bags" in bag:      
                bag = "no other bags"
                reverseMap[bag] += [ holdingBag ]
                straightMap[holdingBag] = []
            else:
                m = re.search(pattern, bag)
                numberOfBags = m.group(1)
                bag = m.group(2)
                # if ('shiny gold bag' in bag):
                #     print(bag)
                reverseMap[bag] += [ holdingBag ]
                straightMap[holdingBag][bag] = numberOfBags

    for k in list(straightMap):
        listOfContainedBags = straightMap[k] 
        if containsBag(listOfContainedBags,"shiny gold bag"):
            totalSum += 1
            print("{} - {}".format(k,listOfContainedBags))
        
    # print("'{}' - {}".format(k,reverseMap[k]))

    print(totalSum)

    individualBagsInGold = findIndividualBagsIn("shiny gold bag")
    print(individualBagsInGold)