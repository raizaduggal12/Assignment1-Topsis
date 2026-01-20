# 📊 TOPSIS Implementation – Assignment 1

This repository contains **Assignment-1 on TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** implemented in **three complete parts**:

1. **Part-I:** Command Line TOPSIS Program (Python)
2. **Part-II:** Python Package published on PyPI
3. **Part-III:** Web Application deployed using Streamlit

All parts are fully implemented, tested, and deployed successfully.

---

## 📌 What is TOPSIS?

**TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** is a Multi-Criteria Decision Making (MCDM) method used to rank alternatives based on:

- Minimum distance from the **ideal solution**
- Maximum distance from the **negative-ideal solution**

TOPSIS is widely used in:
- Decision analysis
- Ranking problems
- Analytics and data science applications

---

## 📂 Project Directory Structure

Assign/
│
├── Part1/
│ ├── data.csv
│ ├── output.csv
│ └── topsis.py
│
├── Topsis-Raiza-102303068/
│ ├── topsis_raiza_102303068/
│ ├── setup.py
│ ├── pyproject.toml
│ ├── LICENSE
│ └── README.md
│
├── Part3_topsis_web/
│
├── Screenshots/
│ ├── terminal_run.png
│ ├── pypi_page.png
│ ├── ui_form.png
│ └── email_result.png
│
└── README.md

yaml
Copy code

---

## 🚀 Part-I: Command Line TOPSIS Program

### 🔹 Description
A Python-based command-line program that:
- Takes a CSV file as input
- Accepts weights and impacts as command-line arguments
- Calculates TOPSIS scores
- Generates ranked results in a CSV output file

---

### 🔹 Command Line Usage

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>
🔹 Example
bash
Copy code
python topsis.py data.csv "1,1,1,1" "+,+,+,+" output.csv
🔹 Input File Format
First column: Name of alternatives (e.g., Fund Name)

Remaining columns: Numeric criteria values

Minimum 3 columns required

Example Input (data.csv)
nginx
Copy code
Fund Name,P1,P2,P3,P4
M1,0.81,0.66,6.7,58.3
M2,0.89,0.79,3.9,68.3
M3,0.70,0.49,6.0,48.6
🔹 Output File Format
The output CSV file contains:

All original columns

TOPSIS Score

Rank (Higher score = better rank)

Example Output (output.csv)
nginx
Copy code
Fund Name,P1,P2,P3,P4,Topsis Score,Rank
M1,0.81,0.66,6.7,58.3,0.3993,5
M2,0.89,0.79,3.9,68.3,0.8598,1
🔹 Validations Implemented
✔ Correct number of command-line arguments
✔ File not found exception handling
✔ Minimum column validation
✔ Numeric data validation (2nd column onwards)
✔ Matching number of weights, impacts, and criteria
✔ Impacts allowed only as + or -
✔ Clear and meaningful error messages

🔹 Command Line Execution Screenshot

📦 Part-II: Python Package Published on PyPI
🔹 Package Information
Package Name: Topsis-Raiza-102303068

Version: 1.0.0

License: MIT

Python Version: ≥ 3.7

🔗 PyPI Link:
https://pypi.org/project/Topsis-Raiza-102303068/

🔹 Installation from PyPI
bash
Copy code
pip install Topsis-Raiza-102303068
🔹 Command Line Usage (After Installation)
bash
Copy code
topsis <InputDataFile> <Weights> <Impacts> <OutputFile>
Example
bash
Copy code
topsis data.csv "1,1,1,1" "+,+,+,+" output.csv
🔹 Dependencies
Python ≥ 3.7

pandas

numpy

🔹 PyPI Package Screenshot

🌐 Part-III: TOPSIS Web Application (Streamlit)
🔹 Description
A fully functional web-based TOPSIS calculator developed using Streamlit.
It allows users to compute TOPSIS rankings without using the command line.

🔹 Live Application Link
🚀 Streamlit App:
https://raiza-topsis.streamlit.app/

🔹 Web Application Features
✔ CSV file upload
✔ Weights input (comma-separated)
✔ Impacts input (+ or -)
✔ Email ID validation
✔ TOPSIS computation
✔ Result table display
✔ Download result as CSV

⚠️ Note: Email sending is disabled due to Streamlit security restrictions.

🔹 Web Application UI Screenshot

🔹 Result Output Screenshot

🛠 Technologies Used
Python

NumPy

Pandas

Streamlit

PyPI

Git & GitHub

👩‍💻 Author
Raiza Duggal
Roll No: 102303068
B.Tech – Computer Science

📜 License
This project is licensed under the MIT License.



