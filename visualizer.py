# visualizer.py

import pygame

class Visualizer:
    def __init__(self, maze):
        pygame.init()
        self.maze = maze
        self.cell_size = 20  # Assuming each cell is 20x20 pixels
        self.screen = pygame.display.set_mode((maze.size * self.cell_size, maze.size * self.cell_size))
        pygame.display.set_caption('Maze Solver')
        self.agent_previous_position = None

    def draw_maze(self):
        self.screen.fill((255, 255, 255))  # Resetting the maze by filling it with white
        for i in range(self.maze.size):
            for j in range(self.maze.size):
                color = (255, 255, 255)  # white for path
                if self.maze.maze[i][j] == 1:
                    color = (0, 0, 0)  # black for obstacle
                pygame.draw.rect(self.screen, color,
                                 (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
        # Mark start and end positions
        self.draw_start_end_positions()

    def draw_start_end_positions(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (
            self.maze.start_point[1] * self.cell_size, self.maze.start_point[0] * self.cell_size, self.cell_size,
            self.cell_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (
            self.maze.end_point[1] * self.cell_size, self.maze.end_point[0] * self.cell_size, self.cell_size,
            self.cell_size))

    def draw_visited_cell(self, position, color=(255, 215, 0)):  # gold color for visited cells
        pygame.draw.rect(self.screen, color,
                         (position[1] * self.cell_size, position[0] * self.cell_size, self.cell_size, self.cell_size))

    def draw_agent_position(self, position, color=(0, 255, 0)):  # green color for agent
        # Clear the agent from its previous position
        if self.agent_previous_position:
            self.draw_visited_cell(self.agent_previous_position)

        # Ensure start and end positions are always drawn with their respective colors
        self.draw_start_end_positions()

        # Draw the agent as a circle inside the tile on top of the maze and start/end points
        pygame.draw.circle(self.screen, color,
                           (int(position[1] * self.cell_size + self.cell_size / 2),
                            int(position[0] * self.cell_size + self.cell_size / 2)),
                           int(self.cell_size / 2) - 2)  # -2 for a little padding

        # Update the agent's previous position
        self.agent_previous_position = position

        pygame.display.flip()

    def animate_solving_process(self, process):
        for position in process:
            self.draw_visited_cell(position)
            self.draw_agent_position(position)
            pygame.time.wait(50)

    def animate_solution(self, solution):
        self.draw_maze()  # Redraw the maze to reset before visualizing the solution
        for position in solution:
            self.draw_agent_position(position)
            pygame.time.wait(100)
        pygame.display.flip()