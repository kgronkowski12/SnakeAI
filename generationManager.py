from snake import *
from config import *
from boardRenderer import *
import time
import statistics

class GenerationManager:

    def __init__(self, ALL_SPRITES):
        self.renderer = BoardRenderer(ALL_SPRITES)
        self.snakes = []
        self.gen = 0
        self.watching = 0
        self.changing = 0
        self.new_gen = 0

    # Prepares first generation
    def prepare(self):
        self.snakes = []
        for i in range(FIRST_GENERATION_SIZE):   
            snake = Snake()
            snake.get_brain().randomize_weights()
            self.snakes.append(snake)

        self.gen = 1

    # Main game loop
    def loop(self):
        dead = 0
        self.changing=0
        point_count = []
        # Snakes take turns
        for snake_number in range(len(self.snakes)):
            point_count.append(self.snakes[snake_number].points)
            if self.snakes[snake_number].alive:
                self.snakes[snake_number].takeTurn()
                if snake_number==self.watching:
                    if self.changing==0:
                        # If we are watching snake, render it's board
                        self.snakes[self.watching].printBoard()
                        self.renderer.render(self.snakes[self.watching].board, True)
                if not self.snakes[self.watching].alive and self.changing==0:
                    # If snake just died, wait half a second and spectate other snake
                    self.changing = 1
                    self.renderer.render(self.snakes[self.watching].board, False)
                    time.sleep(0.5)
                    self.watching = snake_number
            else:
                dead+=1
            if dead==len(self.snakes):

                # Prepare next generation!

                # Sort by point count
                self.snakes = sorted(self.snakes, key=lambda snake : snake.points, reverse = True)
                print("GEN",self.gen," MAX POINTS: ",self.snakes[0].points)
                self.new_gen = 1
                self.watching=0
                self.gen+=1
                time.sleep(5)

                # Keep best snakes
                self.snakes = self.snakes[0:BEST_SAMPLES]
                print("kept!")

                # Best snakes breed with each other
                newSnakes = []
                for repeat in range(REPEATS):
                    for mother in range(BEST_SAMPLES):
                        for father in range(BEST_SAMPLES):
                            if mother != father:
                                offspring = Snake()
                                offspring.get_brain().mix_brains(self.snakes[mother].get_brain(),self.snakes[father].get_brain())
                                newSnakes.append(offspring)
                for s in newSnakes:
                    self.snakes.append(s)
                # Add random snakes
                for s in range(NEW_SNAKES):
                    sn = Snake()
                    self.snakes.append(sn)

                for snake in self.snakes:
                    snake.boardSetup()

        # Update displayed text
        gen_number = f"Generation {self.gen}"
        alive_snakes = f"Alive snakes: {len(self.snakes)-dead}/{len(self.snakes)}"
        b = max(point_count)
        best = f"Highest score: {b}"
        m = int(statistics.mean(point_count))
        mean = f"Mean score: {m}"
        med = statistics.median(point_count)
        median = f"Median score: {med}"
        sd = int(statistics.stdev(point_count))
        standard_deviation = f"Standard deviation: {sd}"
        watching_txt = f"You are watching Snake#{self.watching+1}, who has {self.snakes[self.watching].points} points."
        
        self.renderer.gen_number.changeText(gen_number)
        self.renderer.best.changeText(best)
        self.renderer.mean.changeText(mean)
        self.renderer.median.changeText(median)
        self.renderer.deviation.changeText(standard_deviation)
        self.renderer.alive_snakes.changeText(alive_snakes)
        self.renderer.watching.changeText(watching_txt)

        # Update gen info
        gen_info = f"Gen#{self.gen}: HSc {b} M {m} Mdn {med} SD {sd}"
        if self.gen<=10:
            self.renderer.prev_gen[self.gen-1].changeText(gen_info)
        else:
            # Shift all gen info by one
            if self.new_gen==1:
                for g in range(9):
                    self.renderer.prev_gen[g].changeText(self.renderer.prev_gen[g+1].plain)
                self.new_gen=0
            self.renderer.prev_gen[9].changeText(gen_info)
            
        return 0


