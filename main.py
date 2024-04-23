from snake import *
from config import *
import time

snake1 = Snake()
while snake1.alive:
    snake1.printBoard()
    snake1.takeTurn()
    time.sleep(TURN_TIME)