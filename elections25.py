

import streamlit as st
import pandas as pd



"""
# Elections Canada - 2025

number of seats won by political parties as they are counted and displayed 
on the Canadian news.

"""


df = pd.read_csv("./elections2025.csv")

lib = df['LIB']
cons= df['CON']
bq = df['BQ']
ndp = df['NDP']
grn = df["GRN"]
oth = df['OTH']


chart_data = pd.DataFrame(
    {
        "LIB": lib,
        "CON": cons,
        "BQ": bq,
        "NDP": ndp,
        "GRN": grn,
        "OTH": oth,
    }
)

st.line_chart(chart_data, y_label="seats won", width=200, height=500)
