from snake import *
from config import *
import time

snakes = []
for i in range(FIRST_GENERATION_SIZE):   
    snake = Snake()
    snake.get_brain().randomize_weights()
    snakes.append(snake)

while True: # main loop
    dead = 0
    for snake_number in range(len(snakes)):
        if(snake_number==0 and snakes[0].alive):
            snakes[0].printBoard()
            time.sleep(TURN_TIME)
        if(snakes[snake_number].alive):
            snakes[snake_number].takeTurn()
        else:
            dead+=1
        if dead==len(snakes):

            # Przygotuj następną generacje!

            # Sortowanie od najlepszych
            snakes = sorted(snakes, key=lambda snake : snake.points, reverse = True)
            print("GEN 1 MAX POINTS: ",snakes[0].points)
            print(len(snakes))

            # Zostawiamy najlepsze węże
            snakes = snakes[0:BEST_SAMPLES]
            print("kept!")

            # Najlepsze węże mają dzieci ze sobą, prowadzi do uśredniania wszystkich wartości
            for mother in range(BEST_SAMPLES):
                for father in range(BEST_SAMPLES):
                    print(mother," <-> ",father)
                    if mother != father:
                        offspring = Snake()
                        offspring.get_brain().mix_brains(snakes[mother].get_brain(),snakes[father].get_brain())
                        snakes.append(offspring)

            for snake in snakes:
                snake.boardSetup()
            


