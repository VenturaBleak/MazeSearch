import numpy as np
import random
from solvers.bfs_solver import BFS_Solver

class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = np.ones((size, size), dtype=int)
        self.frontier_list = []

        # Choose a random point and add the neighboring walls to the frontier.
        start_x, start_y = random.randint(0, size - 2), random.randint(0, size - 2)
        self.maze[start_x][start_y] = 0
        self.add_frontier(start_x, start_y)

        self.generate_maze()

        self.randomize_start_end_points()

    def generate_maze(self):
        while self.frontier_list:
            x, y = self.frontier_list[random.randint(0, len(self.frontier_list) - 1)]
            self.frontier_list.remove((x, y))

            # Neighbor cells: up, down, left, right
            neighbors = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

            # Check which neighbors are part of the maze (value is 0)
            maze_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.size and 0 <= ny < self.size and self.maze[nx][ny] == 0]

            # If there's only one neighboring cell that's a part of the maze, carve a passage
            if len(maze_neighbors) == 1:
                self.maze[x][y] = 0
                self.add_frontier(x, y)

    def add_frontier(self, x, y):
        # Check potential walls to be added to frontier
        if x > 1 and self.maze[x-2][y] == 1 and (x-2, y) not in self.frontier_list:
            self.frontier_list.append((x-1, y))
        if x < self.size - 2 and self.maze[x+2][y] == 1 and (x+2, y) not in self.frontier_list:
            self.frontier_list.append((x+1, y))
        if y > 1 and self.maze[x][y-2] == 1 and (x, y-2) not in self.frontier_list:
            self.frontier_list.append((x, y-1))
        if y < self.size - 2 and self.maze[x][y+2] == 1 and (x, y+2) not in self.frontier_list:
            self.frontier_list.append((x, y+1))

    def randomize_start_end_points(self):
        while True:
            self.start_point = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            self.end_point = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if abs(self.end_point[0] - self.start_point[0]) + abs(self.end_point[1] - self.start_point[1]) > 2 and self.maze[self.start_point[0]][self.start_point[1]] == 0 and self.maze[self.end_point[0]][self.end_point[1]] == 0:
                break

    def is_solvable(self):
        solver = BFS_Solver(self.maze, self.start_point, self.end_point)
        _, path = solver.solve()
        return len(path) > 0

    def save_to_disk(self, filename):
        np.save(filename, self.maze)

    def load_from_disk(self, filename):
        self.maze = np.load(filename)