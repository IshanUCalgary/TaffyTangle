import stddraw
import math
import taffyTangle_logic
import color

X = 0
Y = 0

def setScales():
    stddraw.setXscale(0,7)
    stddraw.setYscale(0,9.5)

def clear():
    stddraw.clear()

def show(milliseconds = -1.0):
    if milliseconds < 0:
        stddraw.show()
    else:
        stddraw.show(milliseconds)

def drawCanvas():
    for everyRow in range(len(taffyTangle_logic.MATRIX)):
        for everyColumn in range(len(taffyTangle_logic.MATRIX[everyRow])):
            drawShapes(taffyTangle_logic.MATRIX[8-everyRow][everyColumn],everyColumn+0.5,everyRow+0.5)

def redBox(x,y):
    if y <= 9:
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.RED)
        stddraw.square(x+0.5,y+0.5,0.5)

def selection(x,y,selection):
    if y <= 8:
        if selection == 0:
            global X, Y
            X = x
            Y = y
            redBox(x,y)
        if selection == 1:
            redBox(X,Y)
            redBox(x,y)

def drawShapes(number,x,y):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.01)
    if number == 0:
        stddraw.square(x,y,0.4)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledSquare(x,y,0.4)
    if number == 1:
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(x,y,0.4)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(0.004)
        stddraw.circle(x,y,0.4)
    if number == 2:
        xs = [x-0.4,x+0.4,x]
        ys = [y-0.4,y-0.4,y+0.4]
        stddraw.polygon(xs,ys)
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledPolygon(xs,ys)
    if number == 3:
        xs = [x-0.4,x,x+0.4,x]
        ys = [y,y+0.4,y,y-0.4]
        stddraw.polygon(xs,ys)
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledPolygon(xs,ys)
    if number == 4:
        xs = [x-0.4,x-0.2,x+0.2,x+0.4,x]
        ys = [y,y+0.4,y+0.4,y,y-0.4]
        stddraw.polygon(xs,ys)
        stddraw.setPenColor(stddraw.MAGENTA)
        stddraw.filledPolygon(xs,ys)
    if number == 5:
        xs = [x-0.4,x-0.2,x+0.4,x+0.2]
        ys = [y-0.4,y+0.4,y+0.4,y-0.4]
        stddraw.polygon(xs,ys)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledPolygon(xs,ys)

def showPlayerScore(score):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(1,9.25,'Player Score: ' + str(score))
    stddraw.text(4,9.25,'Moves: ' + str(taffyTangle_logic.MOVES))
    stddraw.line(0,9.0,7.0,9.0)

def win():
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(50)
    stddraw.text(3.5,4.5,'You Won!')
    stddraw.show()

def instructions():
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(30)
    stddraw.text(3.5,7,"To Win This Game All You Have To Do")
    stddraw.text(3.5,6,"Is Get Your Score Over 100 in under 25 Moves.")
    stddraw.text(3.5,5,"That's It!. Good Luck!")

def lose():
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(50)
    stddraw.text(3.5,4.5,'You Lost!')
    stddraw.show()
