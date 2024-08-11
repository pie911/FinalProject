import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

# Load data from JSON file
with open('F:/FinalProject/data.json', 'r') as f:
    data = json.load(f)

# Extract data
mass = np.array(data["mass"])
speed = np.array(data["speed"])
height = np.array(data["height"])
wire_length = np.array(data["wire_length"])
wire_diameter = np.array(data["wire_diameter"])
motor_power = np.array(data["motor_power"])
operational_time = np.array(data["operational_time"])
maintenance_cost = np.array(data["maintenance_cost"])
training_cost = np.array(data["training_cost"])
material_strength = np.array(data["material_strength"])
budget = np.array(data["budget"])
location = np.array(data["location"])
reactant1 = np.array(data["reactant1"])
reactant2 = np.array(data["reactant2"])
sample_type = np.array(data["sample_type"])
wind_speed = np.array(data["wind_speed"])
area = np.array(data["area"])
iron_temp = np.array(data["iron_temp"])
motor_temp = np.array(data["motor_temp"])

# Calculate derived data
weight = mass * 9.8
centripetal_force = (mass * speed**2) / np.random.uniform(0.1, 10, 10)
fall_time = np.sqrt((2 * height) / 9.8)
horizontal_distance = speed * fall_time
total_cost = mass * 100 + np.random.uniform(1000, 10000, 10)
kinetic_energy = 0.5 * mass * speed**2

# List of plots
plots = [
    ("Weight vs. Mass", mass, weight, "Mass (kg)", "Weight (N)"),
    ("Centripetal Force vs. Speed", speed, centripetal_force, "Speed (m/s)", "Centripetal Force (N)"),
    ("Fall Time vs. Height", height, fall_time, "Height (m)", "Fall Time (s)"),
    ("Horizontal Distance vs. Speed", speed, horizontal_distance, "Speed (m/s)", "Horizontal Distance (m)"),
    ("Total Cost vs. Mass", mass, total_cost, "Mass (kg)", "Total Cost (INR)"),
    ("Kinetic Energy vs. Speed", speed, kinetic_energy, "Speed (m/s)", "Kinetic Energy (J)")
]

# Initialize plot index
plot_index = 0

# Function to update the plot
def update_plot():
    global plot_index
    title, x, y, xlabel, ylabel = plots[plot_index]
    ax.clear()
    ax.plot(x, y, 'o-')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    canvas.draw()

# Function to handle key press events
def on_key(event):
    global plot_index
    if event.keysym == 'Right':
        plot_index = (plot_index + 1) % len(plots)
    elif event.keysym == 'Left':
        plot_index = (plot_index - 1) % len(plots)
    update_plot()

# Create the main window
root = tk.Tk()
root.title("Experiment Analysis Graphs")

# Create a figure and axis
fig, ax = plt.subplots()

# Create a canvas to display the plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Bind key press events to the main window
root.bind('<Right>', on_key)
root.bind('<Left>', on_key)

# Initialize the first plot
update_plot()

# Run the main loop
root.mainloop()
