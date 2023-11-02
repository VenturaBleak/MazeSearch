import numpy as np
from collections import deque

class BFS_Solver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = np.zeros_like(maze.maze, dtype=bool)
        self.parent = dict()  # To store the parent of each cell

    def solve(self):
        queue = deque([self.maze.start_point])
        self.visited[self.maze.start_point] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        yield self.maze.start_point  # Begin visualization from the start point

        while queue:
            current = queue.popleft()
            for dx, dy in directions:
                x, y = current
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.maze.size and 0 <= ny < self.maze.size and
                        not self.visited[nx][ny] and self.maze.maze[nx][ny] != 1):
                    self.visited[nx][ny] = True
                    queue.append((nx, ny))
                    yield (nx, ny)  # Yield every cell that gets processed

                    # Store parent info
                    self.parent[(nx, ny)] = current

            if current == self.maze.end_point:
                break

        # Now, backpropagate from end to start to get the shortest path
        path = []
        current = self.maze.end_point
        while current != self.maze.start_point:
            path.append(current)
            current = self.parent[current]
        path.append(self.maze.start_point)

        for p in reversed(path):
            yield p
