from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# ---------------- TOPSIS FUNCTION ----------------
def topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    data = df.iloc[:, 1:].astype(float)

    weights = np.array(weights, dtype=float)

    # Step 1: Normalize
    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm

    # Step 2: Apply weights
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    # Step 3: Ideal best & worst
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance
    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score & Rank
    score = d_neg / (d_pos + d_neg)
    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)

# ---------------- EMAIL FUNCTION ----------------
def send_email(receiver_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "raizaduggal1@gmail.com"
    msg["To"] = receiver_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    # Gmail SMTP
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(
        "raizaduggal1@gmail.com",
        "zceh hgqc dqmm wzmf"   # <-- paste app password here
    )
    server.send_message(msg)
    server.quit()

# ---------------- ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not file or not weights or not impacts or not email:
            return render_template("index.html", message="All fields are required")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template("index.html", message="Invalid Email ID")

        weights = weights.split(",")
        impacts = impacts.split(",")

        if len(weights) != len(impacts):
            return render_template("index.html", message="Weights and impacts count must be equal")

        if not all(i in ['+', '-'] for i in impacts):
            return render_template("index.html", message="Impacts must be + or -")

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(RESULT_FOLDER, "result.csv")

        file.save(input_path)

        # Validate columns vs weights
        df_check = pd.read_csv(input_path)
        if len(weights) != (df_check.shape[1] - 1):
            return render_template(
                "index.html",
                message="Number of weights must match number of criteria columns"
            )

        topsis(input_path, list(map(float, weights)), impacts, output_path)

        try:
            send_email(email, output_path)
            msg = "Result sent to email successfully!"
        except Exception as e:
            msg = "Result generated, but email could not be sent (SMTP blocked)."

        return render_template("index.html", message=msg)

    return render_template("index.html")

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
