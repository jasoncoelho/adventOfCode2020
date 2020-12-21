
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


adjacentPositions = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1),
]


def getOccupiedSeats(position,seats):
    row,col = position

    adjacentSeatsStates = [ getCurrentState((row+aRow,col+aCol),seats) 
    for (aRow,aCol) in adjacentPositions ]

    occupiedSeats = [ seat for seat in adjacentSeatsStates if '#' in seat ]

    return occupiedSeats

   
def newState(position,seats):
    currentState = getCurrentState(position,seats)
    
    adjacentOccupiedSeats = len(getOccupiedSeats(position,seats))

    newState = currentState
    if '#' in currentState:
        newState = 'L' if adjacentOccupiedSeats >= 4 else '#'
    elif 'L' in currentState:
        newState = '#' if adjacentOccupiedSeats == 0 else 'L'
    
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
        if changed == 0:
            break
            
    occupiedCount = 0
    for s in seats:
        occupiedCount += len([d for d in s if d == '#'])

    print(occupiedCount)
    


