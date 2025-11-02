import pandas as pd
import numpy as np

# --- 1. Data Creation (Simulating the CSV file) ---
# Create a dictionary representing simple daily weather data
data = {
    'Date': pd.to_datetime(pd.date_range(start='2025-10-01', periods=10)),
    'City': ['Kolkata', 'Kolkata', 'Mumbai', 'Delhi', 'Kolkata', 'Mumbai', 'Delhi', 'Mumbai', 'Kolkata', 'Delhi'],
    'Temperature_C': np.random.randint(20, 35, 10),
    'Humidity_Pct': np.random.randint(60, 95, 10),
    'Rainfall_mm': [0, 5.2, 0, 1.1, 0, 8.5, 0, 0, 2.3, 0]
}

df_raw = pd.DataFrame(data)

# Save the DataFrame to a CSV file (your starting point)
CSV_FILE_PATH = 'sample_weather_data.csv'
df_raw.to_csv(CSV_FILE_PATH, index=False)

print(f"--- 1. CSV file created: {CSV_FILE_PATH} ---")
print("Sample Data Head:")
print(df_raw.head())
print("-" * 40)


# --- 2. Data Loading (Start Here with Your Own File) ---
# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(CSV_FILE_PATH)

# Ensure the 'Date' column is treated as datetime objects
df['Date'] = pd.to_datetime(df['Date'])

print("--- 2. Data Loaded Successfully ---")
print("-" * 40)


# --- 3. Basic Statistical Analysis ---
# A. Get descriptive statistics for all numerical columns
print("--- 3. A. Descriptive Statistics (Summary) ---")
basic_stats = df.describe()
print(basic_stats)
print("-" * 40)


# B. Compute Mean and Median for Temperature manually
temp_mean = df['Temperature_C'].mean()
temp_median = df['Temperature_C'].median()

print(f"B. Specific Metrics for Temperature:")
print(f"   Average Temperature (Mean): {temp_mean:.2f} °C")
print(f"   Middle Value (Median): {temp_median:.2f} °C")
print("-" * 40)


# C. Grouped Analysis: Mean Humidity by City
print("C. Grouped Analysis (Mean Humidity by City):")
mean_humidity_by_city = df.groupby('City')['Humidity_Pct'].mean()
print(mean_humidity_by_city)
print("-" * 40)

# D. Data shape and type check
print("D. Data Structure Check:")
print(f"   DataFrame Shape (Rows, Columns): {df.shape}")
print(f"   Column Data Types:\n{df.dtypes}")
print("-" * 40)