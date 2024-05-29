import streamlit as st
import csv

st.title("Interview setup page for Interviewer")

uploaded_file = st.file_uploader("Upload interview file", type=("csv"))

if st.button('Submit', key='submit_button'):
    reader = csv.reader(csv_file)
        

