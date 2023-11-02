# maze.py

import numpy as np
import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = np.zeros((size, size))
        self.start_point = (0, 0)
        self.end_point = (size-1, size-1)

    def generate_random_maze(self, obstacle_density=0.31):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in [self.start_point, self.end_point] and random.random() < obstacle_density:
                    self.maze[i][j] = 1

    def save_to_disk(self, filename):
        np.save(filename, self.maze)

    def load_from_disk(self, filename):
        self.maze = np.load(filename)