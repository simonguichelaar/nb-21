import pandas as pd
import numpy as np

# Load the CSV file, skipping the first 68 rows of metadata
df = pd.read_csv('daily_flask_co2_ljo.csv', skiprows=68, header=None)

# Convert to numpy array
data_array = df.values

# Print the array
print("Array of values from CSV file:")
print(data_array)
print("\nArray shape:", data_array.shape)
print("\nFirst 5 rows:")
print(data_array[:5])
