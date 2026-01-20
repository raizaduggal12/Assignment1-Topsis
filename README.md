# TOPSIS Assignment – Complete Implementation (Part I, II & III)

This repository contains the complete implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method developed as part of an academic assignment.
The project is implemented in **three parts**:
1. Command Line Tool
2. Python Package (PyPI)
3. Web Service (Flask)

---

## 📌 About TOPSIS

TOPSIS is a **multi-criteria decision-making (MCDM)** technique used to rank alternatives based on their distance from:
- the **ideal best solution**
- the **ideal worst solution**

The alternative closest to the ideal best and farthest from the ideal worst is ranked highest.

---

## 📁 Repository Structure

```
Assign/
├── Part1/                     # Part I – Command Line Program
│   └── topsis.py
│
├── Topsis-Raiza-102303068/     # Part II – PyPI Package
│
├── Part3_topsis_web/           # Part III – Web Service
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── uploads/
│   └── results/
│
└── README.md
```

> **Note:** The folder structure and code are kept exactly as implemented.

---

## 🔹 PART I – TOPSIS Command Line Tool

### Description
This part implements TOPSIS as a **command-line Python program**.
The user provides:
- Input CSV file
- Weights
- Impacts
- Output file name

The program calculates TOPSIS scores and ranks the alternatives.

### How to Run
```bash
python topsis.py input.csv "1,1,1,1" "+,+,-,+" output.csv
```

### Output
A CSV file containing:
- **TOPSIS Score**
- **Rank of each alternative**

---

## 🔹 PART II – TOPSIS Python Package (PyPI)

### Description
In this part, the TOPSIS logic is converted into a **reusable Python package** and published on **PyPI**.

### Package Name
```
Topsis-Raiza-102303068
```

### Installation
```bash
pip install Topsis-Raiza-102303068
```

### Usage
```bash
topsis input.csv "1,1,1,1" "+,+,-,+" output.csv
```

### Features
- Installable via `pip`
- Command-line interface
- Input validation
- Reusable TOPSIS implementation

---

## 🔹 PART III – TOPSIS Web Service (Flask)

### Description
This part implements TOPSIS as a **web service using Flask**.
The user can:
- Upload a CSV file
- Enter weights and impacts
- Provide an email ID
- Receive the result via email

### How to Run
```bash
cd Part3_topsis_web
python app.py
```

Open in browser:
```
http://127.0.0.1:5000/
```

### Features
- Web-based interface
- File upload support
- Weights and impacts validation
- Email ID validation
- TOPSIS score and ranking
- Result sent as CSV file via email

> **Note:**
> Email functionality is implemented using SMTP.
> Due to security restrictions, email delivery may depend on account and network settings.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Flask
- SMTP (Email)
- setuptools (PyPI packaging)

---

## 👩‍💻 Author

**Raiza Duggal**
TOPSIS Assignment – Part I, II & III

---

## 🎓 Conclusion

This project demonstrates the complete lifecycle of a data science application:
- Command-line computation
- Packaging and distribution using PyPI
- Web-based implementation using Flask

The implementation follows proper validation, modular design, and academic requirements.
