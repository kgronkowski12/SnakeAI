from config import *
import random

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
        elif direction==3:
            addX = 0
            addY = -1 # move down

        # moving tail
        for tail_number in range(len(self.tail)):
            if tail_number==0:
                self.tail[0]=[self.y,self.x]
            else:
                self.tail[self.tail_number]=[self.tail[tail_number-1][0]  , self.tail[tail_number-1][1]]
                self.board[self.tail[tail_number-1][0]][self.tail[tail_number-1][1]]="@"


        self.x+=addX
        self.y+=addY
        if self.board[self.y][self.x]=="#":
            self.alive=False
        if self.board[self.y][self.x]=="^":
            self.points+=1
            if self.points==1:
                self.tail.append([self.y,self.x])
            else:
                self.tail.append([self.tail[len(self.tail)-1][0],self.tail[len(self.tail)-1][0]])
            
            # Terrible O(inf)!!!!
            while True:
                self.food_pos=[random.randint(0,BOARDSIZE_Y),random.randint(0,BOARDSIZE_X)]
                if self.board[self.food_pos[0]][self.food_pos[1]]==" ":
                    break

        self.drawObjects()
        
        


    # clears board and prepares for playing
    def boardSetup(self):
        self.points=0
        self.tail = []
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

        self.food_pos = [self.y, self.x + 10]
        self.drawObjects()


    def drawObjects(self):
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                self.board[y][x]=" "
                if y == 0 or y== len(self.board)-1 or x == 0 or x == len(self.board[x])-1:
                    self.board[y][x]="#"
        self.board[self.y][self.x]="*"
        for tail_part in self.tail:
            self.board[tail_part[0]][tail_part[1]]="@"
        self.board[self.food_pos[0]][self.food_pos[1]]="^"

    def printBoard(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                print(self.board[y][x],end="")
                if x==len(self.board[y])-1:
                    print("")