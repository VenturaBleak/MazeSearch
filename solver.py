import numpy as np
from collections import deque
import heapq  # for priority queue in A* solver
import random  # for randomizing neighbors in DFS

class MazeSolver:
    def __init__(self, maze):
        """Initialize the maze solver with the provided maze."""
        self.maze = maze
        self.visited = np.zeros_like(maze.maze, dtype=bool)
        self.parent = dict()  # To store the parent of each cell

    def get_neighbors(self, current):
        """Returns valid neighbors for the given cell."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            x, y = current
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.maze.size and 0 <= ny < self.maze.size and
                    not self.visited[nx][ny] and self.maze.maze[nx][ny] != 1):
                neighbors.append((nx, ny))
        return neighbors

    def backtrack_path(self):
        """Backtracks from the goal to the start using parent information."""
        path = []
        current = self.maze.end_point
        while current != self.maze.start_point:
            path.append(current)
            current = self.parent[current]
        path.append(self.maze.start_point)
        return path

    def solve(self):
        """Placeholder method. Actual implementation will be in the subclasses."""
        raise NotImplementedError("Subclasses must implement solve method")


class BFS_Solver(MazeSolver):
    """Breadth-first search based maze solver."""

    def solve(self):
        queue = deque([self.maze.start_point])
        self.visited[self.maze.start_point] = True
        yield self.maze.start_point

        while queue:
            current = queue.popleft()
            for neighbor in self.get_neighbors(current):
                nx, ny = neighbor
                self.visited[nx][ny] = True
                queue.append((nx, ny))
                yield neighbor

                # Store parent info
                self.parent[neighbor] = current

            if current == self.maze.end_point:
                break

        # Now, backtrack from end to start to get the shortest path
        for p in reversed(self.backtrack_path()):
            yield p

class DFS_Solver(MazeSolver):
    """Depth-first search based maze solver with randomized neighbor selection."""

    def solve(self):
        stack = [self.maze.start_point]
        self.visited[self.maze.start_point] = True
        yield self.maze.start_point

        while stack:
            current = stack[-1]  # Check the top of the stack, but don't pop it yet

            neighbors = self.get_neighbors(current)
            if neighbors:  # If there are unvisited neighbors
                random_neighbor = random.choice(neighbors)
                nx, ny = random_neighbor
                self.visited[nx][ny] = True
                stack.append(random_neighbor)  # Push the chosen neighbor to the stack
                yield random_neighbor
                self.parent[random_neighbor] = current  # Store parent info
            else:  # If all neighbors are explored, pop the current node
                stack.pop()

            if current == self.maze.end_point:
                break

        # Now, backtrack from end to start to get the shortest path
        for p in reversed(self.backtrack_path()):
            yield p

class AStar_Solver(MazeSolver):
    """A* search based maze solver using Manhattan distance heuristic."""

    def __init__(self, maze):
        super().__init__(maze)
        self.cost = {cell: float('inf') for row in maze.maze for cell in row}
        self.cost[self.maze.start_point] = 0

    def heuristic(self, current):
        """Compute the Manhattan distance from current cell to the goal."""
        x1, y1 = current
        x2, y2 = self.maze.end_point
        return abs(x1 - x2) + abs(y1 - y2)

    def solve(self):
        pq = []  # The priority queue using heapq
        heapq.heappush(pq, (0, self.maze.start_point))  # Initialize with heuristic cost for start point
        self.visited[self.maze.start_point] = True
        yield self.maze.start_point

        while pq:
            _, current = heapq.heappop(pq)  # Extract the cell with the lowest cost
            for neighbor in self.get_neighbors(current):
                nx, ny = neighbor
                new_cost = self.cost[current] + 1
                if new_cost < self.cost[neighbor]:
                    self.cost[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(pq, (priority, neighbor))
                    self.parent[neighbor] = current
                self.visited[nx][ny] = True
                yield neighbor

                # Store parent info
                self.parent[neighbor] = current

            if current == self.maze.end_point:
                break

        # Now, backtrack from end to start to get the shortest path
        for p in reversed(self.backtrack_path()):
            yield p