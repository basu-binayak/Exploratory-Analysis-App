import streamlit as st
import pandas as pd

# App title
st.set_page_config(page_title="EDA App", layout="wide")
st.title("📊 Exploratory Data Analysis App")
st.header("Upload your dataset and start exploring interactively!")

# Custom styled label
st.markdown(
    "<h4 style='font-size:22px;'>📂 Upload your CSV or Excel file</h4>",
    unsafe_allow_html=True
)

# File uploader (with empty label)
# Create a centered column layout
col1, col2, col3 = st.columns([2, 1, 1])  # middle column is wider
with col1:
    uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

