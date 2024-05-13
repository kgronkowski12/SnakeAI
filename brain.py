import random
from config import *

class Brain:

    def __init__(self):
        self.hidden_layer= dict()

    def copy_brain(self,other_brain):
        for key, val in other_brain.hidden_layer:
            self.hidden_layer[key]=val

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


    def randomize_weights(self):
        objects = ["#", "^", "@"]
        for obj in objects:
            weights = []
            for i in range(HIDDEN_LAYER_SIZE):
                weights.append(random.uniform(-100,100))
            self.hidden_layer[obj]=weights

    def get_output(self, obj, distance):
        multiplayer=(max(BOARDSIZE_X,BOARDSIZE_Y)*2-distance)/max(BOARDSIZE_X,BOARDSIZE_Y)/2
        out = 1.0
        for node in range(HIDDEN_LAYER_SIZE):
            out*=self.hidden_layer[obj][node]
        out *= multiplayer

        return out


