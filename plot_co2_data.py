import pandas as pd

# Define column names
columns = ['Date', 'Time', 'Excel_Date', 'Decimal_Year', 'NumFlasks', 'Flag', 'CO2_ppm']

# Read CSV, skipping header lines that start with quotes
df = pd.read_csv('daily_flask_co2_ljo.csv', 
                   comment='"',  # Skip lines starting with quotes
                   sep=',\s*',   # Handle whitespace around commas
                   engine='python',
                   names=columns,
                   header=None)

# Display first 5 rows
print("First 5 rows of CO2 data:\n")
print(df.head())

# Optional: Display info about the dataframe
print(f"\nDataframe shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
