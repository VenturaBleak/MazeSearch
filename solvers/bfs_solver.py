# solvers/bfs_solver.py
from .base_solver import Solver
from collections import deque

class BFS_Solver(Solver):
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
                    if neighbor not in parent:  # Only set parent if it hasn't been set before
                        parent[neighbor] = current

        if self.end not in parent:  # Check if end is not reached
            return process, []

        path = []
        current = self.end
        while current:
            path.append(current)
            current = parent[current]  # We don't need the get method here since we know current is in parent

        return process, path[::-1]