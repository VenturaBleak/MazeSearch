# visualizer.py

import pygame


class Visualizer:
    def __init__(self, maze):
        pygame.init()
        self.maze = maze
        self.cell_size = 20  # Assuming each cell is 20x20 pixels
        self.screen = pygame.display.set_mode((maze.size * self.cell_size, maze.size * self.cell_size))
        pygame.display.set_caption('Maze Solver')

    def draw_maze(self):
        for i in range(self.maze.size):
            for j in range(self.maze.size):
                color = (255, 255, 255)  # white for path
                if self.maze.maze[i][j] == 1:
                    color = (0, 0, 0)  # black for obstacle
                pygame.draw.rect(self.screen, color,
                                 (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

        # Mark start and end positions
        pygame.draw.rect(self.screen, (0, 0, 255), (
        self.maze.start_point[1] * self.cell_size, self.maze.start_point[0] * self.cell_size, self.cell_size,
        self.cell_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (
        self.maze.end_point[1] * self.cell_size, self.maze.end_point[0] * self.cell_size, self.cell_size,
        self.cell_size))

        pygame.display.flip()

    def draw_agent_position(self, position, color=(0, 255, 0)):  # default color is green
        pygame.draw.circle(self.screen, color, (
        position[1] * self.cell_size + self.cell_size // 2, position[0] * self.cell_size + self.cell_size // 2),
                           self.cell_size // 2 - 2)
        pygame.display.flip()

    def animate_solution(self, solution):
        for position in solution:
            self.draw_agent_position(position)
            pygame.time.wait(100)

    def animate_solving_process(self, process):
        for position in process:
            self.draw_agent_position(position, color=(255, 255, 0))  # yellow for the solving process
            pygame.time.wait(50)