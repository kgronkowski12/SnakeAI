import pygame

# PyGame window values
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1100
FPS = 60

# Board render settings
BACKGROUND_COLOR = (255,255,255)
WALL_COLOR = (160,160,160)
EMPTY_COLOR = (0,0,0)
TAIL_COLOR = (0,0,255)
FOOD_COLOR = (0,255,0)
DEAD_COLOR = (200,0,0)

# Global variables
ALL_SPRITES = pygame.sprite.Group()   
ALL_TEXT = []

# Board settings
BOARDSIZE_X = 30
BOARDSIZE_Y = 45
FOOD_COUNT = 3

# Snake settings
HIDDEN_LAYER_SIZE = 9
MAX_HUNGER = 300


# Generation settings
FIRST_GENERATION_SIZE = 25
BEST_SAMPLES = 6
REPEATS = 1
NEW_SNAKES = 5
# Number of snakes per generation:
# Best_samples + (best_samples-1)*best_samples*repeats + new_snakes


# Mutation settings
SMALL_MUTATION_CHANCE = 0.1
BIG_MUTATION_CHANCE = 0.01