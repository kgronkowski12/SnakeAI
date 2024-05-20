import random
from config import *

# Class responsible to make decisions  on which direction the snake should move in.
class Brain:

    def __init__(self):
        self.hidden_layer= dict()

    # Merges to brains into one, used when creating offspring of two snakes
    def mix_brains(self, mother, father):
        for key, val in mother.hidden_layer.items():
            weights = []
            for index in range(len(val)):
                i = val[index]
                x = father.hidden_layer[key][index]
                weight_val = i+x
                weight_val/=2

                mutation_val = random.uniform(0,1)
                if mutation_val < SMALL_MUTATION_CHANCE:
                    weight_val*=random.uniform(0.9,1.1)

                if mutation_val < BIG_MUTATION_CHANCE:
                    weight_val*=random.uniform(-5,5)

                weights.append(weight_val)
            self.hidden_layer[key]=weights

    # Randomizes the hidden layer values.
    def randomize_weights(self):
        # # - wall
        # ^ - food
        # @ - tail
        # stubborn - unwilingness to change directions
        # widzimisie - strength of wanting to move in a random direction for no reason
        # widzimisie_timer - how often widzimisie changes
        objects = ["#", "^", "@", "stubborn", "widzimisie","widzimisie_timer"]
        for obj in objects:
            weights = []
            for i in range(HIDDEN_LAYER_SIZE):
                weights.append(random.uniform(-5,5))
            self.hidden_layer[obj]=weights

    # Assigns a value to a direction
    def get_output(self, obj, distance):
        out = 1.0
        # Multiplies out by all values in hidden layer, matching seen obstacle
        for node in range(HIDDEN_LAYER_SIZE):
            out*=self.hidden_layer[obj][node]
        # The farther away the obstacle, the less significant output value
        out/=distance
        return out


