from snake import *
from config import *
import time

snake1 = Snake()
snake1.get_brain().randomize_weights()

while snake1.alive:
    snake1.printBoard()
    snake1.takeTurn()
    time.sleep(TURN_TIME)