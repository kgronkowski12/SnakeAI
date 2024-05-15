import pygame
from pygame.locals import *
from generationManager import GenerationManager
from config import *
from boardRenderer import *
from tile import *
pygame.init()
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake AI")

ALL_SPRITES = pygame.sprite.Group()

gm = GenerationManager(ALL_SPRITES)
gm.prepare()

out = 0
while True:

    if out==0:
        out = 1    
        out = gm.loop()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill(BACKGROUND_COLOR)
 
    for entity in ALL_SPRITES:
        displaysurface.blit(entity.surf, entity.rect)

    for holder in ALL_TEXT:
        displaysurface.blit(holder.text, holder.position)
 
    pygame.display.update()
    FramePerSec.tick(FPS)