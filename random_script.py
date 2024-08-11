import numpy as np
import json
import pandas as pd
import os
from datetime import datetime
import time
import matplotlib.pyplot as plt

# Generate random data
data = {
    "mass": np.random.uniform(1, 100, 10).tolist(),
    "speed": np.random.uniform(0, 50, 10).tolist(),
    "height": np.random.uniform(0, 100, 10).tolist(),
    "wire_length": np.random.uniform(1, 10, 10).tolist(),
    "wire_diameter": np.random.uniform(0.1, 1, 10).tolist(),
    "motor_power": np.random.uniform(100, 1000, 10).tolist(),
    "operational_time": np.random.uniform(1, 24, 10).tolist(),
    "maintenance_cost": np.random.uniform(1000, 10000, 10).tolist(),
    "training_cost": np.random.uniform(500, 5000, 10).tolist(),
    "material_strength": np.random.uniform(100, 1000, 10).tolist(),
    "budget": np.random.uniform(10000, 100000, 10).tolist(),
    "location": np.random.uniform(0, 100, 10).tolist(),
    "reactant1": np.random.uniform(0, 50, 10).tolist(),
    "reactant2": np.random.uniform(0, 50, 10).tolist(),
    "sample_type": np.random.randint(1, 5, 10).tolist(),
    "wind_speed": np.random.uniform(0, 20, 10).tolist(),
    "area": np.random.uniform(10, 100, 10).tolist(),
    "iron_temp": np.random.uniform(100, 500, 10).tolist(),
    "motor_temp": np.random.uniform(100, 500, 10).tolist()
}

# Save data to JSON file
json_file_path = 'F:/FinalProject/data.json'
with open(json_file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("data.json file created successfully.")

# Create a new folder 'docs' if it doesn't exist
docs_folder = 'F:/FinalProject/docs'
if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

# Prepare data for CSV and Excel
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
start_time = time.time()

# Simulate experiment time
time.sleep(2)  # Simulate a 2-second experiment run time

end_time = time.time()
time_taken = end_time - start_time

experiment_data = {
    "timestamp": [timestamp],
    "time_taken": [time_taken],
    **{key: [value] for key, value in data.items()}
}

df = pd.DataFrame(experiment_data)

# File paths
csv_file_path = os.path.join(docs_folder, 'RandomExperiments.csv')
xlsx_file_path = os.path.join(docs_folder, 'RandomExperiments.xlsx')

# Append data to CSV file
if os.path.exists(csv_file_path):
    df.to_csv(csv_file_path, mode='a', header=False, index=False)
else:
    df.to_csv(csv_file_path, index=False)

# Append data to Excel file
if os.path.exists(xlsx_file_path):
    with pd.ExcelWriter(xlsx_file_path, mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
else:
    df.to_excel(xlsx_file_path, index=False)

print("Experiment data saved to CSV and Excel files successfully.")

# Generate an image of the tabular data
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

image_file_path = os.path.join(docs_folder, 'experiment_data.png')
plt.savefig(image_file_path, bbox_inches='tight')
plt.close()

print("Tabular data image saved successfully.")
