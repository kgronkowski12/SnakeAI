from snake import *
from config import *
from boardRenderer import *
import time

class GenerationManager:

    def __init__(self, ALL_SPRITES):
        self.renderer = BoardRenderer(ALL_SPRITES)
        self.snakes = []
        self.gen = 0

    def prepare(self):
        self.snakes = []
        for i in range(FIRST_GENERATION_SIZE):   
            snake = Snake()
            snake.get_brain().randomize_weights()
            self.snakes.append(snake)

        self.gen = 1

    def loop(self):
        dead = 0
        for snake_number in range(len(self.snakes)):
            if(snake_number==0 and self.snakes[0].alive):
                self.snakes[0].printBoard()
                self.renderer.render(self.snakes[0].board)
                #time.sleep(TURN_TIME)
            if(self.snakes[snake_number].alive):
                self.snakes[snake_number].takeTurn()
            else:
                dead+=1
            if dead==len(self.snakes):

                # Przygotuj następną generacje!

                # Sortowanie od najlepszych
                self.snakes = sorted(self.snakes, key=lambda snake : snake.points, reverse = True)
                print("GEN",self.gen," MAX POINTS: ",self.snakes[0].points)
                self.gen+=1
                time.sleep(5)

                # Zostawiamy najlepsze węże
                self.snakes = self.snakes[0:BEST_SAMPLES]
                print("kept!")

                # Najlepsze węże mają dzieci ze sobą, prowadzi do uśredniania wszystkich wartości
                for mother in range(BEST_SAMPLES):
                    for father in range(BEST_SAMPLES):
                        if mother != father:
                            offspring = Snake()
                            offspring.get_brain().mix_brains(self.snakes[mother].get_brain(),self.snakes[father].get_brain())
                            self.snakes.append(offspring)

                for snake in self.snakes:
                    snake.boardSetup()
                


