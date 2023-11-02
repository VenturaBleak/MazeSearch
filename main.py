from maze import Maze
from solver import BFS_Solver, DFS_Solver
from visualizer import Visualizer

if __name__ == "__main__":
    # create a maze
    maze = Maze(size=10)

    # # bfs solver
    # bfs_solver = BFS_Solver(maze)
    # visualizer = Visualizer(maze, bfs_solver, time_step=200)
    # visualizer.visualize_solution()

    # dfs solver
    dfs_solver = DFS_Solver(maze)
    visualizer = Visualizer(maze, dfs_solver, time_step=200)
    visualizer.visualize_solution()