import streamlit as st
import pandas as pd
import numpy as np
import re

st.set_page_config(page_title="TOPSIS Web Service", layout="centered")

st.title("TOPSIS Web Service")
st.write("Upload a CSV file and provide weights & impacts to compute TOPSIS ranking.")

# ---------------- TOPSIS FUNCTION ----------------
def topsis(df, weights, impacts):
    data = df.iloc[:, 1:].astype(float)

    weights = np.array(weights)
    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    return df

# ---------------- UI ----------------
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
weights_input = st.text_input("Weights (comma separated)", "1,1,1,1")
impacts_input = st.text_input("Impacts (comma separated)", "+,+,-,+")
email = st.text_input("Email ID (for assignment requirement)")

if st.button("Submit"):
    if uploaded_file is None:
        st.error("Please upload a CSV file")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.error("Invalid email format")
    else:
        weights = weights_input.split(",")
        impacts = impacts_input.split(",")

        if len(weights) != len(impacts):
            st.error("Weights and impacts must be equal")
        elif not all(i in ['+', '-'] for i in impacts):
            st.error("Impacts must be + or -")
        else:
            df = pd.read_csv(uploaded_file)
            result = topsis(df, list(map(float, weights)), impacts)

            st.success("TOPSIS calculation completed successfully")
            st.dataframe(result)

            csv = result.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Result CSV",
                data=csv,
                file_name="topsis_result.csv",
                mime="text/csv"
            )

            st.info("📌 Email sending is disabled on Streamlit due to security restrictions.")
