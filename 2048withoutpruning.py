from Moves import Grid
from Moves import ComputerAI

from Minimax import Minimax 
from tkinter import Tk, Label, Button
from colorama import Back

from Moves  import Displayer
from random       import randint
import time

defaultInitialTiles = 2
defaultProbability = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

timeLimit = 0.2
allowance = 0.05

class GameManager:
    def __init__(self, size = 4):
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4]
        self.probability = defaultProbability
        self.initTiles  = defaultInitialTiles
        self.computerAI = None
        self.Minimax   = None
        self.displayer  = None
        self.over       = False

    def setComputerAI(self, computerAI):
        self.computerAI = computerAI

    def setAlgo(self, Minimax):
        self.Minimax = Minimax

    def setDisplayer(self, displayer):
        self.displayer = displayer

    def updateAlarm(self, currTime):
        if currTime - self.prevTime > timeLimit + allowance:
            print("TIME RUN OUT")
            self.over = True
        else:
            while time.clock() - self.prevTime < timeLimit + allowance:
                pass

            self.prevTime = time.clock()

    def start(self):
        for i in range(self.initTiles):
            self.insertRandonTile()

        self.displayer.display(self.grid)

        turn = PLAYER_TURN
        maxTile = 0

        self.prevTime = time.clock()

        while not self.isGameOver() and not self.over:
            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print("Player's Turn:", end="")
                move = self.Minimax.getMove(gridCopy)
                print(Back.CYAN + actionDic[move])

                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        maxTile = self.grid.getMaxTile()
                    else:
                        print("Invalid PlayerAI Move")
                        self.over = True
                else:
                    print("Invalid PlayerAI Move - 1")
                    self.over = True
            else:
                print("Computer's turn:")
                move = self.computerAI.getMove(gridCopy)

                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer AI Move")
                    self.over = True

            if not self.over:
                self.displayer.display(self.grid)

            self.updateAlarm(time.clock())

            turn = 1 - turn
        print('High score: ',maxTile)
        self.Minimax._logger.info("Max Depth={}, Avg move time={}, Max Tile={}".format(self.Minimax._max_move_depth,self.Minimax._avg_move_time/self.Minimax._no_of_moves,maxTile))

    def isGameOver(self):
        return not self.grid.canMove()

    def getNewTileValue(self):
        if randint(0,99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1];

    def insertRandonTile(self):
        tileValue = self.getNewTileValue()
        cells = self.grid.getAvailableCells()
        cell = cells[randint(0, len(cells) - 1)]
        self.grid.setCellValue(cell, tileValue)

def main():
    gameManager = GameManager()
    minimax = Minimax()
    computerAI  = ComputerAI()
    displayer = Displayer()

    gameManager.setDisplayer(displayer)
    gameManager.setAlgo(minimax)
    gameManager.setComputerAI(computerAI)

    gameManager.start()

root = Tk()

label = Label(root, text= "Click the button to see the moves.")
label.pack()
button = Button(root, text="Print Me", command=main) 
button.pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()