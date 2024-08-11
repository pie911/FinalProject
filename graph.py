import numpy as np
import json
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Load data from JSON file
json_file_path = 'F:/FinalProject/data.json'
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create a new folder 'docs' if it doesn't exist
docs_folder = 'F:/FinalProject/docs'
if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

# Create a new folder for the current run
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
run_folder = os.path.join(docs_folder, f'graphs_{timestamp}')
os.makedirs(run_folder)

# Function to save and show plots
def save_and_show_plot(fig, plot_name):
    image_file_path = os.path.join(run_folder, f'{plot_name}.png')
    fig.savefig(image_file_path, bbox_inches='tight')
    plt.show()
    plt.close(fig)
    print(f"{plot_name} saved and displayed successfully.")
    return image_file_path

# List to store image paths
image_paths = []

# Plotting different graphs
# 1. Mass vs Speed
fig, ax = plt.subplots()
ax.scatter(df['mass'], df['speed'])
ax.set_xlabel('Mass')
ax.set_ylabel('Speed')
ax.set_title('Mass vs Speed')
image_paths.append(save_and_show_plot(fig, 'mass_vs_speed'))

# 2. Height vs Wire Length
fig, ax = plt.subplots()
ax.scatter(df['height'], df['wire_length'])
ax.set_xlabel('Height')
ax.set_ylabel('Wire Length')
ax.set_title('Height vs Wire Length')
image_paths.append(save_and_show_plot(fig, 'height_vs_wire_length'))

# 3. Motor Power Distribution
fig, ax = plt.subplots()
ax.hist(df['motor_power'], bins=10)
ax.set_xlabel('Motor Power')
ax.set_ylabel('Frequency')
ax.set_title('Motor Power Distribution')
image_paths.append(save_and_show_plot(fig, 'motor_power_distribution'))

# 4. Maintenance Cost vs Training Cost
fig, ax = plt.subplots()
ax.scatter(df['maintenance_cost'], df['training_cost'])
ax.set_xlabel('Maintenance Cost')
ax.set_ylabel('Training Cost')
ax.set_title('Maintenance Cost vs Training Cost')
image_paths.append(save_and_show_plot(fig, 'maintenance_vs_training_cost'))

# 5. Iron Temperature vs Motor Temperature
fig, ax = plt.subplots()
ax.scatter(df['iron_temp'], df['motor_temp'])
ax.set_xlabel('Iron Temperature')
ax.set_ylabel('Motor Temperature')
ax.set_title('Iron Temperature vs Motor Temperature')
image_paths.append(save_and_show_plot(fig, 'iron_vs_motor_temp'))

print("All graphs generated, saved, and displayed successfully.")

