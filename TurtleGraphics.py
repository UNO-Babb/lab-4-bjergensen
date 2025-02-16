#TurtleGraphics.py
#Name:Brandon Jergensen
#Date:2/16/25
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360 / sides)
        
def fillCorner(myTurtle, corner):
    #draw big square
    if corner == 1:
        drawSquare(myTurtle, 100)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 2:
        drawSquare(myTurtle, 100)
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 3:
        drawSquare(myTurtle, 100)
        myTurtle.penup()
        myTurtle.goto(50, -50)
        myTurtle.pendown()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 4:
        drawSquare(myTurtle, 100)
        myTurtle.goto(0, -50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
def squaresInSquares(myTurtle, num):
    for size in range(num):
        drawSquare(myTurtle, num*10)
        myTurtle.penup()
        myTurtle.forward(5)
        myTurtle.right(90)
        myTurtle.forward(5)
        myTurtle.left(90)
        myTurtle.pendown()
        num -= 1
    
    

def main():
    bob = turtle.Turtle()
    #drawSquare(bob, 100)
    #drawPolygon(bob, 5) #draws a pentagon
    #drawPolygon(bob, 8) #draws an octogon

    # fillCorner(bob, 4) #draws a square with top right corner filled in.
    # fillCorner(bob, 3) #draws a square bottom left corner filled in.

    squaresInSquares(bob, 5) #draws 5 concentric squares
     #squaresInSquares(bob, 3) #draws 3 concentric squares


main()
