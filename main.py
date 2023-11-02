from maze import Maze
from solver import BFS_Solver
from visualizer import Visualizer

if __name__ == "__main__":
    maze = Maze(size=20)
    solver = BFS_Solver(maze)
    visualizer = Visualizer(maze, solver, time_step=200)
    visualizer.visualize_solution()