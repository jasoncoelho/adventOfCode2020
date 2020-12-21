
import os
import sys
import queue


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

rowLen = 0
colLen = 0

def getCurrentState(position,seats):
    row,col = position
    if (row < 0 or col < 0 or row > rowLen-1 or col > colLen-1):
        return ''
    return seats[row][col]


directions = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1),
]


def getVisiblyOccupiedSeats(position,seats):
    row,col = position

    visiblyOccupiedSeats = 0

    for (dRow,dCol) in directions:
        aRow, aCol = row, col
        while True:
            aRow += dRow
            aCol += dCol
            seatStateAtDirection = getCurrentState((aRow,aCol),seats)
            if '#' in seatStateAtDirection:
                visiblyOccupiedSeats += 1
                break
            elif seatStateAtDirection == '' or 'L' in seatStateAtDirection:
                break

    # print("checking for visibly occupied seat at {} is {}"
    # .format((row,col),visiblyOccupiedSeats))

    # print("visibly occupied seats for {} is {}".format(position,visiblyOccupiedSeats))
    return visiblyOccupiedSeats


def newState(position,seats):
    currentState = getCurrentState(position,seats)
    
    visiblyOccupiedSeats = getVisiblyOccupiedSeats(position,seats)

    newState = currentState
    if '#' in currentState:
        newState = 'L' if visiblyOccupiedSeats >= 5 else '#'
    elif 'L' in currentState:
        newState = '#' if visiblyOccupiedSeats == 0 else 'L'
    
    return (newState,newState != currentState)


def findNewState(seats):

    newSeats = []

    changed = 0

    row = 0
    for rowArr in seats:
        newRow = []
        col = 0
        for seat in rowArr:
            newSeat,newSeatChanged = newState((row,col),seats)
            changed += 1 if newSeatChanged else 0
            newRow += newSeat
            col += 1
        row += 1
        newSeats += [newRow]

    return (newSeats,changed)

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    seats = [ [c for c in line.rstrip()] for line in reader.readlines() ]

    rowLen = len(seats)
    colLen = len(seats[0])

    changedCount = 0
    while True:
        seats, changed = findNewState(seats)
        print("changed seats {}".format(changed))
        if changed == 0:
            break
            
    occupiedCount = 0
    for s in seats:
        occupiedCount += len([d for d in s if d == '#'])

    print(occupiedCount)
    


