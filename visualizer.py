import tkinter as tk

class Visualizer:
    def __init__(self, maze, solver, time_step=500):
        self.maze = maze
        self.solver = solver
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=maze.size * 20, height=maze.size * 20, bg="white")
        self.canvas.pack()
        self.time_step = time_step

        # Introduce flag to determine whether we're visualizing the shortest path
        self.visualizing_path = False

    def draw_maze(self):
        for i in range(self.maze.size):
            for j in range(self.maze.size):
                cell_value = self.maze.maze[i][j]
                if cell_value == 0:  # Empty
                    color = "white"
                elif cell_value == 1:  # Wall
                    color = "black"
                elif cell_value == 2:  # Start
                    color = "green"
                elif cell_value == 3:  # End
                    color = "red"
                self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color, outline="gray")

    def visualize_agent(self, current_position):
        i, j = current_position
        if (i, j) != self.maze.end_point:  # Ensure not to overwrite the goal
            self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="purple", outline="gray")
            self.canvas.create_text((j+0.5)*20, (i+0.5)*20, text="A", fill="white")


    def visualize_explored(self, position):
        i, j = position
        if position == self.maze.start_point:
            color = "green"
        elif position != self.maze.end_point:
            color = "lightblue"
        else:
            color = None  # Ensures the end point isn't overwritten
        if color:
            self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color, outline="gray")

    def visualize_shortest_path(self, position):
        i, j = position
        if position in [self.maze.start_point, self.maze.end_point]:
            return
        color = "gold"
        self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color, outline="gray")

    def animate_solution(self):
        if self.step_index < len(self.solver_steps):
            current = self.solver_steps[self.step_index]

            if not self.visualizing_path:  # If still doing BFS
                if self.step_index > 0:
                    prev = self.solver_steps[self.step_index - 1]
                    self.visualize_explored(prev)
                self.visualize_agent(current)
                if current == self.maze.end_point:  # If we've reached the goal
                    self.visualizing_path = True  # Set the flag
                    self.step_index = len(self.solver_steps) - 1  # Start from the last step
                else:
                    self.step_index += 1

            else:  # If we're visualizing the shortest path
                self.visualize_shortest_path(current)
                if current == self.maze.start_point:  # If we've reached the start point while visualizing path
                    self.root.after(self.time_step, self.root.destroy)  # Delayed termination
                    return  # Stop the backpropagation
                self.step_index -= 1  # Backtrack through the steps

            self.root.after(self.time_step, self.animate_solution)
        else:
            self.root.destroy()  # Terminate the window once BFS and shortest path are visualized

    def visualize_solution(self):
        self.draw_maze()
        self.solver_steps = list(self.solver.solve())
        self.step_index = 0
        self.root.after(self.time_step, self.animate_solution)
        self.root.mainloop()