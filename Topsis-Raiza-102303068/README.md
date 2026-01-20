# Topsis-Raiza-102303068

## Description
This Python package implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method used in Multi-Criteria Decision Making (MCDM).

It allows users to rank alternatives based on multiple criteria using command-line input.

---

## Installation

Install the package from PyPI using:

```bash
pip install Topsis-Raiza-102303068
```

---

## Command Line Usage

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputFile>
```

---

## Example

```bash
topsis data.csv "1,1,1,2,1" "+,+,-,+,-" output.csv
```

---

## Input File Format

- First column: Name of alternatives (e.g., Fund Name)
- Remaining columns: Numeric criteria values
- Minimum 3 columns required
- Weights and impacts must match number of criteria

---

## Output File

The output CSV file contains:
- All original columns
- `Topsis Score`
- `Rank` (higher score = better rank)

---

## Requirements

- Python 3.7+
- pandas
- numpy

---

## Author

Raiza Duggal  
Roll No: 102303068
