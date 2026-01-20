import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

# ------------------ STEP 1: Check Arguments ------------------
if len(sys.argv) != 5:
    error("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")

input_file = sys.argv[1]
weights = sys.argv[2]
impacts = sys.argv[3]
output_file = sys.argv[4]

# ------------------ STEP 2: Check File Exists ------------------
if not os.path.exists(input_file):
    error("Input file not found")

# ------------------ STEP 3: Read File ------------------
try:
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)
except:
    error("Unable to read input file")

# ------------------ STEP 4: Column Validation ------------------
if df.shape[1] < 3:
    error("Input file must contain three or more columns")

data = df.iloc[:, 1:]

# ------------------ STEP 5: Numeric Check ------------------
try:
    data = data.astype(float)
except:
    error("From 2nd column to last column must contain numeric values only")

# ------------------ STEP 6: Weights & Impacts Validation ------------------
weights = list(map(float, weights.split(",")))
impacts = impacts.split(",")

if len(weights) != data.shape[1]:
    error("Number of weights must be equal to number of criteria")

if len(impacts) != data.shape[1]:
    error("Number of impacts must be equal to number of criteria")

for i in impacts:
    if i not in ['+', '-']:
        error("Impacts must be either '+' or '-'")

# ------------------ STEP 7: Normalize ------------------
norm = np.sqrt((data ** 2).sum())
normalized_data = data / norm

# ------------------ STEP 8: Apply Weights ------------------
weighted_data = normalized_data * weights

# ------------------ STEP 9: Ideal Best & Worst ------------------
ideal_best = []
ideal_worst = []

for i in range(len(impacts)):
    if impacts[i] == '+':
        ideal_best.append(weighted_data.iloc[:, i].max())
        ideal_worst.append(weighted_data.iloc[:, i].min())
    else:
        ideal_best.append(weighted_data.iloc[:, i].min())
        ideal_worst.append(weighted_data.iloc[:, i].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

# ------------------ STEP 10: Distance Measures ------------------
distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

# ------------------ STEP 11: TOPSIS Score ------------------
topsis_score = distance_worst / (distance_best + distance_worst)

# ------------------ STEP 12: Ranking ------------------
df["Topsis Score"] = topsis_score
df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

# ------------------ STEP 13: Save Output ------------------
df.to_csv(output_file, index=False)
print("TOPSIS analysis completed successfully.")
