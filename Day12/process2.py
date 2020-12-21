
import os
import sys
import math

directionalMoves = {
    'E' : (1,0),
    'W' : (-1,0),
    'N' : (0,1),
    'S' : (0,-1)
}
    
def moveShip(shipPosition,wayPointPosition,units):

    wX,wY = wayPointPosition
    x,y = shipPosition
    mX,mY = wX * units, wY * units
    return (x + mX, y + mY)


def rotatePoint(point,angle):
    wX,wY = point
    r = math.radians(angle)

    x = round(wX * math.cos(r) - wY * math.sin(r))
    y = round(wX * math.sin(r) + wY * math.cos(r))

    return x,y


def moveWayPoint(wayPointPosition,move):

    wX,wY = wayPointPosition

    direction,moveUnits = move

    mX,mY = directionalMoves[direction]

    return wX + (moveUnits * mX), wY + (moveUnits * mY) 
         

def calculateDistance(startPosition,shipPosition):

    x,y = startPosition
    endX,endY = shipPosition

    return abs(endX) + abs(endY)


with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    lines = [ line.rstrip() for line in reader.readlines() ]

    moves = [ (line[0:1],int(line[1:])) for line in lines]

    shipPosition =  (0,0)
    wayPointPosition = (10,1)

    print("position:{} wayPointPosition:{}".format(shipPosition,wayPointPosition))

    for move in moves:
        direction,units = move

        if direction == 'F':
            shipPosition = moveShip(shipPosition,wayPointPosition,units)
          
        elif direction in ['L','R']:

            if direction == 'R':
                units = 360 - units
           
            wayPointPosition = rotatePoint(wayPointPosition,units)
              
        elif direction in ['N','E','W','S']:
            wayPointPosition = moveWayPoint(wayPointPosition,move)
          
        print("position:{} wayPointPosition:{} move:{}"
            .format(shipPosition,wayPointPosition,move))

    distance = calculateDistance((0,0),shipPosition)

    print(distance)


    #  thoughts
    #  - made a mistake rotating the waypoint. the angle to the formula moves counter-clockwise rather than clock-wise
