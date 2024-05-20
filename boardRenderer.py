import pygame
from tile import *
from config import *
from textHolder import *

# Class resposible for rendering the board state to screen.
class BoardRenderer():
    def __init__(self,ALL_SPRITES):

        # Create a 2D array of tiles (sprites), which create the board
        self.board = [[Tile((50+x*10,50+y*10)) for x in range(BOARDSIZE_X)] for y in range(BOARDSIZE_Y)]
        for row in self.board:
            for tile in row:
                ALL_SPRITES.add(tile)

        
        # Initialize text with info about board
        self.gen_number = TextHolder((50,BOARDSIZE_Y*10+75))
        ALL_TEXT.append(self.gen_number)

        self.alive_snakes = TextHolder((50,BOARDSIZE_Y*10+100))
        ALL_TEXT.append(self.alive_snakes)

        self.best = TextHolder((50,BOARDSIZE_Y*10+125))
        ALL_TEXT.append(self.best)

        self.mean = TextHolder((50,BOARDSIZE_Y*10+150))
        ALL_TEXT.append(self.mean)

        self.median = TextHolder((50,BOARDSIZE_Y*10+175))
        ALL_TEXT.append(self.median)

        self.deviation = TextHolder((50,BOARDSIZE_Y*10+200))
        ALL_TEXT.append(self.deviation)

        self.watching = TextHolder((50,BOARDSIZE_Y*10+225))
        ALL_TEXT.append(self.watching)

        previous_gens = TextHolder((BOARDSIZE_X*10+75,50))
        previous_gens.changeText("Previous generations:")
        ALL_TEXT.append(previous_gens)
        
        self.prev_gen = []
        for x in range(10):
            gen = TextHolder((BOARDSIZE_X*10+75,75+25*x))
            gen.changeText("-")
            ALL_TEXT.append(gen)
            self.prev_gen.append(gen)


    # Changes the color of every tile in the board to match given board in text form
    def render(self, text_board, alive):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if text_board[y][x]=="#":
                    self.board[y][x].change_color(WALL_COLOR)
                if text_board[y][x]==" ":
                    self.board[y][x].change_color(EMPTY_COLOR)
                if text_board[y][x]=="^":
                    self.board[y][x].change_color(FOOD_COLOR)
                if text_board[y][x] in ["@","*"]:
                    if alive:
                        self.board[y][x].change_color(TAIL_COLOR)
                    else:
                        self.board[y][x].change_color(DEAD_COLOR)


                