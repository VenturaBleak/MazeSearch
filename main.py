# main.py
from maze import Maze
from game_logic import GameLogic
from solvers.bfs_solver import BFS_Solver
from visualizer import Visualizer
import pygame

if __name__ == "__main__":
    maze_size = 10

    maze = Maze(maze_size)
    maze.generate_random_maze()

    game = GameLogic(maze)

    solver = BFS_Solver(maze)
    process, path = solver.solve()  # Process captures the solving steps and path captures the final solution

    visualizer = Visualizer(maze)
    visualizer.draw_maze()
    visualizer.animate_solving_process(process)
    pygame.time.wait(500)  # Wait for half a second before animating the solution
    visualizer.animate_solution(path)

    # Keep the window open until closed by the user
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()