

input = [0,14,6,20,1,4]

memory = dict((number,turn) for turn,number in enumerate(input,start=1))

turn = 7
nextNumber = 0

stopAt = 30000000 # 2020

while True:

    prevNumber = nextNumber

    nextNumber = turn - memory[prevNumber] if prevNumber in memory else 0 
   
    memory[prevNumber] = turn

    turn += 1

    if turn == stopAt:
        break

print(nextNumber)

# 8546398
