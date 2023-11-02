# solvers/bfs_solver.py

from collections import deque

class BFS_Solver:
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
        queue = deque([self.start])
        parent = {self.start: None}
        process = []  # to keep track of the order of cells being visited

        while queue:
            current = queue.popleft()
            process.append(current)  # Add current cell to the process list
            self.visited.add(current)
            if current == self.end:
                break
            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.add(neighbor)
                    parent[neighbor] = current

        if self.end not in parent:  # Check if end is not reached
            return process, []

        path = []
        while self.end:
            path.append(self.end)
            self.end = parent.get(self.end)  # Use get to avoid KeyError

        return process, path[::-1]