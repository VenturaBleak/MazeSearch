# solvers/a_star_solver.py
from .base_solver import Solver
from queue import PriorityQueue

class A_Star_Solver(Solver):
    def heuristic(self, position):
        # Manhattan distance to goal
        return abs(position[0] - self.end[0]) + abs(position[1] - self.end[1])

    def solve(self):
        open_list = PriorityQueue()
        open_list.put((0, self.start))
        parent = {self.start: None}
        g = {self.start: 0}  # Actual cost from start to this position
        process = []

        while not open_list.empty():
            _, current = open_list.get()
            process.append(current)

            for neighbor in self.get_neighbors(current):
                # Tentative gScore
                tentative_g = g[current] + 1
                if neighbor not in g or tentative_g < g[neighbor]:
                    g[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor)
                    open_list.put((f, neighbor))
                    parent[neighbor] = current
                    self.visited.add(neighbor)

        # Removing the early stopping condition for the end
        path = []
        node = self.end
        while node:
            path.append(node)
            node = parent.get(node)

        return process, path[::-1]