# main.py
from maze import Maze
from game_logic import GameLogic
from solvers.bfs_solver import BFS_Solver
from visualizer import Visualizer
import pygame

if __name__ == "__main__":
    maze_size = 8

    maze = Maze(maze_size)
    maze.generate_random_maze()

    game_logic = GameLogic(maze)
    solver = BFS_Solver(maze)
    process, path = solver.solve()

    visualizer = Visualizer(maze)
    visualizer.draw_maze()

    # Animate the BFS solving process and solution
    visualizer.animate_solving_process(process)
    pygame.time.wait(500)  # Optional: Wait for half a second before animating the solution
    visualizer.animate_solution(path)

    # Wait for a while after visualization and then close pygame
    pygame.time.wait(1000)  # Wait for 2 seconds before auto-closing
    pygame.quit()