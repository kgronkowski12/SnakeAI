import pygame
from config import *

# One square sprite from which the board is built
class Tile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__() 
        self.pos = position
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(EMPTY_COLOR)
        self.rect = self.surf.get_rect()
        self.rect.topleft = position
    
    def change_color(self, color):
        self.surf.fill(color)