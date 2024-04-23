from config import *

class Snake:


    def __init__(self):
        self.boardSetup()

    def takeTurn(self):
        direction = 0 # move right
        addX=1
        addY=0
        if direction==1:
            addX = -1 # move left
            addY = 0
        elif direction==2:
            addX = 0
            addY = 1 # move up
        else:
            addX = 0
            addY = -1 # move down
        self.board[self.x][self.y]=" "
        self.x+=addX
        self.y+=addY
        if self.board[self.y][self.x]=="#":
            self.alive=False
        self.board[self.x][self.y]="*"
        
        


    # clears board and prepares for playing
    def boardSetup(self):
        self.alive = True
        self.board = [[" " for x in range(BOARDSIZE_Y)] for x in range(BOARDSIZE_X)]

        # setting walls
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if y == 0 or y== len(self.board)-1 or x == 0 or x == len(self.board[x])-1:
                    self.board[y][x]="#"
        
        # setting player
        self.x = BOARDSIZE_X//2
        self.y = BOARDSIZE_Y//2
        self.board[self.x][self.y] = "*"
        self.board[self.x][self.y-10] = "^"


    def printBoard(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                print(self.board[y][x],end="")
                if x==len(self.board[y])-1:
                    print("")