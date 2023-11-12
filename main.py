import ast
import turtle

varInput = ''
verify = False
database = {}

def getAllRecords():
    global database
    with open('db.txt') as data:
        f = data.read()
        database = ast.literal_eval(f)

def getInput():
    global varInput
    varInput = 'Triangle' # input

def verifyShape(shape):
    global verify
    if shape in database.keys():
        print('Shape found')
        verify = True
        return verify
    else:
        print('Not found')
        verify = False
        return verify


def drawSquare():
    pass


def printShape(isTrue):
    global varInput
    if isTrue:
        if varInput == 'Triangle':
            drawTriangle()
        elif varInput == 'Square':
            drawSquare()
        elif varInput == 'Shape3':
            drawShape()
        else:
            print('Finish')
    else:
        print('Shape not found')

def drawShape():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(20)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

getAllRecords()
getInput()
def getShape(varInput):
       pass


shape_found = getShape(varInput)
printShape(shape_found)


def drawTriangle():
       for i in range(3):
           turtle.forward(100)
           turtle.left(120)
           turtle.color('white')
           turtle.bgcolor('pink')
           turtle.speed('10')
           turtle.Screen().exitonclick()



if __name__ == '__main__':
    verifyShape(varInput)