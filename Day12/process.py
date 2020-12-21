
import os
import sys

directionChange = ['R','L']
degree180 = {
    'N' : 'S',
    'S' : 'N',
    'E' : 'W',
    'W' : 'E'
}

degreeL270 = degreeR90 = {
    'N' : 'E',
    'S' : 'W',
    'E' : 'S',
    'W' : 'N'
}

degreeR270 = degreeL90 = {
    'N' : 'W',
    'S' : 'E',
    'E' : 'N',
    'W' : 'S'
}

directionalMoves = {
    'E' : (1,0),
    'W' : (-1,0),
    'N' : (0,1),
    'S' : (0,-1)
}

def moveShip(shipDirection,shipPosition,move):

    direction, moveValue = move

    if direction in directionChange:
        if moveValue == 180:
            shipDirection = degree180[shipDirection]
        elif moveValue == 270:
            shipDirection = degreeL270[shipDirection] if direction == 'L' else degreeR270[shipDirection]
        elif moveValue == 90:
            shipDirection = degreeL90[shipDirection] if direction == 'L' else degreeR90[shipDirection]
        return (shipDirection,shipPosition)

    x,y = shipPosition
    
    moveDirection = shipDirection if direction == 'F' else direction
    moveX, moveY = directionalMoves[moveDirection]
    
    shipPosition = (x+(moveX*moveValue),y+(moveY*moveValue))

    return (shipDirection,shipPosition)
    

def calculateDistance(startPosition,shipPosition):

    x,y = startPosition
    endX,endY = shipPosition

    return abs(endX) + abs(endY)


with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    lines = [ line.rstrip() for line in reader.readlines() ]

    moves = [ (line[0:1],int(line[1:])) for line in lines]

    shipPosition =  (0,0)
    shipDirection = 'E'

    for move in moves:
        # print("Moving ship {},{}\tto {}".format(shipDirection,shipPosition,move))
        (shipDirection,shipPosition) = moveShip(shipDirection,shipPosition,move)

    # (shipDirection,shipPosition) = moveShip(shipDirection,startPosition,('W',90))
    print("direction:{} position:{}".format(shipDirection,shipPosition))

    distance = calculateDistance((0,0),shipPosition)

    print(distance)
