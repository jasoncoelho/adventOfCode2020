import os
import sys
import re

def findRange(upper,first,last):
    middle = round((first + last) / 2)
    if upper:
        return middle, last
    else:
        return first, middle-1 

def isUpperColCode(individualCode):
    return individualCode == 'R'

def isUpperRowCode(individualCode):
    return individualCode == 'B'

def calculateNumber(colCode,isLowerFunction,first,last):

    for index,individualCode in enumerate(colCode):
        if index < len(colCode)-1:
            first,last = findRange(isLowerFunction(individualCode),first,last)
   
    if isLowerFunction(individualCode):
        return last
    else:
        return first

def seatIdCalc(row,col):
    return row * 8 + col

def calculateSeatId(code):

    # BFBBBBBRLL
    row = calculateNumber(code[0:7],isUpperRowCode,0,127)
    col = calculateNumber(code[7:],isUpperColCode,0,7)
    seatId = seatIdCalc(row,col)
    return row,col,seatId

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    startColumn = 0

    passport = ""

    maxSeatId = 0

    validCount = 0 ;

    seats = {}
    seatIds = []

    for count, line in enumerate(reader, start=1):
    
        code = line.rstrip()

        # validate(code)

        row,col,seatId = calculateSeatId(code)

        if (seatId > maxSeatId):    
            maxSeatId = seatId 

        print("Code:{} SeatId:{} Row:{} Col:{}".format(code,seatId,row,col))
        print("Max Seat Id:{}".format(maxSeatId))

        if row in seats:
            seats[row].append(col)
        else:
            seats[row] = [col]

        seatIds.append(seatId)


    for key,val in seats.items():
        if (len(val) != 8):
            val.sort()
            emptySeatCols = [x for x in range(0,7) if x not in val]
            for emptySeatCol in emptySeatCols:
                emptySeatId = seatIdCalc(key,emptySeatCol)
                print("row:{} col:{} seats:{} seatId:{}".format(key,emptySeatCol,val,emptySeatId))
                if (emptySeatId+1) in seatIds and (emptySeatId-1) in seatIds:
                    print("your seat id is {}".format(emptySeatId))
