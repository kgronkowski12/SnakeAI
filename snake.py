from config import *
from brain import *
import random
import statistics

class Snake:


    def __init__(self):
        self.prevdir=5
        self.brain = Brain()
        self.brain.randomize_weights()
        self.boardSetup()
    
    def get_brain(self):
        return self.brain

    # Look in a direction, pass seen obstacle and distance to it to a brain function
    def look(self, start_x, start_y, x, y, add_dist):
        dist = 1
        looking_for = ["#","@","^"]
        while self.board[start_y+y][start_x+x] not in looking_for:
            start_x+=x
            start_y+=y
            dist+=1
        return self.brain.get_output(self.board[start_y+y][start_x+x],dist+add_dist)

    # Look in every direction
    def ultra_look(self,x,y):
        dist = 1
        looking_for = ["#","@","^"]
        start_x = self.x
        start_y = self.y
        outputs = []
        while self.board[start_y+y][start_x+x] not in looking_for:
            start_x+=x
            start_y+=y
            dist+=1
            outputs.append(self.look(start_x,start_y,-1,0,dist))
            outputs.append(self.look(start_x,start_y,1,0,dist))
            outputs.append(self.look(start_x,start_y,0,-1,dist))
            outputs.append(self.look(start_x,start_y,0,1,dist))
        outputs.append(self.brain.get_output(self.board[start_y+y][start_x+x],dist))
        return max(outputs)

    # Place food on board
    def placeFood(self):
        while True:
            pos=[random.randint(0,BOARDSIZE_Y-1),random.randint(0,BOARDSIZE_X-1)]
            if self.board[pos[0]][pos[1]]==" ":
                self.food_pos.append(pos)
                break

    def takeTurn(self):
        # Get output values
        right_out = self.ultra_look(1,0)
        left_out = self.ultra_look(-1,0)
        down_out = self.ultra_look(0,-1)
        up_out = self.ultra_look(0,1)

        # Add stubborness value to previous direction
        if self.prevdir==0:
            right_out+=self.same_dir_add+1
        elif self.prevdir==1:
            left_out+=self.same_dir_add+1
        elif self.prevdir==2:
            up_out+=self.same_dir_add+1
        elif self.prevdir==3:
            down_out+=self.same_dir_add+1

        # Add widzimisie value to randomly chosen direction
        if self.widzimisie_dir==0:
            right_out+=self.widzimisie
        elif self.widzimisie_dir==1:
            left_out+=self.widzimisie
        elif self.widzimisie_dir==2:
            up_out+=self.widzimisie
        elif self.widzimisie_dir==3:
            down_out+=self.widzimisie

        # Can't turn 180 degrees
        if self.prevdir!=1:
            addX=1
            addY=0
            current_max = right_out
            # move right by default
        else:
            addX=-1
            addY=0
            current_max = left_out

        # Looks witch output value is the biggest
        # Changes direction based on it.
        if left_out>current_max:
            self.prevdir=1
            current_max=left_out
            addX = -1 # move left
            addY = 0
        if up_out>current_max:
            self.prevdir=2
            current_max=up_out
            addX = 0
            addY = 1 # move up
        if down_out>current_max:
            self.prevdir=3
            current_max=down_out
            addX = 0
            addY = -1 # move down
        if addX==1 and addY==0:
            self.prevdir=0

        if len(self.tail)>0:
            last_tail = [self.tail[len(self.tail)-1][0], self.tail[len(self.tail)-1][1]]
        else:
            last_tail = [self.y,self.x]

        # Moving tail
        for tail_number in range(len(self.tail)):
            if tail_number==0:
                self.tail[0]=[self.y,self.x]
            else:
                self.tail[len(self.tail)-tail_number]=[self.tail[len(self.tail)-tail_number-1][0]  , self.tail[len(self.tail)-tail_number - 1][1]]

        # If eaten food previous turn, add a new tail piece
        if self.addTail:
            self.tail.append(last_tail)
            self.addTail=False

        # Change position
        self.x+=addX
        self.y+=addY
        if self.board[self.y][self.x]=="#": # Hit wall
            self.alive=False
        if self.board[self.y][self.x]=="@": # Hit tail
            self.alive=False
        if self.board[self.y][self.x]=="^": # Eaten food
            self.points+=1
            self.addTail = True
            
            self.placeFood()
            self.food_pos.remove([self.y,self.x])
            self.hunger=0

        self.drawObjects()
        self.hunger+=1
        if self.hunger>= MAX_HUNGER:
            self.alive=False
        self.step_count+=1
        # Change widzimisie direction
        if self.step_count>self.widzimisie_timer:
            self.step_count=0
            self.widzimisie_dir = random.randint(0,4)
        


    # clears board and prepares for playing
    def boardSetup(self):
        self.widzimisie_timer = sum(self.brain.hidden_layer["widzimisie_timer"])
        self.widzimisie = abs(sum(self.brain.hidden_layer["widzimisie"]))
        self.same_dir_add = abs(sum(self.brain.hidden_layer["stubborn"]))

        self.widzimisie_dir = random.randint(0,4)
        self.step_count=0
        self.prevdir=5
        self.points=0
        self.hunger=0
        self.tail = []
        self.addTail=False
        self.food_pos = []
        self.alive = True
        self.board = [[" " for x in range(BOARDSIZE_X)] for y in range(BOARDSIZE_Y)]

        # setting walls
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if y == 0 or y== len(self.board)-1 or x == 0 or x == len(self.board[y])-1:
                    self.board[y][x]="#"
        
        # setting player
        self.x = BOARDSIZE_X//2
        self.y = BOARDSIZE_Y//2

        for food in range(FOOD_COUNT):
            self.placeFood()
        self.drawObjects()

    # Sets up text board
    def drawObjects(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                self.board[y][x]=" "
                if y == 0 or y== len(self.board)-1 or x == 0 or x == len(self.board[x])-1:
                    self.board[y][x]="#"
        self.board[self.y][self.x]="*"
        for tail_part in self.tail:
            self.board[tail_part[0]][tail_part[1]]="@"
        for food in self.food_pos:
            self.board[food[0]][food[1]]="^"

    # Prints text board
    def printBoard(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                print(self.board[y][x],end="")
                if x==len(self.board[y])-1:
                    print("")