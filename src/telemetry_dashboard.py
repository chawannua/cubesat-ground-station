import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings('ignore')

# Set path to the master file in the 'data' folder
current_path = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(current_path, '..', 'data', 'master_flight_data.csv')

plt.style.use('dark_background')

def load_master_data(path):
    print(f"Opening: {path}")
    if not os.path.exists(path):
        print("Error: Master file not found. Run merge_data.py first.")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(path)
        # Convert necessary columns to numeric
        numeric_cols = ['Temp', 'Axis X', 'Axis Y', 'Axis Z', 'Latitude', 'Longitude']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df.dropna(subset=numeric_cols).reset_index(drop=True)
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

df = load_master_data(FILE_PATH)

if df.empty:
    exit()

# Dashboard UI Setup
fig = plt.figure(figsize=(12, 8))
fig.canvas.manager.set_window_title('Flight Analysis - Master Data')

# 1. Temperature Profile
ax1 = plt.subplot(2, 1, 1)
ax1.plot(df.index, df['Temp'], color='#00ffcc', label='Temp (C)')
ax1.set_title('Temperature Profile')
ax1.set_ylabel('Celsius')
ax1.grid(True, alpha=0.2)
ax1.legend()

# 2. GPS Path
ax2 = plt.subplot(2, 2, 3)
ax2.plot(df['Longitude'], df['Latitude'], color='#ff00ff')
ax2.set_title('GPS Flight Path')
ax2.set_xlabel('Lon')
ax2.set_ylabel('Lat')
ax2.grid(True, alpha=0.2)

# 3. IMU Data
ax3 = plt.subplot(2, 2, 4)
ax3.plot(df.index, df['Axis X'], label='X', alpha=0.7)
ax3.plot(df.index, df['Axis Y'], label='Y', alpha=0.7)
ax3.plot(df.index, df['Axis Z'], label='Z', alpha=0.7)
ax3.set_title('Acceleration Forces')
ax3.legend()
ax3.grid(True, alpha=0.2)

plt.tight_layout()
print("Displaying dashboard...")
plt.show()