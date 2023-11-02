# main.py
from maze import Maze
from game_logic import GameLogic
from visualizer import Visualizer
from solvers.bfs_solver import BFS_Solver
from solvers.dfs_solver import DFS_Solver
from solvers.a_star_solver import A_Star_Solver

import pygame

if __name__ == "__main__":
    maze_size = 20
    #hi

    maze = Maze(maze_size)

    game_logic = GameLogic(maze)

    solvers = [BFS_Solver, DFS_Solver, A_Star_Solver]  # Add other solvers to this list
    visualizer = Visualizer(maze)

    for solver_class in solvers:
        solver = solver_class(maze)
        process, path = solver.solve()

        visualizer.draw_maze()

        # Animate the solving process and solution
        visualizer.animate_solving_process(process)
        pygame.time.wait(500)  # Optional: Wait for half a second before animating the solution
        visualizer.animate_solution(path)
        pygame.time.wait(1000)  # Wait for 2 seconds before moving to the next solver

    pygame.quit()