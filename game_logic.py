# game_logic.py

class GameLogic:
    def __init__(self, maze):
        self.maze = maze
        self.agent_position = self.maze.start_point

    def reset_position(self):
        self.agent_position = self.maze.start_point

    def move_agent(self, direction):
        x, y = self.agent_position
        if direction == "UP" and x > 0 and self.maze.maze[x-1][y] == 0:
            self.agent_position = (x-1, y)
        elif direction == "DOWN" and x < self.maze.size - 1 and self.maze.maze[x+1][y] == 0:
            self.agent_position = (x+1, y)
        elif direction == "LEFT" and y > 0 and self.maze.maze[x][y-1] == 0:
            self.agent_position = (x, y-1)
        elif direction == "RIGHT" and y < self.maze.size - 1 and self.maze.maze[x][y+1] == 0:
            self.agent_position = (x, y+1)