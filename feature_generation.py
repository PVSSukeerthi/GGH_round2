import os
import re
import pandas as pd
import subprocess

# Function to extract features from Yosys output
def extract_yosys_features(yosys_output):
    features = {
        "Number of wires": None,
        "Number of wire bits": None,
        "Number of public wires": None,
        "Number of public wire bits": None,
        "Number of memories": None,
        "Number of memory bits": None,
        "Number of processes": None,
        "Number of cells": None,
    }

    # Extract each feature using regex
    for line in yosys_output.split("\n"):
        for key in features.keys():
            match = re.search(rf"{key}:\s+(\d+)", line)
            if match:
                features[key] = int(match.group(1))

    return features

current_dir = os.path.dirname(os.path.abspath(__file__))
# All Verilog files 
verilog_files = [f"rtl_codes/rtl{i}.v" for i in range(1, 11)]  # rtl1.v, rtl2.v, ..., rtl10.v

# Data storage
data = []

# Process each Verilog file
for vfile in verilog_files:
    vfile_path = os.path.join(current_dir, vfile)
    
    # Run Yosys to get statistics
    yosys_cmd = f'yosys -p "read_verilog {vfile_path}; proc; opt; stat"'
    result = subprocess.run(yosys_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Extract features
        features = extract_yosys_features(result.stdout)
        features["File Name"] = vfile  # Add file name for reference
        data.append(features)
        print(f"Processed: {vfile}")
    else:
        print(f"Error processing {vfile}: {result.stderr}")

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
csv_path = os.path.join(current_dir, "yosys_features.csv")
df.to_csv(csv_path, index=False)

print(f"All features extracted and saved to {csv_path}")

