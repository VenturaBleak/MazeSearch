# solvers/dfs_solver.py
from .base_solver import Solver
import random

class DFS_Solver(Solver):
    def solve(self):
        stack = [self.start]
        parent = {self.start: None}
        process = []

        while stack:
            current = stack.pop()

            if current in self.visited:
                continue

            process.append(current)
            self.visited.add(current)

            neighbors = self.get_neighbors(current)
            random.shuffle(neighbors)  # Randomize the exploration order

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    stack.append(neighbor)
                    if neighbor not in parent:  # To ensure the shortest path in the maze
                        parent[neighbor] = current

        # Removing the early stopping condition for the end
        path = []
        node = self.end
        while node:
            path.append(node)
            node = parent.get(node)

        return process, path[::-1]