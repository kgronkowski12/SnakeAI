import random
from config import *

class Brain:

    def __init__(self):
        self.input = [0 for x in range(4)]
        self.hidden_layer= dict()

    def randomize_weights(self):
        objects = ["#", "^", "@"]
        for obj in objects:
            weights = []
            for i in range(HIDDEN_LAYER_SIZE):
                weights.append(random.uniform(-1,1))
            self.hidden_layer[obj]=weights

    def get_output(self, obj, distance):
        multiplayer=(max(BOARDSIZE_X,BOARDSIZE_Y)-distance)/max(BOARDSIZE_X,BOARDSIZE_Y)
        out = 1.0
        for node in range(HIDDEN_LAYER_SIZE):
            out*=self.hidden_layer[obj][node]
        return out


