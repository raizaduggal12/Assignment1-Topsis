def main():
    import sys
    import pandas as pd
    import numpy as np
    import os

    def error(msg):
        print(f"Error: {msg}")
        sys.exit(1)

    if len(sys.argv) != 5:
        error("Usage: topsis <InputDataFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        error("Input file not found")

    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)

    if df.shape[1] < 3:
        error("Input file must contain three or more columns")

    data = df.iloc[:, 1:]

    try:
        data = data.astype(float)
    except:
        error("Columns from 2nd onward must be numeric")

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        error("Weights, impacts and columns count mismatch")

    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be '+' or '-'")

    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully.")


if __name__ == "__main__":
    main()
