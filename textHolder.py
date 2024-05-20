import pygame

# Holds text and it's position on the screen
class TextHolder:

    def __init__(self,pos):
        pygame.font.init()
        self.font = pygame.font.Font("./fonts/Pixels.ttf", 50)
        self.position = pos
        self.text = self.font.render("lorem ipsum", False, (0, 0, 0))
        self.plain = "lorem ipsum"

    # Changes text
    def changeText(self, text):
        self.text = self.font.render(text, False, (0, 0, 0))
        self.plain = text