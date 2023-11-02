# solvers/base_solver.py

class Solver:
    def __init__(self, maze):
        self.maze = maze.maze
        self.start = maze.start_point
        self.end = maze.end_point
        self.visited = set()

    def get_neighbors(self, current):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze) and self.maze[nx][ny] != 1 and (nx, ny) not in self.visited:
                neighbors.append((nx, ny))
        return neighbors

    def solve(self):
        raise NotImplementedError("Subclasses must implement this method.")