import taffyTangle_logic
import taffyTangle_draw
import stddraw

def lmao():
    stddraw.clear()
    taffyTangle_draw.drawCanvas()
    taffyTangle_draw.showPlayerScore(taffyTangle_logic.SCORE)
    stddraw.show(100)

turn = 0
selection = 0
click = 0
taffyTangle_logic.fixMatrix()
taffyTangle_draw.setScales()
while True:
    if taffyTangle_logic.SCORE < 100 and taffyTangle_logic.MOVES < 25:
        if turn == 0:
            taffyTangle_draw.instructions()
            stddraw.show(1250)
            turn = 1
        taffyTangle_draw.clear()
        taffyTangle_draw.drawCanvas()
        taffyTangle_draw.showPlayerScore(taffyTangle_logic.SCORE)
        if stddraw.mousePressed():
            x = int(stddraw.mouseX())
            y = int(stddraw.mouseY())
            click += 1
        if click % 2 != 0 and click > 0:
            selection = 0
            taffyTangle_draw.selection(x,y,selection)
        elif click > 0:
            selection = 1
            if taffyTangle_logic.checkIfClickAdjacent(taffyTangle_draw.X,taffyTangle_draw.Y,x,y):
                taffyTangle_draw.selection(x,y,selection)
                taffyTangle_logic.swap(8-taffyTangle_draw.Y,taffyTangle_draw.X,8-y,x)
                lmao()
                if taffyTangle_logic.checkIfThree() == False:
                        taffyTangle_logic.swap(8-y,x,8-taffyTangle_draw.Y,taffyTangle_draw.X)
                        lmao()
                else:
                    taffyTangle_logic.MOVES += 1
                    while taffyTangle_logic.checkIfThree():
                        taffyTangle_logic.similar()
                        lmao()
                        while taffyTangle_logic.check1s():
                            taffyTangle_logic.fillMatrix()
                            lmao()
                            taffyTangle_logic.fillRow0()
                            lmao()
                        taffyTangle_logic.fillRow0()
                        lmao()
                click = 0
            else:
                click = 0
                selection = 0
        stddraw.show(100)
    else:
        if taffyTangle_logic.SCORE >= 100:
            taffyTangle_draw.win()
        else:
            taffyTangle_draw.lose()

