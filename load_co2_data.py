import numpy as np

# Read the CSV file directly as text
with open('daily_flask_co2_ljo.csv', 'r') as file:
    lines = file.readlines()

# Skip the first 68 rows (metadata)
data_lines = lines[68:]

# Parse the data
data_array = []
for line in data_lines:
    # Remove leading/trailing whitespace and newlines
    line = line.strip()
    if line:  # Skip empty lines
        # Split by comma
        values = [x.strip() for x in line.split(',')]
        data_array.append(values)

# Convert to numpy array with object dtype to handle variable-length rows
data_array = np.array(data_array, dtype=object)

# Print the array
print("Array of values from CSV file:")
print(data_array)
print("\nArray shape:", data_array.shape)
print("\nFirst 5 rows:")
print(data_array[:5])
print("\nColumn count in first row:", len(data_array[0]))
