import pandas as pd
import warnings
import os

warnings.filterwarnings('ignore')

# Get current script path (src folder)
current_path = os.path.dirname(os.path.abspath(__file__))

# Navigate to 'data' folder which is at the same level as 'src'
# (Moving up one level then into 'data')
data_dir = os.path.join(current_path, '..', 'data')
output_filename = os.path.join(data_dir, "master_flight_data.csv")

# Actual file names to merge
csv_files = [
    "flight1.csv",
    "flight2.csv",
    "midflight.csv",
    "midflight1.csv",
    "midflight2.csv",
    "midflight3.csv",
    "midflight4.csv",
    "Mix data from LoRa.csv"
]

df_list = []
print(f"Targeting data directory: {os.path.abspath(data_dir)}")

for file_name in csv_files:
    file_path = os.path.join(data_dir, file_name)
    
    if not os.path.exists(file_path):
        print(f"Warning: '{file_name}' not found. Skipping...")
        continue
        
    print(f"Reading: {file_name}")
    try:
        # Load and clean corrupted lines/columns
        df = pd.read_csv(file_path, on_bad_lines='skip', low_memory=False)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

if not df_list:
    print("\n❌ Error: No CSV files found in 'data' folder.")
    print(f"Check path: {os.path.abspath(data_dir)}")
    exit()

# Processing
print("Merging and sorting data...")
master_df = pd.concat(df_list, ignore_index=True)
master_df = master_df.drop_duplicates()
master_df = master_df[master_df['Temp'] != 'Temp']

# Chronological Sort by Package Number
master_df['Pack_Num'] = master_df['Package'].astype(str).str.extract(r'\[(\d+)\]').astype(float)
master_df = master_df.dropna(subset=['Pack_Num']).sort_values('Pack_Num')
master_df = master_df.drop(columns=['Pack_Num'])

# Save to data folder
master_df.to_csv(output_filename, index=False)
print("-" * 40)
print(f"Done! Created: {output_filename}")
print(f"Total clean rows: {len(master_df)}")