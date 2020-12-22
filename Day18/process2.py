import os
import sys

def solveExpression(expression):

    answer = None

    digitBuffer = ''
    operationBuffer = None
    currentIndex = 0

    multiplicationBuffer = []

    while currentIndex < len(expression):
        
        char = expression[currentIndex]

        if char in ['+','*',')']:
            
            if operationBuffer:
               
                if operationBuffer == '*':
                    multiplicationBuffer += [ answer ]
                    answer = int(digitBuffer)
                else:
                    answer += int(digitBuffer)
            else:
                answer = int(digitBuffer)
            
            digitBuffer = ''
            operationBuffer = char
        
            if char == ')':
                for val in multiplicationBuffer:
                    answer *= val
                return answer,currentIndex

        elif char == '(':

            remainderOfExpression = expression[currentIndex+1:]
            expressionAnswer , endPoint = solveExpression(remainderOfExpression)

            digitBuffer = expressionAnswer
            currentIndex += endPoint + 1
        else:
            digitBuffer += char

        currentIndex += 1

    if operationBuffer == '+':
        answer += int(digitBuffer)
    else:
        multiplicationBuffer += [ int(digitBuffer) ]

    for val in multiplicationBuffer:
        answer *= val
   
    return answer,currentIndex


with open(os.path.join(sys.path[0],"input.txt")) as read:

    expressions = [ line.strip().replace(" ","") for line in read.readlines() ]

    cumulative = 0

    for expression in expressions:

        answer,_ = solveExpression(expression) # 13
        print(f"answer:{answer}\t\t\texpression:{expression}")
        cumulative += answer

    print(f"cumulative: {cumulative}")