import numpy as np

class Maze:
    def __init__(self, size=10):
        self.size = size
        # Let's use a 2D numpy array to represent the maze.
        # 0 means path, 1 means wall, 2 means start, and 3 means end.
        self.maze = np.zeros((size, size), dtype=int)

        # Set random walls
        wall_indices = np.random.choice(size*size, size*2, replace=False)
        self.maze[np.unravel_index(wall_indices, (size, size))] = 1

        # Set random start and end points
        start_point = tuple(np.random.randint(0, size, 2))
        end_point = tuple(np.random.randint(0, size, 2))
        while self.maze[end_point] == 1 or start_point == end_point:
            end_point = tuple(np.random.randint(0, size, 2))

        self.maze[start_point] = 2
        self.maze[end_point] = 3
        self.start_point = start_point
        self.end_point = end_point