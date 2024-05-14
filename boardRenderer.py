import pygame
from tile import *
from config import *

class BoardRenderer():
    def __init__(self,ALL_SPRITES):
        self.board = [[Tile((100+x*10,100+y*10)) for x in range(BOARDSIZE_X)] for y in range(BOARDSIZE_Y)]
        for row in self.board:
            for tile in row:
                ALL_SPRITES.add(tile)

    def render(self, text_board):
        print("rendering...")
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if text_board[y][x]=="#":
                    self.board[y][x].change_color(WALL_COLOR)
                if text_board[y][x]==" ":
                    self.board[y][x].change_color(EMPTY_COLOR)
                if text_board[y][x]=="*":
                    self.board[y][x].change_color(PLAYER_COLOR)
                if text_board[y][x]=="^":
                    self.board[y][x].change_color(FOOD_COLOR)
                if text_board[y][x]=="@":
                    self.board[y][x].change_color(TAIL_COLOR)
                