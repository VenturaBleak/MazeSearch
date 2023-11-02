# Pygame Maze Solver

## Overview
This repository contains a Pygame application to generate random mazes and solve them using different algorithms. The goal is simple: start from a random position and find your way to the end point.

<img src="https://github.com/VenturaBleak/MazeSearch/blob/master/images/maze_solving.png" width="30%" height="30%"> <img src="https://github.com/VenturaBleak/MazeSearch/blob/master/images/maze_shortest_path.png" width="28%" height="28%">

*Generated maze.* *Maze solved using one of our algorithms.*

## Algorithms Used

### Depth-First Search (DFS)
DFS goes deep into the maze, exploring each branch before backtracking.

### Breadth-First Search (BFS)
BFS checks neighboring nodes first, moving to the next level of neighbors only once all on the current level are explored.

### A*
A* uses a heuristic to estimate the cost to the goal from a given node, prioritizing paths that seem more promising.

## Why This Repo?
- Learn and visualize common maze-solving algorithms.
  
- Showcase what Pygame can do in terms of visualizations.
  
- Understand maze generation, specifically with Prim's algorithm.

In this game, the agent starts on a random tile and aims to reach another random end tile. Each maze generated is checked to make sure it can be solved.

## Repository Structure

### Main Directory:
- `solvers/`: Contains the different maze-solving algorithms.
- `game_logic.py`: Handles the game's rules and mechanics.
- `main.py`: The starting point of the application.
- `maze.py`: Handles maze generation.
- `visualizer.py`: Displays the maze and its solution using Pygame.

### Solvers Directory:
- `__init__.py`: Initialization file.
- `a_star_solver.py`: A* solver implementation.
- `base_solver.py`: Basic structure for all solvers.
- `bfs_solver.py`: BFS solver implementation.
- `dfs_solver.py`: DFS solver implementation.

## Getting Started
Generate a maze, then solve it using one of the provided algorithms. It's a visual and interactive way to understand how each method works.
